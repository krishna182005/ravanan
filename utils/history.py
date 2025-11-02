"""
History Module
Manages browsing history with back/forward navigation
"""
from typing import List, Optional


class BrowsingHistory:
    """Manages browser history stack"""
    
    def __init__(self, max_history: int = 100):
        self.max_history = max_history
        self.history: List[str] = []
        self.current_index: int = -1
    
    def add(self, url: str):
        """
        Add a URL to history
        
        Args:
            url: The URL to add
        """
        # If we're not at the end of history, remove everything after current position
        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]
        
        # Add new URL
        self.history.append(url)
        self.current_index = len(self.history) - 1
        
        # Limit history size
        if len(self.history) > self.max_history:
            self.history.pop(0)
            self.current_index -= 1
    
    def can_go_back(self) -> bool:
        """Check if we can go back in history"""
        return self.current_index > 0
    
    def can_go_forward(self) -> bool:
        """Check if we can go forward in history"""
        return self.current_index < len(self.history) - 1
    
    def go_back(self) -> Optional[str]:
        """
        Go back in history
        
        Returns:
            Previous URL or None if can't go back
        """
        if self.can_go_back():
            self.current_index -= 1
            return self.history[self.current_index]
        return None
    
    def go_forward(self) -> Optional[str]:
        """
        Go forward in history
        
        Returns:
            Next URL or None if can't go forward
        """
        if self.can_go_forward():
            self.current_index += 1
            return self.history[self.current_index]
        return None
    
    def get_current(self) -> Optional[str]:
        """Get current URL"""
        if 0 <= self.current_index < len(self.history):
            return self.history[self.current_index]
        return None
    
    def clear(self):
        """Clear all history"""
        self.history = []
        self.current_index = -1
    
    def get_history_list(self) -> List[str]:
        """Get the full history list"""
        return self.history.copy()
