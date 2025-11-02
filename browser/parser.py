"""
HTML Parser Module
Extracts text and links from HTML content
"""
from bs4 import BeautifulSoup, Comment
from typing import List, Dict, Tuple
from urllib.parse import urljoin, urlparse


class HTMLParser:
    """Parses HTML and extracts readable content"""
    
    def __init__(self):
        self.soup = None
        self.base_url = None
        self.links = []
        self.text_content = []
    
    def parse(self, html_content: str, base_url: str) -> Tuple[List[Dict], List[str]]:
        """
        Parse HTML content and extract text and links
        
        Args:
            html_content: Raw HTML string
            base_url: Base URL for resolving relative links
            
        Returns:
            Tuple of (links_list, text_content_lines)
        """
        self.base_url = base_url
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.links = []
        self.text_content = []
        
        # Remove script and style elements
        for script in self.soup(['script', 'style', 'noscript']):
            script.decompose()
        
        # Remove comments
        for comment in self.soup.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()
        
        # Parse the body content
        body = self.soup.find('body')
        if body:
            self._parse_element(body)
        else:
            # If no body, parse the entire document
            self._parse_element(self.soup)
        
        return self.links, self.text_content
    
    def _parse_element(self, element, depth: int = 0):
        """Recursively parse HTML elements"""
        for child in element.children:
            if isinstance(child, str):
                # Text node
                text = child.strip()
                if text:
                    self.text_content.append(('text', text, depth))
            elif child.name:
                # Element node
                tag = child.name.lower()
                
                # Handle headings
                if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    text = child.get_text(strip=True)
                    if text:
                        level = int(tag[1])
                        self.text_content.append(('heading', text, level))
                
                # Handle links
                elif tag == 'a':
                    href = child.get('href', '')
                    text = child.get_text(strip=True)
                    
                    if href and href.strip():
                        # Skip anchor-only links and javascript
                        if not href.startswith('#') and not href.startswith('javascript:'):
                            # Resolve relative URLs
                            absolute_url = urljoin(self.base_url, href)
                            
                            # Only include http/https links
                            if urlparse(absolute_url).scheme in ['http', 'https']:
                                link_index = len(self.links) + 1
                                self.links.append({
                                    'index': link_index,
                                    'url': absolute_url,
                                    'text': text or absolute_url
                                })
                                
                                if text:
                                    self.text_content.append(('link', text, link_index))
                
                # Handle paragraphs
                elif tag == 'p':
                    text = child.get_text(strip=True)
                    if text:
                        self.text_content.append(('paragraph', text, depth))
                    self.text_content.append(('newline', '', 0))
                
                # Handle line breaks
                elif tag == 'br':
                    self.text_content.append(('newline', '', 0))
                
                # Handle lists
                elif tag in ['ul', 'ol']:
                    self._parse_list(child, tag, depth)
                
                # Handle list items
                elif tag == 'li':
                    text = child.get_text(strip=True)
                    if text:
                        self.text_content.append(('list_item', text, depth))
                
                # Handle blockquotes
                elif tag == 'blockquote':
                    text = child.get_text(strip=True)
                    if text:
                        self.text_content.append(('blockquote', text, depth))
                
                # Handle preformatted text
                elif tag == 'pre':
                    text = child.get_text()  # Don't strip for pre
                    if text:
                        self.text_content.append(('pre', text, depth))
                
                # Handle divs and other containers
                elif tag in ['div', 'section', 'article', 'main', 'header', 'footer', 'nav']:
                    self._parse_element(child, depth)
                
                # Handle tables (simplified)
                elif tag == 'table':
                    self._parse_table(child, depth)
                
                # Recursively parse other elements
                else:
                    self._parse_element(child, depth)
    
    def _parse_list(self, element, list_type: str, depth: int):
        """Parse ordered or unordered lists"""
        self.text_content.append(('newline', '', 0))
        for item in element.find_all('li', recursive=False):
            text = item.get_text(strip=True)
            if text:
                prefix = '  • ' if list_type == 'ul' else '  - '
                self.text_content.append(('list_item', f"{prefix}{text}", depth))
        self.text_content.append(('newline', '', 0))
    
    def _parse_table(self, element, depth: int):
        """Parse tables (simplified rendering)"""
        self.text_content.append(('newline', '', 0))
        self.text_content.append(('text', '--- TABLE ---', depth))
        
        for row in element.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            if cells:
                row_text = ' | '.join(cell.get_text(strip=True) for cell in cells)
                self.text_content.append(('text', row_text, depth))
        
        self.text_content.append(('text', '--- END TABLE ---', depth))
        self.text_content.append(('newline', '', 0))
    
    def get_page_title(self) -> str:
        """Extract page title"""
        if self.soup:
            title_tag = self.soup.find('title')
            if title_tag:
                return title_tag.get_text(strip=True)
        return "Untitled Page"
