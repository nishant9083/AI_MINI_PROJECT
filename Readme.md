# Image Captioning Web Application

## Overview

This is a Flask web application that allows users to upload an image, select a language, and receive a text caption along with an audio file of the caption in the selected language. The application uses machine learning models to generate captions and convert text to speech.

## Features

- Upload images to generate captions.
- Select from multiple languages for the caption.
- Receive audio playback of the caption in the selected language.
- Supports multiple languages including Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Punjabi (Gurmukhi), Tamil, Telugu, and Urdu.

## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/nishant9083/AI_MINI_PROJECT.git
    cd AI_MINI_PROJECT
    ```

2. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Ensure the audio directories exist:**

    ```sh
    mkdir -p audio
    ```

4. **Prepare your model and workflow:**

   Make sure you have the necessary models and scripts in place for image captioning and text-to-audio conversion. The example assumes you have a `workflow.py` file with an `image_to_text_to_audio` function.

## Usage

1. **Run the Flask application:**

    ```sh
    python app.py
    ```

2. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:5000
    ```

3. **Upload an image and select the desired language:**

    - Choose an image file.
    - Select a language from the dropdown menu.
    - Click the "Caption It" button.

4. **Receive the generated caption and audio:**

    - The application will display the caption as text.
    - An audio file will be generated and played in the selected language.

## API Endpoints

- **`GET /`**: Home page. Renders the upload interface.
- **`POST /predict`**: Accepts an image file and a language code. Returns the caption and audio file.
- **`GET /audio/<filename>`**: Serves the generated audio file.

## Code Structure

- **`app.py`**: Main Flask application file.
- **`templates/index.html`**: HTML file for the upload interface.
- **`workflow.py`**: Script containing the `image_to_text_to_audio` function for generating captions and audio.

## Example Workflow

1. Upload an image.
2. Select a language from the dropdown.
3. Click "Caption It."
4. The application processes the image, generates a caption, converts the caption to audio, and displays/plays the results.

## Notes

- This example uses the `gTTS` library for text-to-speech conversion. Ensure it is included in your `requirements.txt`.
- Adjust paths and configuration as needed for your specific environment and setup.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

