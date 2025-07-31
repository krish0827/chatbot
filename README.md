Image Generation Chatbot

This project is an image generation chatbot that allows users to generate and edit images using text prompts. It combines:

- `Stable Diffusion v1.5` for image generation from text
- `InstructPix2Pix` for image editing based on instructions

Features

- Text-to-image generation
- Image editing using natural language prompts

 Models Used

- [`runwayml/stable-diffusion-v1-5`] (https://huggingface.co/runwayml/stable-diffusion-v1-5)
- [`timbrooks/instruct-pix2pix`] (https://huggingface.co/timbrooks/instruct-pix2pix)

 Installation

1. Clone the repo:


git clone https://github.com/krish0827/image-generation-chatbot.git
cd image-generation-chatbot.git

2.Install dependencies:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121  # or cpu-only
pip install diffusers gradio transformers accelerate safetensors pillow

3.Run the app
python chatbot.py

After launching, a Gradio web interface will open where you can type prompts like:

"A futuristic city at sunset"

"Make it look like a painting"

"Add snow and make it night"





