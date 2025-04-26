#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
APK Builder for C0lorNote

This script builds an Android APK and places it in the apk folder.
"""

import os
import sys
import subprocess
import glob
import shutil

print("Building C0lorNote Android APK...")

# Make sure the apk directory exists
apk_dir = "apk"
os.makedirs(apk_dir, exist_ok=True)

try:
    # Install buildozer if needed
    try:
        subprocess.run(["buildozer", "--version"], stdout=subprocess.PIPE, check=True)
    except (FileNotFoundError, subprocess.SubprocessError):
        print("Installing buildozer...")
        subprocess.run([sys.executable, "-m", "pip", "install", "buildozer"], check=True)
    
    # Initialize buildozer if needed
    if not os.path.exists("buildozer.spec"):
        subprocess.run(["buildozer", "init"], check=True)
        
        # Update buildozer.spec with app info
        with open("buildozer.spec", "r") as f:
            spec = f.read()
        
        spec = spec.replace("title = My Application", "title = C0lorNote")
        spec = spec.replace("package.name = myapp", "package.name = colornote")
        spec = spec.replace("source.include_exts = py,png,jpg,kv,atlas", 
                          "source.include_exts = py,png,jpg,kv,atlas,json")
        spec = spec.replace("requirements = python3", 
                          "requirements = python3,pyqt6,pillow,pyyaml")
        
        with open("buildozer.spec", "w") as f:
            f.write(spec)
    
    # Build the APK
    print("Building APK (this may take a while)...")
    subprocess.run(["buildozer", "android", "debug"], check=True)
    
    # Find and copy the APK
    apk_files = glob.glob(os.path.join("bin", "*.apk"))
    if apk_files:
        latest_apk = max(apk_files, key=os.path.getctime)
        dst_apk = os.path.join(apk_dir, os.path.basename(latest_apk))
        shutil.copy2(latest_apk, dst_apk)
        print(f"✓ APK built and copied to {dst_apk}")
    else:
        print("✗ No APK files found in the bin directory")
        
except Exception as e:
    print(f"✗ Error building APK: {str(e)}")
    sys.exit(1)

print("APK build process completed.")
