#!/bin/bash
# Ravanan Quick Launcher for Linux/Mac
# The 10-Headed Web Browser - Created by Krishna D

echo "========================================"
echo "   Ravanan - The 10-Headed Browser"
echo "   Created by: Krishna D"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "[1/3] Creating virtual environment..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        echo "Please ensure Python 3 is installed"
        exit 1
    fi
    echo "      Done!"
else
    echo "[1/3] Virtual environment found"
fi

echo ""
# Install dependencies if not already installed
if [ ! -d ".venv/lib/python*/site-packages/requests" ]; then
    echo "[2/3] Installing dependencies..."
    source .venv/bin/activate
    pip install -q -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
    echo "      Done!"
else
    echo "[2/3] Dependencies already installed"
fi

echo ""
echo "[3/3] Starting Ravanan..."
echo ""
echo "========================================"
echo ""

# Run the browser with any passed arguments
.venv/bin/python main.py "$@"
