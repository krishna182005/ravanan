@echo off
REM Ravanan Quick Launcher for Windows
REM The 10-Headed Web Browser - Created by Krishna D

echo ========================================
echo    Ravanan - The 10-Headed Browser
echo    Created by: Krishna D
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv\" (
    echo [1/3] Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        echo Please ensure Python is installed and in your PATH
        pause
        exit /b 1
    )
    echo       Done!
) else (
    echo [1/3] Virtual environment found
)

echo.
REM Activate virtual environment and install dependencies
if not exist ".venv\Scripts\requests" (
    echo [2/3] Installing dependencies...
    call .venv\Scripts\activate.bat
    pip install -q -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    echo       Done!
) else (
    echo [2/3] Dependencies already installed
)

echo.
echo [3/3] Starting Ravanan...
echo.
echo ========================================
echo.

REM Run the browser with any passed arguments
.venv\Scripts\python.exe main.py %*
