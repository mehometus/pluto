import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_bp
from config import Config

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(chat_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    print("=" * 60)
    print("🤖 AI CHATBOT SERVER STARTING")
    print("=" * 60)
    print(f"Host: {Config.HOST}")
    print(f"Port: {Config.PORT}")
    print(f"Model: {Config.DEFAULT_MODEL}")
    print("=" * 60)
    
    app = create_app()
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )