execute_commands()
from flask import Flask, request, jsonify, render_template, send_file
import os
from workflow import image_to_text_to_audio
from prepare import execute_commands

# Initialize the Flask app
app = Flask(__name__)

# Folder to save generated audio files
AUDIO_FOLDER = 'audio'
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER

# Ensure the audio folder exists
os.makedirs(AUDIO_FOLDER, exist_ok=True)

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

    if 'language' not in request.form:
        return jsonify({'error': 'No language selected'}), 400

    language = request.form['language']
    print(language)

    # Generate caption and audio file
    caption = image_to_text_to_audio(file, language)

    # Assuming 'output.mp3' is the generated audio file
    audio_path = os.path.join(app.config['AUDIO_FOLDER'], 'output.mp3')

    return jsonify({'prediction': caption, 'audio_file': 'output.mp3'})

@app.route('/audio/<filename>')
def get_audio(filename):
    return send_file(os.path.join(app.config['AUDIO_FOLDER'], filename))

if __name__ == '__main__':
    app.run(debug=True)
