#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C0lorNote Cross-Platform Build Script

This script helps build C0lorNote for different platforms:
- Windows: using PyInstaller
- macOS: using PyInstaller with app bundle support
- Linux: using PyInstaller
- Android: preparation for Buildozer
"""

import os
import sys
import shutil
import subprocess
import platform
import argparse
import glob

# Basic project details
APP_NAME = "C0lorNote"
APP_VERSION = "1.0.0"
MAIN_SCRIPT = "modern_colornote.py"
ICON_PATH = os.path.join("assets", "icon")

# Output directories
EXE_DIR = "exe"
APK_DIR = "apk"

def clean_build_dirs():
    """Clean build directories"""
    print("Cleaning build directories...")
    dirs_to_clean = ["dist", "build", "__pycache__"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
    
    # Also clean .spec files
    for spec_file in [f for f in os.listdir(".") if f.endswith(".spec")]:
        os.remove(spec_file)
    
    print("✓ Build directories cleaned")

def setup_windows():
    """Build for Windows"""
    print("Building for Windows...")
    
    # Create resources directory in case it doesn't exist
    os.makedirs("assets", exist_ok=True)
    
    # Create the exe output directory if it doesn't exist
    os.makedirs(EXE_DIR, exist_ok=True)
    
    # Run PyInstaller
    subprocess.run([
        "pyinstaller",
        "--name={}".format(APP_NAME),
        "--windowed",
        "--icon={}".format(os.path.join(ICON_PATH, "icon.ico")),
        "--add-data=assets;assets",
        MAIN_SCRIPT
    ], check=True)
    
    # Copy the executable to the exe folder
    src_exe = os.path.join("dist", APP_NAME, f"{APP_NAME}.exe")
    dst_exe = os.path.join(EXE_DIR, f"{APP_NAME}.exe")
    
    if os.path.exists(src_exe):
        # Copy exe file
        shutil.copy2(src_exe, dst_exe)
        print(f"✓ Copied executable to {dst_exe}")
        
        # Copy necessary DLLs and dependencies
        exe_deps_dir = os.path.join(EXE_DIR, "lib")
        os.makedirs(exe_deps_dir, exist_ok=True)
        
        # Copy all files from dist/APP_NAME to exe/lib folder
        for item in os.listdir(os.path.join("dist", APP_NAME)):
            if item != f"{APP_NAME}.exe":
                src_item = os.path.join("dist", APP_NAME, item)
                dst_item = os.path.join(exe_deps_dir, item)
                
                if os.path.isdir(src_item):
                    if os.path.exists(dst_item):
                        shutil.rmtree(dst_item)
                    shutil.copytree(src_item, dst_item)
                else:
                    shutil.copy2(src_item, dst_item)
        
        print(f"✓ Copied dependencies to {exe_deps_dir}")
    else:
        print(f"⚠ Could not find {src_exe}. Build may have failed.")
    
    print("✓ Windows build completed")

def setup_macos():
    """Build for macOS"""
    print("Building for macOS...")
    
    # Create resources directory in case it doesn't exist
    os.makedirs("assets", exist_ok=True)
    
    # Run PyInstaller
    subprocess.run([
        "pyinstaller",
        "--name={}".format(APP_NAME),
        "--windowed",
        "--icon={}".format(os.path.join(ICON_PATH, "icon.icns")),
        "--add-data=assets:assets",
        "--osx-bundle-identifier=com.colornote.app",
        MAIN_SCRIPT
    ], check=True)
    
    print("✓ macOS build completed")
    print(f"  App is at: dist/{APP_NAME}.app")

def setup_linux():
    """Build for Linux"""
    print("Building for Linux...")
    
    # Create resources directory in case it doesn't exist
    os.makedirs("assets", exist_ok=True)
    
    # Run PyInstaller
    subprocess.run([
        "pyinstaller",
        "--name={}".format(APP_NAME),
        "--windowed",
        "--icon={}".format(os.path.join(ICON_PATH, "icon.png")),
        "--add-data=assets:assets",
        MAIN_SCRIPT
    ], check=True)
    
    # Create .desktop file for Linux
    desktop_file = f"""[Desktop Entry]
Name={APP_NAME}
Exec=/usr/local/bin/{APP_NAME}/{APP_NAME}
Icon=/usr/local/share/icons/{APP_NAME}.png
Type=Application
Categories=Utility;TextEditor;
"""
    
    with open(f"dist/{APP_NAME}.desktop", "w") as f:
        f.write(desktop_file)
    
    print("✓ Linux build completed")
    print(f"  Executable is at: dist/{APP_NAME}/{APP_NAME}")
    print(f"  Desktop file created at: dist/{APP_NAME}.desktop")

def prepare_android():
    """Prepare for Android build using Buildozer"""
    print("Preparing Android build...")
    
    # Create apk directory if it doesn't exist
    os.makedirs(APK_DIR, exist_ok=True)
    
    # Check for buildozer
    try:
        subprocess.run(["buildozer", "--version"], check=True, stdout=subprocess.PIPE)
    except (subprocess.SubprocessError, FileNotFoundError):
        print("⚠ Buildozer not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "buildozer"], check=True)
    
    # Initialize buildozer if spec file doesn't exist
    if not os.path.exists("buildozer.spec"):
        subprocess.run(["buildozer", "init"], check=True)
        
        # Update the spec file
        with open("buildozer.spec", "r") as f:
            spec_content = f.read()
        
        # Replace placeholders
        spec_content = spec_content.replace("title = My Application", f"title = {APP_NAME}")
        spec_content = spec_content.replace("package.name = myapp", "package.name = colornote")
        spec_content = spec_content.replace("source.include_exts = py,png,jpg,kv,atlas", 
                                           "source.include_exts = py,png,jpg,kv,atlas,json")
        spec_content = spec_content.replace("requirements = python3", 
                                          "requirements = python3,pyqt6,pillow,pyyaml")
        
        # Write updated spec
        with open("buildozer.spec", "w") as f:
            f.write(spec_content)
    
    # Build the APK
    try:
        print("Building Android APK...")
        subprocess.run(["buildozer", "android", "debug"], check=True)
        
        # Find the APK file
        apk_files = glob.glob(os.path.join("bin", "*.apk"))
        if apk_files:
            latest_apk = max(apk_files, key=os.path.getctime)
            # Copy to the apk directory
            dst_apk = os.path.join(APK_DIR, os.path.basename(latest_apk))
            shutil.copy2(latest_apk, dst_apk)
            print(f"✓ APK copied to {dst_apk}")
        else:
            print("⚠ No APK files found in the bin directory")
    except subprocess.CalledProcessError:
        print("⚠ Failed to build Android APK. Check buildozer output for details.")
    
    print("✓ Android build process completed")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Build C0lorNote for different platforms")
    parser.add_argument("--clean", action="store_true", help="Clean build directories")
    parser.add_argument("--windows", action="store_true", help="Build for Windows")
    parser.add_argument("--macos", action="store_true", help="Build for macOS")
    parser.add_argument("--linux", action="store_true", help="Build for Linux")
    parser.add_argument("--android", action="store_true", help="Build for Android")
    parser.add_argument("--all", action="store_true", help="Build for all platforms")
    
    args = parser.parse_args()
    
    # Default to current platform if no specific platform is specified
    if not (args.windows or args.macos or args.linux or args.android or args.all):
        system = platform.system().lower()
        if system == "windows":
            args.windows = True
        elif system == "darwin":
            args.macos = True
        elif system == "linux":
            args.linux = True
    
    # Clean if requested
    if args.clean:
        clean_build_dirs()
    
    # Build for all platforms if requested
    if args.all:
        args.windows = True
        args.macos = True
        args.linux = True
        args.android = True
    
    # Build for each specified platform
    if args.windows:
        setup_windows()
    
    if args.macos:
        setup_macos()
    
    if args.linux:
        setup_linux()
    
    if args.android:
        prepare_android()
    
    print("Build process completed!")

if __name__ == "__main__":
    main() 