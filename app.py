from flask import Flask, request, jsonify
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch

app = Flask(__name__)

# Load ViT-GPT2 model
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

@app.route("/caption", methods = ["GET", "POST"]) # This defines the URL and method
def caption_get():                       # This is the function that handles it
    if request.method == "GET":
        return "🟢 Captioning API is live. Send a POST request with an image."

    # This block only runs for POST
    if "image" not in request.files:
        return "❌ No image file found in the request", 400
    file = request.files["image"]          # Step 1: Get the uploaded image
    image = Image.open(file.stream).convert("RGB")      # Step 2: Open and process the image
    pixel_values = processor(images=image, return_tensors = "pt").pixel_values
    output_ids = model.generate(pixel_values, max_length = 16, num_beams= 4)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens= True)
    return "🟢 Send a POST request to /caption with an image file (key='image')."
if __name__ == "__main__":
    app.run(debug = "True")





