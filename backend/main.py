from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
from .image_processor import ImageProcessor

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize image processor
processor = ImageProcessor()

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    # Read the image file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    # Process the image
    result = processor.process_image(image)
    return result

# Mount static files
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend") 