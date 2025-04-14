# Image Captioning with BLIP

A FastAPI-based web application that generates captions, titles, and tags for images using the BLIP (Bootstrapping Language-Image Pre-training) model.

## Features

- Upload images through a web interface
- Generate detailed image captions
- Extract relevant tags
- Create concise titles
- Real-time processing
- Modern, responsive UI

## Prerequisites

- Python 3.9+
- Conda (recommended) or any Python virtual environment tool

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/hidingbehindrainbows/LLM-Image-Captioning.git>
```

2. Set up a Python virtual environment using one of these options:

Option 1 - Using Conda (Recommended):
```bash
conda create -n your-env-name python=3.9
conda activate your-env-name
```

Option 2 - Using venv (Python's built-in tool):
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Option 3 - Using virtualenv:
```bash
pip install virtualenv
virtualenv your-env-name
# For Windows
.\your-env-name\Scripts\activate
# For macOS/Linux
source your-env-name/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

Note: The environment name (e.g., 'your-env-name') can be anything you choose. Just remember to use the same name when activating the environment.

## Running the Application

1. Start the FastAPI server:
```bash
python run.py
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

## Project Structure

```
.
├── backend/
│   ├── __init__.py
│   ├── main.py
│   └── image_processor.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── requirements.txt
├── run.py
└── README.md
```

## API Endpoints

- `POST /analyze-image`: Upload and process an image
  - Input: Form data with image file
  - Output: JSON with title, description, and tags

## Environment Variables

No environment variables are required for basic functionality. The application automatically detects if CUDA is available and uses CPU if it's not.

## Model Information

The application uses BLIP (Bootstrapping Language-Image Pre-training) for image captioning:
- Default model: "Salesforce/blip-image-captioning-large"
- Alternative models available:
  - "Salesforce/blip2-opt-2.7b"
  - "Salesforce/blip2-flan-t5-xl"
  - "Salesforce/blip2-opt-6.7b"

## Dependencies

Major dependencies include:
- FastAPI
- Torch
- Transformers
- Pillow
- NLTK
- uvicorn

See `requirements.txt` for complete list.

## Development

To run the application in development mode with auto-reload:
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

## Troubleshooting

1. If you encounter CUDA errors:
   - The application will automatically fall back to CPU
   - Ensure you have the correct torch version installed

2. If you get import errors:
   - Ensure you're in the correct conda environment
   - Try reinstalling dependencies: `pip install -r requirements.txt`
