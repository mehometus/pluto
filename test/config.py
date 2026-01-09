import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the AI Chatbot"""
    
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY")
    
    # Model Settings
    DEFAULT_MODEL = "llama-3.1-8b-instant"
    TEMPERATURE = 0.7
    MAX_TOKENS = 1024
    
    # Server Settings
    HOST = "localhost"
    PORT = 5000
    DEBUG = True
    
    # System Prompt
    SYSTEM_PROMPT = (
        "You are an expert AI Assistant. "
        "CRITICAL RULES:\n"
        "1. NEVER mention your knowledge cutoff, training date, or that you are an AI.\n"
        "2. Be direct, conversational, and helpful.\n"
        "3. Provide clear and accurate responses.\n"
        "4. Do not apologize for your limitations; simply provide the answer."
    )