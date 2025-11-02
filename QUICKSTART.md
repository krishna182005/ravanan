# TermLynx Quick Start Guide

## Installation

1. **Navigate to the project directory:**
   ```bash
   cd text-browser
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   
   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Browser

### Basic Usage

```bash
# Start with default page (example.com)
python main.py

# Open a specific website
python main.py https://wikipedia.org

# Open without https:// (will be added automatically)
python main.py wikipedia.org
```

### Advanced Options

```bash
# Set a custom home page
python main.py --home https://news.ycombinator.com

# Check version
python main.py --version

# Show help
python main.py --help
```

## Quick Command Reference

Once the browser is running, use these commands:

### Navigate by Link Number
```
> 1          # Opens link #1
> 5          # Opens link #5
```

### Navigate by URL
```
> wikipedia.org
> https://github.com
```

### Browser Controls
```
> b          # Go back
> f          # Go forward
> r          # Reload current page
> h          # Go to home page
> q          # Quit browser
```

### Search
```
> /python    # Search for "python" in current page
> /tutorial  # Search for "tutorial"
```

### Help
```
> ?          # Show help menu
```

## Example Browsing Session

```bash
$ python main.py

# Browser opens with example.com

> wikipedia.org
# Wikipedia loads with numbered links

> 3
# Opens link #3 from Wikipedia

> /science
# Searches for "science" in the current page

> b
# Goes back to Wikipedia

> h
# Returns to home page (example.com)

> q
# Quits browser
```

## Recommended Sites to Try

### News & Information
- `news.ycombinator.com` - Hacker News (works great in text mode)
- `lobste.rs` - Lobsters tech community
- `text.npr.org` - NPR text-only site

### Reference & Learning
- `wikipedia.org` - Wikipedia
- `python.org` - Python documentation
- `stackoverflow.com` - Stack Overflow

### Fun & Lightweight
- `example.com` - Simple test page
- `info.cern.ch` - First website ever made
- `motherfuckingwebsite.com` - Minimalist web manifesto

## Troubleshooting

### Import Errors
If you see `ModuleNotFoundError`, make sure you've installed dependencies:
```bash
pip install -r requirements.txt
```

### Connection Errors
- Check your internet connection
- Some sites may block automated requests
- Try sites known to work: `example.com`, `wikipedia.org`

### Display Issues
- Ensure your terminal supports Unicode
- Try resizing your terminal window
- Windows users: Use Windows Terminal for best results

## Tips & Tricks

1. **Bookmark Your Favorites**: Keep a text file with your favorite URLs
   ```
   wikipedia.org
   news.ycombinator.com
   stackoverflow.com
   ```

2. **Use Short URLs**: The browser auto-adds `https://`
   ```
   > reddit.com    ✓
   > github.com    ✓
   ```

3. **Search Before Clicking**: Use `/keyword` to find specific links
   ```
   > /python       # Find all mentions of "python"
   > 2             # Then click relevant link
   ```

4. **Quick Navigation**: Use single-letter commands
   ```
   b  # Back
   f  # Forward
   h  # Home
   r  # Reload
   ```

## Advanced Features (Coming Soon)

- 📚 Bookmarks system
- 💾 Offline page caching
- 🎨 Custom color themes
- 🔐 Proxy support
- 📥 Download pages as text files

## Getting Help

- Type `?` in the browser for help
- Check `README.md` for full documentation
- Run `python main.py --help` for command-line options

---

**Happy Browsing! 🌐**
