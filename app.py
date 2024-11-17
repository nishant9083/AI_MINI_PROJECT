from flask import Flask, request, jsonify, render_template
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import io
import pickle

# Initialize the Flask app
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get image file from request
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Process the image
    img = Image.open(io.BytesIO(file.read()))
    img = transform(img).unsqueeze(0)  # Add batch dimension

    # Make prediction
    with torch.no_grad():
        output = model(img)
        _, predicted = torch.max(output.data, 1)
        digit = predicted.item()
    
    return jsonify({'prediction': digit})

if __name__ == '__main__':
    app.run(debug=True)
