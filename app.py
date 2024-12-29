from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import torch
from diffusers import StableDiffusionPipeline
import time
from threading import Lock, Thread

app = Flask(__name__)

# Initialize the model once at the start
model = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
model.to("cpu")

# Folder to store generated images
UPLOAD_FOLDER = 'generated_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Lock to ensure thread safety for image generation
lock = Lock()

# Helper function to generate the image
def generate_image(prompt, image_path):
    image = model(prompt).images[0]
    image.save(image_path)

# Route to handle the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the image generation process
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    image_filename = f"image_{int(time.time())}.png"
    image_path = os.path.join(UPLOAD_FOLDER, image_filename)

    # Start image generation in a separate thread
    def generate_in_background():
        with lock:
            generate_image(prompt, image_path)

    Thread(target=generate_in_background).start()

    return jsonify({'status': 'image generation started', 'image_url': image_filename})

# Route to serve the generated image
@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Route to delete the generated image
@app.route('/delete/<filename>', methods=['POST'])
def delete_image(filename):
    try:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({'status': 'image deleted'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

