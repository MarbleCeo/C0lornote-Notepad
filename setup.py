#!/usr/bin/env python3
"""
Setup script for C0lorNote application.
"""

import os
import sys
import shutil
import subprocess
import glob
from setuptools import setup, find_packages

# Basic app info
APP_NAME = "C0lorNote"
MAIN_SCRIPT = "modern_colornote.py"

# Output directories
EXE_DIR = "exe"
APK_DIR = "apk"

def build_windows_exe():
    """Build Windows executable and copy to exe folder"""
    print(f"Building {APP_NAME} for Windows...")
    
    # Make sure the exe directory exists
    os.makedirs(EXE_DIR, exist_ok=True)
    
    try:
        # Use PyInstaller to create the executable
        subprocess.run([
            "pyinstaller",
            "--name=" + APP_NAME,
            "--onefile",
            "--windowed",
            "--icon=assets/icon.ico" if os.path.exists("assets/icon.ico") else "",
            MAIN_SCRIPT
        ], check=True)
        
        # Find the executable
        exe_path = os.path.join("dist", f"{APP_NAME}.exe")
        if os.path.exists(exe_path):
            # Copy to exe folder
            dst_path = os.path.join(EXE_DIR, f"{APP_NAME}.exe")
            shutil.copy2(exe_path, dst_path)
            print(f"✓ Executable copied to {dst_path}")
            return True
        else:
            print(f"✗ Error: Executable not found at {exe_path}")
            return False
    except Exception as e:
        print(f"✗ Error building Windows executable: {str(e)}")
        return False

def build_android_apk():
    """Build Android APK and copy to apk folder"""
    print(f"Building {APP_NAME} for Android...")
    
    # Make sure the apk directory exists
    os.makedirs(APK_DIR, exist_ok=True)
    
    try:
        # Check for buildozer
        try:
            subprocess.run(["buildozer", "--version"], stdout=subprocess.PIPE, check=True)
        except (FileNotFoundError, subprocess.SubprocessError):
            print("Installing buildozer...")
            subprocess.run([sys.executable, "-m", "pip", "install", "buildozer"], check=True)
        
        # Initialize buildozer if needed
        if not os.path.exists("buildozer.spec"):
            subprocess.run(["buildozer", "init"], check=True)
            
            # Update buildozer.spec with our app info
            with open("buildozer.spec", "r") as f:
                spec = f.read()
            
            spec = spec.replace("title = My Application", f"title = {APP_NAME}")
            spec = spec.replace("package.name = myapp", "package.name = colornote")
            spec = spec.replace("source.include_exts = py,png,jpg,kv,atlas", 
                              "source.include_exts = py,png,jpg,kv,atlas,json")
            spec = spec.replace("requirements = python3", 
                              "requirements = python3,pyqt6,pillow,pyyaml")
            
            with open("buildozer.spec", "w") as f:
                f.write(spec)
        
        # Build the APK
        subprocess.run(["buildozer", "android", "debug"], check=True)
        
        # Find and copy the APK
        apk_files = glob.glob(os.path.join("bin", "*.apk"))
        if apk_files:
            latest_apk = max(apk_files, key=os.path.getctime)
            dst_path = os.path.join(APK_DIR, os.path.basename(latest_apk))
            shutil.copy2(latest_apk, dst_path)
            print(f"✓ APK copied to {dst_path}")
            return True
        else:
            print("✗ Error: No APK file found in bin directory")
            return False
    except Exception as e:
        print(f"✗ Error building Android APK: {str(e)}")
        return False

# Handle command line arguments
if len(sys.argv) > 1:
    if sys.argv[1] == "--windows":
        build_windows_exe()
        sys.exit(0)
    elif sys.argv[1] == "--android":
        build_android_apk()
        sys.exit(0)
    elif sys.argv[1] == "--all":
        build_windows_exe()
        build_android_apk()
        sys.exit(0)

# Regular setup.py functionality continues below
# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="c0lornote",
    version="1.0.0",
    description="A modern note-taking application inspired by macOS Notes and Google Keep",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/c0lornote",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Personal Information Management",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: POSIX :: Linux",
        "Environment :: X11 Applications :: Gnome",
    ],
    keywords="notes, note-taking, markdown, rich text, tkinter",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "pyqt6>=6.8.0",
        "pillow>=11.0.0",
        "pyyaml>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "pyinstaller>=6.5.0",
            "buildozer>=1.5.0",
        ],
    },
    package_data={
        "c0lornote": [
            "assets/*.png",
            "assets/*.ico",
            "assets/*.svg",
        ],
    },
    data_files=[
        ("share/applications", ["debian/c0lornote.desktop"]),
        ("share/pixmaps", ["assets/c0lornote.png"]),
        ("share/icons/hicolor/48x48/apps", ["assets/c0lornote.png"]),
        ("share/icons/hicolor/256x256/apps", ["assets/c0lornote.png"]),
    ],
    entry_points={
        "console_scripts": [
            "c0lornote=c0lornote.main:main",
        ],
        "gui_scripts": [
            "c0lornote-gui=c0lornote.main:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/c0lornote/issues",
        "Source": "https://github.com/yourusername/c0lornote",
    },
)

