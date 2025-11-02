# 📦 Publishing Ravanan to GitHub and PyPI

Complete guide for publishing Ravanan as an open-source project on GitHub and making it installable via `pip install ravanan`.

**Created by: Krishna D**

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Publishing to GitHub](#publishing-to-github)
3. [Publishing to PyPI](#publishing-to-pypi)
4. [Post-Publication](#post-publication)
5. [Updating Versions](#updating-versions)
6. [Troubleshooting](#troubleshooting)

---

## ✅ Prerequisites

### Required Accounts

1. **GitHub Account**
   - Sign up at: https://github.com/signup
   - Free account is sufficient

2. **PyPI Account**
   - Sign up at: https://pypi.org/account/register/
   - Verify your email
   - Consider enabling 2FA for security

3. **TestPyPI Account** (Recommended for testing)
   - Sign up at: https://test.pypi.org/account/register/
   - Separate from main PyPI (for testing)

### Required Software

```bash
# Install Git
# Windows: Download from https://git-scm.com/
# Linux: sudo apt-get install git
# Mac: brew install git

# Install Python 3.8+
python --version  # Should be 3.8 or higher

# Install required tools
pip install build twine
```

---

## 🐙 Publishing to GitHub

### Step 1: Create a GitHub Repository

1. **Go to GitHub**: https://github.com/new

2. **Repository Settings**:
   - **Repository name**: `ravanan`
   - **Description**: "The 10-Headed Web Browser - A powerful text-based browser for the terminal"
   - **Visibility**: Public (for open source)
   - **Initialize**: Don't add README, .gitignore, or license (we already have them)

3. **Click "Create repository"**

### Step 2: Prepare Your Local Repository

```bash
# Navigate to your project directory
cd c:\Users\DHANUSH\Desktop\every-prjs\text-browser

# Initialize git (if not already done)
git init

# Create .gitignore file if it doesn't exist
```

Create `.gitignore` file:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
*.txt.bak
saved_pages/
config.ini
```

### Step 3: Initial Commit

```bash
# Add all files
git add .

# Check what will be committed
git status

# Commit
git commit -m "Initial commit: Ravanan v1.0.0 - The 10-Headed Web Browser"
```

### Step 4: Push to GitHub

```bash
# Add GitHub repository as remote
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/ravanan.git

# Verify remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

**If you have 2FA enabled** or encounter authentication issues:

```bash
# Use personal access token instead of password
# Create token at: https://github.com/settings/tokens
# Give it 'repo' permissions
# Use token as password when prompted
```

### Step 5: Configure GitHub Repository

1. **Go to your repository**: `https://github.com/YOUR_USERNAME/ravanan`

2. **Add Topics** (click gear icon next to "About"):
   - `python`
   - `terminal`
   - `browser`
   - `cli`
   - `text-browser`
   - `lynx`
   - `web-browser`
   - `tui`

3. **Add Description**: "The 10-Headed Web Browser - A powerful text-based browser for the terminal"

4. **Add Website**: Your project website or PyPI link (after publishing)

5. **Enable Issues** (for bug reports and feature requests)

6. **Enable Discussions** (optional, for community)

### Step 6: Create a Release

1. **Go to Releases**: `https://github.com/YOUR_USERNAME/ravanan/releases`

2. **Click "Create a new release"**

3. **Tag version**: `v1.0.0`

4. **Release title**: `Ravanan v1.0.0 - The 10-Headed Web Browser`

5. **Description**:
```markdown
## 🔱 Ravanan v1.0.0 - Initial Release

The 10-Headed Web Browser is now available!

### ✨ Features

- 🌐 Full HTML parsing and rendering
- ⚡ Fast HTTP/HTTPS fetching
- 🎨 Beautiful terminal UI with responsive banner
- 🔗 Numbered link navigation
- 📜 Full browsing history
- 🔍 In-page search
- ❌ Comprehensive error handling
- 💾 Save pages as text

### 📦 Installation

```bash
pip install ravanan
```

### 🚀 Quick Start

```bash
ravanan
```

See README for full documentation.
```

6. **Click "Publish release"**

---

## 🐍 Publishing to PyPI

### Step 1: Prepare Your Package

```bash
# Navigate to project directory
cd c:\Users\DHANUSH\Desktop\every-prjs\text-browser

# Ensure setup.py is configured correctly
# Update email in setup.py if needed

# Clean previous builds
rm -rf build dist *.egg-info  # Linux/Mac
# or
rd /s /q build dist  # Windows PowerShell (if they exist)
```

### Step 2: Build the Package

```bash
# Install build tools
pip install --upgrade build twine

# Build the package
python -m build

# This creates:
# - dist/ravanan-1.0.0-py3-none-any.whl
# - dist/ravanan-1.0.0.tar.gz
```

### Step 3: Test on TestPyPI (Recommended)

```bash
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# When prompted:
# Username: __token__
# Password: (your TestPyPI API token)
```

**Create TestPyPI API Token**:
1. Go to: https://test.pypi.org/manage/account/token/
2. Click "Add API token"
3. Token name: "Ravanan Upload"
4. Scope: "Entire account" or specific to "ravanan"
5. Copy the token (starts with `pypi-`)

**Test Installation from TestPyPI**:

```bash
# Create a test environment
python -m venv test_env
test_env\Scripts\activate  # Windows
# or
source test_env/bin/activate  # Linux/Mac

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ ravanan

# Test it
ravanan

# If it works, deactivate and remove test environment
deactivate
rm -rf test_env  # Linux/Mac
rd /s /q test_env  # Windows
```

### Step 4: Publish to PyPI

If TestPyPI works correctly:

```bash
# Upload to real PyPI
python -m twine upload dist/*

# When prompted:
# Username: __token__
# Password: (your PyPI API token)
```

**Create PyPI API Token**:
1. Go to: https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Token name: "Ravanan Upload"
4. Scope: "Entire account" (for first upload)
5. Copy the token

**Note**: After first upload, create a project-specific token:
1. Go to: https://pypi.org/manage/project/ravanan/settings/
2. Create a new token scoped to "ravanan" only

### Step 5: Verify Publication

```bash
# Visit your package page
https://pypi.org/project/ravanan/

# Test installation
pip install ravanan

# Run it
ravanan

# Uninstall
pip uninstall ravanan
```

---

## 🎉 Post-Publication

### Update README with Installation Instructions

Your README.md already has this, but verify:

```markdown
## Installation

```bash
pip install ravanan
```

After installation:

```bash
ravanan
```
```

### Create PyPI Badge

Add to README.md:

```markdown
[![PyPI](https://img.shields.io/pypi/v/ravanan.svg)](https://pypi.org/project/ravanan/)
[![Downloads](https://pepy.tech/badge/ravanan)](https://pepy.tech/project/ravanan)
```

### Announce Your Project

1. **Twitter/X**: Share your project
2. **Reddit**: 
   - r/Python
   - r/opensource
   - r/commandline
3. **Hacker News**: Show HN
4. **Dev.to**: Write a blog post
5. **LinkedIn**: Share with your network

### Update GitHub Repository

```bash
# After PyPI publication, update GitHub
git add .
git commit -m "Update documentation with PyPI links"
git push
```

---

## 🔄 Updating Versions

When you make changes and want to release a new version:

### Step 1: Update Version Number

Update in `setup.py`:

```python
setup(
    name="ravanan",
    version="1.0.1",  # Increment version
    ...
)
```

### Step 2: Update CHANGELOG.md

Add new version entry:

```markdown
## [1.0.1] - 2025-11-XX

### Added
- New feature description

### Fixed
- Bug fix description

### Changed
- Change description
```

### Step 3: Commit and Tag

```bash
# Commit changes
git add .
git commit -m "Release v1.0.1: description of changes"

# Create git tag
git tag -a v1.0.1 -m "Version 1.0.1"

# Push to GitHub
git push origin main
git push origin v1.0.1

# Create GitHub release (same as before)
```

### Step 4: Rebuild and Upload to PyPI

```bash
# Clean old builds
rm -rf build dist *.egg-info

# Build new version
python -m build

# Upload to PyPI
python -m twine upload dist/*
```

---

## 🛠️ Troubleshooting

### Common Issues

#### 1. "Package name already taken"

**Solution**: Choose a different name in `setup.py`

```python
setup(
    name="ravanan-browser",  # Try different name
    ...
)
```

#### 2. Authentication Failed

**Solution**: Use API tokens, not password
- Create token on PyPI
- Username: `__token__`
- Password: Your token (including `pypi-` prefix)

#### 3. Build Fails

**Solution**: Check setup.py for errors

```bash
# Validate setup.py
python setup.py check

# Test install locally
pip install -e .
```

#### 4. Import Errors After Installation

**Solution**: Check entry points in setup.py

```python
entry_points={
    "console_scripts": [
        "ravanan=main:main",  # Ensure this matches your main function
    ],
},
```

Verify `main.py` has a `main()` function:

```python
def main():
    """Main entry point"""
    # Your code here
    pass

if __name__ == "__main__":
    main()
```

#### 5. Missing Files in Package

**Solution**: Check MANIFEST.in

```bash
# Verify what's included
python setup.py sdist
tar -tzf dist/ravanan-1.0.0.tar.gz
```

#### 6. Git Push Rejected

**Solution**: Pull first, then push

```bash
git pull origin main
git push origin main
```

---

## 📝 Checklist

### Before Publishing

- [ ] All tests pass (`python test.py`)
- [ ] README.md is complete and accurate
- [ ] LICENSE file has correct copyright
- [ ] setup.py has correct metadata
- [ ] CHANGELOG.md is updated
- [ ] Version number is correct
- [ ] .gitignore is configured
- [ ] MANIFEST.in includes all needed files

### GitHub Publication

- [ ] Repository created on GitHub
- [ ] Code pushed to GitHub
- [ ] Topics added to repository
- [ ] Release created with tag
- [ ] Issues enabled
- [ ] Description and website set

### PyPI Publication

- [ ] PyPI account created
- [ ] API token created
- [ ] Package built successfully
- [ ] Tested on TestPyPI
- [ ] Published to PyPI
- [ ] Installation tested
- [ ] Package page verified

---

## 🎯 How Users Will Install

After successful publication:

```bash
# Users can install with:
pip install ravanan

# They can run with:
ravanan

# Or:
ravanan wikipedia.org

# Upgrade to latest:
pip install --upgrade ravanan

# Uninstall:
pip uninstall ravanan
```

---

## 🚀 Quick Command Reference

```bash
# GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ravanan.git
git push -u origin main
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0

# PyPI
pip install --upgrade build twine
python -m build
python -m twine upload --repository testpypi dist/*
python -m twine upload dist/*

# Testing
pip install ravanan
ravanan
pip uninstall ravanan
```

---

## 💡 Tips

1. **Use API Tokens**: More secure than passwords
2. **Test on TestPyPI first**: Catch issues before production
3. **Semantic Versioning**: Use MAJOR.MINOR.PATCH (1.0.0)
4. **Keep CHANGELOG**: Document all changes
5. **Write Good Commit Messages**: Clear and descriptive
6. **Tag Releases**: Makes version management easier
7. **Update Documentation**: Keep README current

---

## 📚 Additional Resources

- **PyPI Documentation**: https://packaging.python.org/
- **Git Documentation**: https://git-scm.com/doc
- **GitHub Guides**: https://guides.github.com/
- **Semantic Versioning**: https://semver.org/
- **Python Packaging**: https://packaging.python.org/tutorials/packaging-projects/

---

**Congratulations! Your project is now open source and available worldwide! 🎉**

*Happy Publishing! - Krishna D*
