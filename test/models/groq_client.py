from groq import Groq
from config import Config

class GroqClient:
    """Wrapper for Groq API client"""
    
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)
    
    def create_chat_completion(self, messages, model=None, temperature=None, max_tokens=None):
        """
        Create a chat completion using Groq API
        
        Args:
            messages: List of message dictionaries
            model: Model name (defaults to config)
            temperature: Response randomness (defaults to config)
            max_tokens: Maximum tokens in response (defaults to config)
            
        Returns:
            Response content string or error message
        """
        try:
            response = self.client.chat.completions.create(
                model=model or Config.DEFAULT_MODEL,
                messages=messages,
                temperature=temperature or Config.TEMPERATURE,
                max_tokens=max_tokens or Config.MAX_TOKENS
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def analyze_image(self, messages):
        """
        Analyze image using Groq's vision capabilities
        
        Args:
            messages: List of message dictionaries with image content
            
        Returns:
            Analysis result string or error message
        """
        try:
            response = self.client.chat.completions.create(
                model="llama-3.2-11b-vision-preview",
                messages=messages,
                temperature=0.7,
                max_tokens=1024
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error analyzing image: {str(e)}"