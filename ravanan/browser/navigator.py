"""
Navigator Module
Manages page navigation and link selection
"""
from typing import List, Dict, Optional
from ..utils.history import BrowsingHistory


class Navigator:
    """Handles navigation logic"""
    
    def __init__(self):
        self.current_url: Optional[str] = None
        self.current_links: List[Dict] = []
        self.history = BrowsingHistory()
    
    def set_current_page(self, url: str, links: List[Dict]):
        """
        Set the current page data
        
        Args:
            url: Current page URL
            links: List of links on the page
        """
        self.current_url = url
        self.current_links = links
        
        # Add to history
        self.history.add(url)
    
    def get_link_by_index(self, index: int) -> Optional[str]:
        """
        Get URL for a link by its index number
        
        Args:
            index: Link index (1-based)
            
        Returns:
            URL or None if index not found
        """
        for link in self.current_links:
            if link['index'] == index:
                return link['url']
        return None
    
    def go_back(self) -> Optional[str]:
        """
        Go back in history
        
        Returns:
            Previous URL or None
        """
        return self.history.go_back()
    
    def go_forward(self) -> Optional[str]:
        """
        Go forward in history
        
        Returns:
            Next URL or None
        """
        return self.history.go_forward()
    
    def can_go_back(self) -> bool:
        """Check if we can go back"""
        return self.history.can_go_back()
    
    def can_go_forward(self) -> bool:
        """Check if we can go forward"""
        return self.history.can_go_forward()
    
    def reload(self) -> Optional[str]:
        """
        Get current URL for reloading
        
        Returns:
            Current URL or None
        """
        return self.current_url
    
    def get_link_count(self) -> int:
        """Get number of links on current page"""
        return len(self.current_links)
