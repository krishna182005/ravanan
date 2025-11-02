# Contributing to Ravanan 🔱

First off, thank you for considering contributing to Ravanan! It's people like you that make Ravanan such a great tool.

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [What We're Looking For](#what-were-looking-for)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## 📜 Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. By participating, you are expected to uphold this standard. Please report unacceptable behavior to the project maintainer.

## 🎯 What We're Looking For

Ravanan is an open source project and we love to receive contributions from our community! There are many ways to contribute:

- **Bug reports**: Report issues you encounter
- **Bug fixes**: Submit fixes for known issues
- **Feature requests**: Suggest new features or enhancements
- **Documentation**: Improve documentation, add examples
- **Code refactoring**: Improve code quality and performance
- **Tests**: Add or improve test coverage
- **Translations**: Help translate to other languages (future)

## 🚀 How to Contribute

### For First-Time Contributors

1. **Fork the repository** on GitHub
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ravanan.git
   cd ravanan
   ```
3. **Create a branch** for your contribution:
   ```bash
   git checkout -b feature/my-new-feature
   ```
   or
   ```bash
   git checkout -b fix/bug-description
   ```

4. **Make your changes** (see [Development Setup](#development-setup))

5. **Test your changes** thoroughly:
   ```bash
   python test.py
   ```

6. **Commit your changes** (see [Commit Messages](#commit-messages)):
   ```bash
   git add .
   git commit -m "Add feature: description of feature"
   ```

7. **Push to your fork**:
   ```bash
   git push origin feature/my-new-feature
   ```

8. **Create a Pull Request** on GitHub

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ravanan.git
cd ravanan

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Run the browser
ravanan

# Run tests
python test.py
```

## 📝 Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use meaningful variable and function names

### Code Structure

```python
"""
Module docstring explaining the purpose of the module

Created by: Your Name
"""
import standard_library
import third_party_library
from local_module import something


class MyClass:
    """Class docstring explaining the class"""
    
    def __init__(self):
        """Initialize the class"""
        pass
    
    def my_method(self, param: str) -> str:
        """
        Method docstring
        
        Args:
            param: Description of parameter
            
        Returns:
            Description of return value
        """
        return param


def my_function(arg1: str, arg2: int = 0) -> bool:
    """
    Function docstring
    
    Args:
        arg1: Description
        arg2: Description with default value
        
    Returns:
        Description of return value
    """
    return True
```

### Documentation

- Add docstrings to all modules, classes, and functions
- Use type hints for function parameters and return values
- Update README.md if adding new features
- Add comments for complex logic

### Testing

- Write tests for new features
- Ensure all existing tests pass
- Test on multiple platforms if possible (Windows, Linux, Mac)
- Test edge cases and error conditions

## 💬 Commit Messages

### Format

```
Type: Brief description (50 chars or less)

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. Explain the problem that this commit is solving.

- Bullet points are okay
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
```

### Types

- **Feature**: A new feature
- **Fix**: A bug fix
- **Docs**: Documentation changes
- **Style**: Code style changes (formatting, missing semicolons, etc.)
- **Refactor**: Code refactoring
- **Test**: Adding or updating tests
- **Chore**: Maintenance tasks

### Examples

```
Feature: Add bookmark system for saving favorite pages

Implement a bookmark manager that allows users to save, list,
and visit bookmarked pages. Bookmarks are stored in a JSON file
in the user's home directory.

- Add Bookmark class in utils/bookmarks.py
- Add commands: bookmark, bookmarks, goto-bookmark
- Update README with bookmark documentation
```

```
Fix: Handle timeout errors gracefully in fetcher

Previously, timeout errors would crash the browser. Now they
display a user-friendly error message and allow continued browsing.
```

## 🔄 Pull Request Process

### Before Submitting

1. ✅ Ensure your code follows the coding standards
2. ✅ Run all tests and ensure they pass
3. ✅ Update documentation if needed
4. ✅ Add yourself to CONTRIBUTORS.md (if it exists)
5. ✅ Ensure your branch is up to date with main:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
Describe the tests you ran to verify your changes.

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

### Review Process

1. A maintainer will review your PR
2. They may request changes or ask questions
3. Make requested changes and push to your branch
4. Once approved, your PR will be merged

## 🐛 Reporting Bugs

### Before Submitting a Bug Report

- **Check existing issues** to see if it's already reported
- **Try the latest version** to see if it's already fixed
- **Collect information** about the bug

### How to Submit a Bug Report

Create an issue on GitHub with the following information:

**Title**: Brief, descriptive title

**Description**:
- What did you expect to happen?
- What actually happened?
- Steps to reproduce
- Screenshots (if applicable)

**Environment**:
- Ravanan version (`ravanan --version` or check setup.py)
- Python version (`python --version`)
- Operating system (Windows, Linux, Mac)
- Terminal emulator

**Example**:

```markdown
## Bug: Browser crashes when visiting certain URLs

### Expected Behavior
Browser should load the page or show an error message

### Actual Behavior
Browser crashes with a traceback

### Steps to Reproduce
1. Run `ravanan`
2. Enter URL: `example-broken-site.com`
3. Browser crashes

### Environment
- Ravanan: 1.0.0
- Python: 3.9.5
- OS: Windows 10
- Terminal: Windows Terminal

### Error Message
```
[Paste error message here]
```
```

## 💡 Suggesting Enhancements

### Before Submitting an Enhancement

- **Check if it already exists** in newer versions
- **Check existing feature requests** on GitHub Issues
- **Consider if it fits** the project's scope and philosophy

### How to Submit an Enhancement

Create an issue on GitHub with:

**Title**: Clear, descriptive title

**Description**:
- What problem does this solve?
- How should it work?
- Why is this useful?
- Examples of how it would be used

**Example**:

```markdown
## Feature Request: Add bookmark system

### Problem
Currently, there's no way to save favorite pages for quick access

### Proposed Solution
Add a bookmark system with these commands:
- `bookmark` - Save current page
- `bookmarks` - List all bookmarks
- `b [number]` - Go to bookmark

### Use Cases
- Save frequently visited sites
- Quick access to documentation pages
- Build a personal wiki

### Implementation Ideas
- Store bookmarks in JSON file
- Include URL, title, and date added
- Organize by categories (optional)
```

## 🏅 Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file (if exists)
- GitHub contributors page
- Release notes for significant contributions

## 📞 Getting Help

- **Documentation**: Read the README.md and other docs
- **Issues**: Search existing GitHub issues
- **Discussions**: Start a discussion on GitHub
- **Email**: Contact the maintainer (Krishna D)

## 🙏 Thank You!

Your contributions make Ravanan better for everyone. We appreciate your time and effort!

---

*Happy Contributing! 🚀*

*The Ravanan Team*
