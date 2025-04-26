# 📝 C0lorNote

A modern, cross-platform note-taking application with rich text and code editing capabilities.

## ✨ Features

C0lorNote has been completely rebuilt with PyQt6 to provide a modern, feature-rich experience:

- 🎨 **Four Beautiful Themes**: Choose between Matrix (hacker-style), Dreamcore (surreal pastels), Apple Light (clean Apple-inspired), and Space Red (cosmic dark red)
- 📝 **Rich Text Editing**: Format text with bold, italic, underline, and custom colors
- 💻 **Code Editor**: Dedicated code environment with Python syntax highlighting
- 🏃 **Run Code**: Execute Python code snippets directly with F5 key
- 🔍 **Fast Search**: Instantly find notes as you type in the search bar
- 🏷️ **Organization**: Categorize and tag notes for easy filtering
- 🔄 **Smart Views**: Quickly access all notes, recent notes, or code snippets
- 📤 **Export Options**: Save notes as HTML, Python code, or plain text files
- 💾 **Auto-saving**: Notes are automatically saved as you work
- 👤 **Branded UI**: Includes subtle @marbleceo branding in the status bar.


## 🌐 Cross-Platform Support

C0lorNote is fully compatible with multiple platforms:

### 💻 Desktop Platforms
- **Windows**: Native exe with Space Red theme by default
- **macOS**: Native app bundle with Apple Light theme by default
- **Linux**: Native executable with Matrix theme by default

### 📱 Mobile Platforms
- **Android**: APK package with Dreamcore theme by default

### 🔄 Synchronized Experience
- Same clean interface across all platforms
- Consistent theme and UI components
- Platform-specific optimizations for the best performance
- Data stored in platform-appropriate locations

### 🚀 One-Click Building
We provide easy-to-use build scripts for all platforms:
```bash
# Build for all platforms
python cross_platform_setup.py --all

# Build for specific platforms
python cross_platform_setup.py --windows
python cross_platform_setup.py --macos
python cross_platform_setup.py --linux
python cross_platform_setup.py --android
```
## 🎭 Themes

### 🖥️ Matrix Theme
A hacker-inspired theme with bright green text on black backgrounds. Perfect for coding sessions and creating a cyberpunk atmosphere while taking notes.

### 🌈 Dreamcore Theme
A surreal theme with deep purples and vibrant pinks that creates a creative, dreamy environment for your notes. Ideal for brainstorming and artistic projects.

### 🌞 Minimalist Theme
A clean, distraction-free theme with soft yellow accents on a light background. Great for everyday note-taking and focused writing.

### 🔴 Space Red Theme
A bold theme with deep blacks and striking red accents, creating a dramatic cosmic feel. Perfect for night-time work and immersive coding sessions.

## 📸 Screenshots

*Note: The following are descriptions of the application's appearance with each theme. Replace with actual screenshots when available.*

- **Matrix Theme**: Dark black interface with neon green text, code highlighting in bright green and blue tones, creating a terminal-like experience.

- **Dreamcore Theme**: Rich purple background with pink accents, featuring pastel-colored UI elements and a dreamy aesthetic.

- **Minimalist Theme**: Clean white interface with soft yellow accents, minimal UI elements, and plenty of whitespace for distraction-free writing.

## 📋 Requirements

- Python 3.7+
- PyQt6
- Other dependencies in requirements.txt

## 🚀 Installation

### Direct installation

```bash
# Clone the repository
git clone https://github.com/yourusername/C0lorNote.git
cd C0lorNote

# Install dependencies
pip install -r requirements.txt

# Run the application
python modern_colornote.py
```

### Building for specific platforms

The `cross_platform_setup.py` script helps you build C0lorNote for different platforms:

```bash
# Install the build dependencies
pip install pyinstaller buildozer

# Clean previous builds
python cross_platform_setup.py --clean

# Build for your current platform
python cross_platform_setup.py

# Build for a specific platform
python cross_platform_setup.py --windows
python cross_platform_setup.py --macos
python cross_platform_setup.py --linux
python cross_platform_setup.py --android

# Build for all platforms
python cross_platform_setup.py --all
```

## Platform-specific notes

### Windows

- The app uses the Space Red theme by default on Windows
- Data is stored in %APPDATA%\c0lornote

### macOS

- The app uses the Minimalist theme by default on macOS
- Data is stored in ~/Library/Application Support/c0lornote
- Font sizes are slightly increased for better readability

### Linux

- The app uses the Matrix theme by default on Linux
- Data is stored in ~/.config/c0lornote

### Android

- The app uses the Dreamcore theme by default on Android
- Data is stored in ~/.c0lornote
- Larger font sizes and UI elements for touch interaction
- Built using Buildozer (see Android build instructions below)

## Building for Android

To build for Android:

1. Prepare your environment for Android builds:
   ```bash
   # Install buildozer
   pip install buildozer
   
   # On Ubuntu/Debian, install required packages
   sudo apt-get install -y python3-pip build-essential git python3 python3-dev \
       libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
       libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
   ```

2. Run the preparation step:
   ```bash
   python cross_platform_setup.py --android
   ```

3. Build the debug APK:
   ```bash
   buildozer android debug
   ```

4. The APK will be generated in the bin/ directory

## 🖱️ Usage

### Basic Operations

- **Create a Note**: Click the "+ New Note" button in the note list panel
- **Save a Note**: Press Ctrl+S or use File > Save (auto-saving is also enabled)
- **Delete a Note**: Select the note and press Delete or use Edit > Delete Note
- **Export a Note**: Use File > Export Note to save as HTML, Python, or text

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+N | Create new note |
| Ctrl+S | Save current note |
| Ctrl+E | Export note |
| Delete | Delete selected note |
| F5 | Run code (in code editor) |
| Ctrl+B | Bold text |
| Ctrl+I | Italic text |
| Ctrl+U | Underline text |
| Ctrl+F | Focus search bar |

### Rich Text Editing

1. Select the "Rich Text" tab in the editor
2. Use the formatting toolbar to apply:
   - Bold, italic, or underline formatting
   - Text colors
   - Other formatting options

### Code Editing & Execution

1. Select the "Code" tab in the editor
2. Write Python code with syntax highlighting
3. Press F5 or click the "Run" button to execute
4. View the output in a popup dialog

## 📂 Organization

C0lorNote provides powerful organization features to keep your notes structured:

### Categories

- Create categories for broad organization (e.g., Work, Personal, Projects)
- Click the "+" button in the Categories section to add a new category
- Assign categories when creating notes
- Filter notes by clicking on a category in the sidebar

### Tags

- Add multiple tags to notes for cross-category organization
- Create tags by clicking the "+" in the Tags section
- Add comma-separated tags when creating or editing notes
- Filter notes by clicking on a tag in the sidebar

### Smart Views

Access quick filters for your notes:
- **All Notes**: View all your notes
- **Recent**: Show notes modified in the last 7 days
- **Code Snippets**: Show only notes containing code

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions to C0lorNote are welcome! Feel free to fork the repository, make changes, and submit pull requests.

---

<p align="center">Made with ❤️ for the Linux community</p>
