from config import Config

class ConversationManager:
    """Manages conversation sessions and history"""
    
    def __init__(self):
        self.conversations = {}
    
    def get_conversation(self, session_id):
        """
        Get or create a conversation for a session
        
        Args:
            session_id: Unique identifier for the conversation session
            
        Returns:
            List of message dictionaries representing the conversation history
        """
        if session_id not in self.conversations:
            self.conversations[session_id] = [
                {"role": "system", "content": Config.SYSTEM_PROMPT}
            ]
        return self.conversations[session_id]
    
    def add_message(self, session_id, role, content):
        """
        Add a message to the conversation history
        
        Args:
            session_id: Unique identifier for the conversation session
            role: Message role ('user' or 'assistant')
            content: Message content
        """
        conversation = self.get_conversation(session_id)
        conversation.append({"role": role, "content": content})
    
    def clear_conversation(self, session_id):
        """
        Clear conversation history for a session
        
        Args:
            session_id: Unique identifier for the conversation session
        """
        if session_id in self.conversations:
            self.conversations[session_id] = [
                {"role": "system", "content": Config.SYSTEM_PROMPT}
            ]
    
    def delete_conversation(self, session_id):
        """
        Delete a conversation session entirely
        
        Args:
            session_id: Unique identifier for the conversation session
        """
        if session_id in self.conversations:
            del self.conversations[session_id]
    
    def get_all_sessions(self):
        """
        Get list of all active session IDs
        
        Returns:
            List of session IDs
        """
        return list(self.conversations.keys())