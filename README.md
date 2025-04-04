# image-caption-app

A small but practical Python script that combines computer vision with natural language generation — using a single Flask API and a Hugging Face model.
The idea was simple:
 Take an uploaded image → run it through a vision-language transformer model → return a caption.
⚙️ What I used: • Python + Flask for the API
 • Hugging Face ViT-GPT2 model for image captioning
 • PyTorch for model inference
 • Pillow (PIL) for image handling
🔍 What I explored: • How pretrained vision-language models work in practice
 • Running inference locally in a minimal Flask app
 • Handling file uploads and integrating model logic into a simple backend
 • Debugging common API issues (KeyErrors, method routing, etc.)

