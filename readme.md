# SDIM

## Stable Diffusion Flask Image Generator

This project provides a Flask-based web application that allows users to generate images from text prompts using the Stable Diffusion model. The app runs the Stable Diffusion model in the background, showing a loading indicator while the image is being generated, and allows users to download or delete the generated image.

## Features
- Generate images using the Stable Diffusion model
- Background processing for image generation
- Option to download or delete the generated image

## Requirements

- Python 3.8+
- Docker (for containerized deployment)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/stable-diffusion-flask-app.git
   cd stable-diffusion-flask-app
   pip install -r requirements.txt
   python app.py
   ```

2 Using Docker in local:
   ```bash
   docker pull rajeshacts/sdim
   docker run -d -p 5000:5000 --name sdim rajeshacts/sdim:01
   ```
