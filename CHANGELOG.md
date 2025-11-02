# Changelog

All notable changes to TermLynx will be documented in this file.

## [1.0.0] - 2025-11-01

### 🎉 Initial Release

#### Core Features
- ✅ Full HTTP/HTTPS web fetching with `requests`
- ✅ Smart HTML parsing with `BeautifulSoup4`
- ✅ Rich terminal UI with colors and formatting using `rich`
- ✅ Link navigation by number
- ✅ Back/forward history navigation
- ✅ In-page text search
- ✅ Home page functionality
- ✅ Page reload capability

#### Components
- `browser/fetcher.py` - HTTP request handler with error handling
- `browser/parser.py` - HTML parser extracting text, links, headers, lists, tables
- `browser/renderer.py` - Terminal renderer with styled output
- `browser/navigator.py` - Navigation logic and link management
- `utils/history.py` - Browsing history manager with back/forward stack

#### Supported Commands
- `[number]` - Navigate to link by index
- `b` - Go back in history
- `f` - Go forward in history
- `r` - Reload current page
- `h` - Go to home page
- `/[query]` - Search in current page
- `?` - Show help
- `q` - Quit browser

#### Error Handling
- HTTP 404, 403, 500 errors
- Connection timeouts
- Invalid URLs
- Network errors
- Redirect handling

#### Documentation
- Comprehensive README.md
- Quick Start Guide (QUICKSTART.md)
- Example configuration file
- Demo script for testing

### Known Limitations
- No JavaScript execution
- No CSS rendering
- No image display
- No cookie management (yet)
- No bookmark system (planned for v2)
- Limited table rendering

## [Planned for v2.0.0]

### Features in Development
- 📚 Bookmark system with save/load
- 💾 Offline page caching
- 🎨 Multiple color themes (dark, light, monochrome)
- 🔐 HTTP/SOCKS proxy support
- 📥 Save pages as text/markdown
- 🍪 Basic cookie support
- 📊 Download progress indicator
- 🔍 Enhanced search with regex support
- 📑 Tab support (multiple pages)
- 🔄 Auto-refresh for live pages
- ⌨️ Vim-style keyboard shortcuts
- 📱 Mobile-friendly URL shortcuts

### Improvements Planned
- Better table rendering
- Form support (basic input fields)
- SSL certificate verification options
- Custom user agent per site
- Reading mode (enhanced text extraction)
- Export history to file
- Import bookmarks from browsers

## [Future Versions]

### v3.0.0 (Planned)
- Plugin system for extensions
- Custom CSS-to-text style mapping
- WebSocket support for real-time pages
- Archive.org integration
- RSS feed reader mode
- API mode for automation

### Community Requests
- [ ] Markdown export
- [ ] PDF export (text-based)
- [ ] Integration with `w3m` renderer
- [ ] Session save/restore
- [ ] Password manager integration
- [ ] DuckDuckGo bangs support

---

## Version History

| Version | Release Date | Highlights |
|---------|--------------|------------|
| 1.0.0   | 2025-11-01  | Initial release with core features |

---

**Note**: This is an open-source project. Contributions and feature requests are welcome!
