from models.groq_client import GroqClient
from services.conversation_manager import ConversationManager

class ChatService:
    """Handles chat message processing and responses"""
    
    def __init__(self):
        self.groq_client = GroqClient()
        self.conversation_manager = ConversationManager()
    
    def send_message(self, user_input, session_id):
        """
        Process a text message and generate a response
        
        Args:
            user_input: User's message text
            session_id: Unique identifier for the conversation session
            
        Returns:
            Assistant's response string
        """
        try:
            # Get conversation history
            conversation = self.conversation_manager.get_conversation(session_id)
            
            # Add user message to history
            self.conversation_manager.add_message(session_id, "user", user_input)
            
            # Get response from Groq
            reply = self.groq_client.create_chat_completion(
                messages=self.conversation_manager.get_conversation(session_id)
            )
            
            # Add assistant response to history
            self.conversation_manager.add_message(session_id, "assistant", reply)
            
            return reply
            
        except Exception as e:
            return f"System Error: {str(e)}"
    
    def clear_history(self, session_id):
        """
        Clear conversation history for a session
        
        Args:
            session_id: Unique identifier for the conversation session
        """
        self.conversation_manager.clear_conversation(session_id)
    
    def get_conversation_history(self, session_id):
        """
        Get the conversation history for a session
        
        Args:
            session_id: Unique identifier for the conversation session
            
        Returns:
            List of message dictionaries
        """
        return self.conversation_manager.get_conversation(session_id)