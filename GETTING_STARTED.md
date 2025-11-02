# 🎯 GETTING STARTED WITH TERMLYNX

## 🚀 Super Quick Start (30 seconds)

### Windows
```bash
# Double-click or run:
run.bat
```

### Linux/Mac
```bash
# Make executable and run:
chmod +x run.sh
./run.sh
```

That's it! The script handles everything automatically.

---

## 📖 Manual Installation

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Browser
```bash
python main.py
```

---

## 🎮 First Steps

### When the browser starts:

1. **You'll see** the TermLynx banner and example.com
2. **Try typing** a website:
   ```
   > wikipedia.org
   ```

3. **Click a link** by its number:
   ```
   > 3
   ```

4. **Go back**:
   ```
   > b
   ```

5. **Search** in the page:
   ```
   > /python
   ```

6. **Get help**:
   ```
   > ?
   ```

7. **Quit**:
   ```
   > q
   ```

---

## 💡 Quick Tips

### Navigate Like a Pro
```
> wikipedia.org          # Visit Wikipedia
> 5                      # Click link #5  
> /artificial            # Search for "artificial"
> 2                      # Click search result #2
> b                      # Go back
> f                      # Go forward
> h                      # Return home
```

### Try These Websites
- `example.com` - Simple test site
- `wikipedia.org` - Works great!
- `news.ycombinator.com` - Hacker News
- `info.cern.ch` - First website ever
- `text.npr.org` - NPR text version

---

## 🛠️ Command Reference

| What You Want | Command | Example |
|---------------|---------|---------|
| Visit a website | Type URL | `wikipedia.org` |
| Click a link | Type number | `5` |
| Go back | `b` | `b` |
| Go forward | `f` | `f` |
| Reload page | `r` | `r` |
| Go home | `h` | `h` |
| Search in page | `/query` | `/python` |
| Show help | `?` | `?` |
| Quit | `q` | `q` |

---

## ❓ Common Questions

### Q: How do I click a link?
A: Just type the number in square brackets. If you see `[5]`, type `5` and press Enter.

### Q: The page is too long!
A: Your terminal scrolls naturally. On Windows Terminal, use Scroll Lock or scroll with your mouse.

### Q: Can I save bookmarks?
A: Not in v1.0, but it's planned for v2.0! For now, keep a text file with your favorites.

### Q: It says "Error 404" or connection error
A: The website might be down, blocked, or doesn't exist. Try a different URL.

### Q: How do I exit?
A: Type `q` and press Enter.

### Q: Can I browse JavaScript-heavy sites?
A: Not yet! TermLynx shows only HTML content. Sites like Gmail won't work, but Wikipedia, blogs, and news sites work great.

---

## 🎨 Example Session

```
$ python main.py

[TermLynx Banner appears]

> wikipedia.org
[Wikipedia loads with links [1], [2], [3]...]

> /artificial intelligence
[Search results shown]

> 2
[Opens link #2 about AI]

> /history
[Finds "history" mentions on page]

> b
[Returns to Wikipedia main page]

> news.ycombinator.com
[Hacker News loads]

> 1
[Opens top story]

> h
[Returns to home page]

> q
[Exits browser]

Thanks for using TermLynx! Goodbye.
```

---

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"
**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### "Python is not recognized..."
**Solution:** Install Python from python.org or ensure it's in your PATH

### Terminal looks weird / no colors
**Solution:** 
- Windows: Use Windows Terminal (recommended)
- Linux/Mac: Any modern terminal works
- Try: `python -m rich` to test Rich library

### Pages won't load
**Solution:**
- Check internet connection
- Try a simple site: `example.com`
- Some sites block automated requests

### Can't see full page
**Solution:**
- Resize your terminal window
- Use terminal scrolling (mouse wheel, Page Up/Down)
- Most content is at the top

---

## 📚 Learning Resources

### Included Files
- `README.md` - Full documentation
- `QUICKSTART.md` - This file
- `PROJECT_SUMMARY.md` - What was built
- `CHANGELOG.md` - Version history

### Running Tests
```bash
python test.py
```

### Running Demo
```bash
python demo.py
```

---

## 🎯 Next Steps

### For Users
1. Browse your favorite sites
2. Try different websites
3. Learn the keyboard shortcuts
4. Provide feedback!

### For Developers
1. Read `README.md` for architecture
2. Check out the code in `browser/`
3. Run tests with `python test.py`
4. Add your own features!

---

## 🆘 Need Help?

1. **Type `?` in the browser** for quick help
2. **Read README.md** for detailed docs
3. **Run the demo** (`python demo.py`) to see examples
4. **Check the tests** (`python test.py`) to see it work

---

## 🌟 Enjoy!

You're all set! Happy browsing in the terminal! 🚀

**Remember:**
- Type website URLs to visit them
- Type numbers to click links
- Type `b` to go back
- Type `q` to quit
- Type `?` for help anytime

**Have fun exploring the web, text-style!** 🌐✨

---

*TermLynx v1.0.0*
*Made with ❤️ for terminal enthusiasts*
