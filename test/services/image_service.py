from PIL import Image
import base64
import requests
from io import BytesIO
from models.groq_client import GroqClient

class ImageService:
    """Handles image analysis operations"""
    
    def __init__(self):
        self.groq_client = GroqClient()
    
    def analyze_image_from_base64(self, base64_string, prompt="Describe this image in detail."):
        """
        Analyze an image from base64 string
        
        Args:
            base64_string: Base64 encoded image string
            prompt: Analysis prompt (default: "Describe this image in detail.")
            
        Returns:
            Analysis result string
        """
        try:
            # Decode and validate image
            image_data = base64.b64decode(base64_string)
            image = Image.open(BytesIO(image_data))
            
            # Prepare message for Groq API
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_string}"
                            }
                        }
                    ]
                }
            ]
            
            return self.groq_client.analyze_image(messages)
            
        except Exception as e:
            return f"Error processing base64 image: {str(e)}"
    
    def analyze_image_from_url(self, image_url, prompt="Describe this image in detail."):
        """
        Analyze an image from URL
        
        Args:
            image_url: URL of the image
            prompt: Analysis prompt (default: "Describe this image in detail.")
            
        Returns:
            Analysis result string
        """
        try:
            # Download and validate image
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            
            # Prepare message for Groq API
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": image_url}
                        }
                    ]
                }
            ]
            
            return self.groq_client.analyze_image(messages)
            
        except requests.exceptions.RequestException as e:
            return f"Error downloading image: {str(e)}"
        except Exception as e:
            return f"Error processing image from URL: {str(e)}"