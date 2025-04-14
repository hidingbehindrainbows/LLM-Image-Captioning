import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from nltk.corpus import stopwords
import nltk
import string

class ImageProcessor:
    def __init__(self):
        """Initialize the BLIP image captioning model"""
        # Download required NLTK data
        nltk.download('stopwords', quiet=True)
        
        # Initialize the BLIP model and processor
        model_name = "Salesforce/blip-image-captioning-large"
        # model_name = "Salesforce/blip2-opt-2.7b"
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)
        
        # Set device
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = self.model.to(self.device)

    def extract_tags(self, caption):
        """Extract relevant tags from the caption"""
        stop_words = set(stopwords.words('english'))
        words = caption.lower().translate(str.maketrans('', '', string.punctuation)).split()
        tags = set(word for word in words if word not in stop_words and len(word) > 3)
        return list(tags)

    def generate_title(self, caption):
        """Generate a title from the caption"""
        first_sentence = caption.split('.')[0]
        words = first_sentence.split()
        articles = {'a', 'an', 'the', 'in', 'on', 'at', 'there', 'is', 'are'}
        title_words = [w for w in words if w.lower() not in articles]
        title = ' '.join(title_words[:5]).capitalize()
        return title

    def preprocess_image(self, image):
        """Convert PIL Image to tensor without using numpy"""
        # Ensure image is RGB
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # Resize to a standard size
        image = image.resize((224, 224))
        
        # Convert to tensor directly from PIL
        image_tensor = torch.FloatTensor(image.getdata()).view(1, 224, 224, 3)
        # Normalize to [0, 1]
        image_tensor = image_tensor / 255.0
        # Permute dimensions to [batch, channels, height, width]
        image_tensor = image_tensor.permute(0, 3, 1, 2)
        
        return image_tensor

    def process_image(self, image):
        """Process an image and return metadata"""
        try:
            # Preprocess image to tensor
            image_tensor = self.preprocess_image(image)
            image_tensor = image_tensor.to(self.device)
            
            # Generate caption directly with the model
            with torch.no_grad():
                outputs = self.model.generate(
                    pixel_values=image_tensor,
                    max_length=50,
                    num_beams=1,
                    min_length=5
                )
            
            # Decode caption
            caption = self.processor.decode(outputs[0], skip_special_tokens=True)
            caption = caption.strip().capitalize()
            
            # Generate title and tags
            title = self.generate_title(caption)
            tags = self.extract_tags(caption)
            
            return {
                "title": title,
                "description": caption,
                "tags": tags
            }
            
        except Exception as e:
            print(f"Error processing image: {str(e)}")
            print(f"Error type: {type(e)}")
            import traceback
            print(traceback.format_exc())
            return {
                "title": "Error processing image",
                "description": str(e),
                "tags": []
            } 