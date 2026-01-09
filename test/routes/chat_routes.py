from flask import Blueprint, request, jsonify
from services.chat_service import ChatService
from services.image_service import ImageService

# Create Blueprint
chat_bp = Blueprint('chat', __name__)

# Initialize services
chat_service = ChatService()
image_service = ImageService()

@chat_bp.route('/chat', methods=['POST'])
def chat():
    """
    Handle text chat messages
    
    Expected JSON:
    {
        "message": "User's message",
        "session_id": "unique_session_identifier"
    }
    """
    try:
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        
        response = chat_service.send_message(user_message, session_id)
        
        return jsonify({
            "response": response,
            "session_id": session_id
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_bp.route('/image/base64', methods=['POST'])
def analyze_image_base64():
    """
    Analyze image from base64 string
    
    Expected JSON:
    {
        "image": "base64_encoded_string",
        "prompt": "Optional analysis prompt"
    }
    """
    try:
        data = request.json
        base64_string = data.get('image', '')
        prompt = data.get('prompt', 'Describe this image in detail.')
        
        if not base64_string:
            return jsonify({"error": "Image data is required"}), 400
        
        result = image_service.analyze_image_from_base64(base64_string, prompt)
        
        return jsonify({"analysis": result})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_bp.route('/image/url', methods=['POST'])
def analyze_image_url():
    """
    Analyze image from URL
    
    Expected JSON:
    {
        "url": "image_url",
        "prompt": "Optional analysis prompt"
    }
    """
    try:
        data = request.json
        image_url = data.get('url', '')
        prompt = data.get('prompt', 'Describe this image in detail.')
        
        if not image_url:
            return jsonify({"error": "Image URL is required"}), 400
        
        result = image_service.analyze_image_from_url(image_url, prompt)
        
        return jsonify({"analysis": result})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_bp.route('/clear', methods=['POST'])
def clear_conversation():
    """
    Clear conversation history for a session
    
    Expected JSON:
    {
        "session_id": "unique_session_identifier"
    }
    """
    try:
        data = request.json
        session_id = data.get('session_id', 'default')
        
        chat_service.clear_history(session_id)
        
        return jsonify({
            "message": "Conversation cleared successfully",
            "session_id": session_id
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_bp.route('/history', methods=['POST'])
def get_history():
    """
    Get conversation history for a session
    
    Expected JSON:
    {
        "session_id": "unique_session_identifier"
    }
    """
    try:
        data = request.json
        session_id = data.get('session_id', 'default')
        
        history = chat_service.get_conversation_history(session_id)
        
        return jsonify({
            "history": history,
            "session_id": session_id
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500