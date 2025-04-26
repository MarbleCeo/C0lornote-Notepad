#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Windows EXE Builder for C0lorNote

This script builds a standalone Windows executable with proper Apple-like theming
and places it in the exe folder.
"""

import os
import sys
import shutil
import subprocess

# Make sure the exe directory exists
exe_dir = "exe"
os.makedirs(exe_dir, exist_ok=True)

print("Building C0lorNote Windows Executable...")

try:
    # Install PyInstaller if needed
    try:
        import PyInstaller
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)

    # Create icon directory if needed
    icon_dir = os.path.join("assets", "icon")
    os.makedirs(icon_dir, exist_ok=True)
    
    # Create a simple icon if not exists
    icon_path = os.path.join(icon_dir, "icon.ico")
    if not os.path.exists(icon_path):
        print("Creating application icon...")
        try:
            from PIL import Image, ImageDraw
            
            # Create a basic icon - could be improved
            img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Draw a colorful square (representing a note)
            draw.rectangle((48, 48, 208, 208), fill=(10, 132, 255))  # Apple blue
            
            # Save in ICO format
            img.save(icon_path, format='ICO')
            print(f"✓ Created icon at {icon_path}")
        except ImportError:
            print("⚠ Pillow not installed, skipping icon creation")
            # Continue without an icon
    
    # Build the executable with better settings
    subprocess.run([
        "pyinstaller",
        "--name=C0lorNote",
        "--onefile",
        "--windowed",
        "--clean",
        "--noupx",
        "--noconfirm",
        f"--icon={icon_path}" if os.path.exists(icon_path) else "",
        "--add-data=assets;assets",
        "modern_colornote.py"
    ], check=True)
    
    # Check if the executable was created
    exe_path = os.path.join("dist", "C0lorNote.exe")
    if os.path.exists(exe_path):
        # Copy to exe folder
        dst_path = os.path.join(exe_dir, "C0lorNote.exe")
        shutil.copy2(exe_path, dst_path)
        print(f"✓ Executable built and copied to {dst_path}")
        
        # Create a simple launcher script
        launcher = """@echo off
echo Starting C0lorNote...
start "" "%~dp0C0lorNote.exe"
"""
        with open(os.path.join(exe_dir, "Launch C0lorNote.bat"), "w") as f:
            f.write(launcher)
        print(f"✓ Created launcher batch file")
        
    else:
        print(f"✗ Failed to build C0lorNote.exe - file not found at {exe_path}")
        
except Exception as e:
    print(f"✗ Error: {str(e)}")
    sys.exit(1)

print("Windows executable build process completed.") 