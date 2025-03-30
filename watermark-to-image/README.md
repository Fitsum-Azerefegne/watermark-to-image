 📸 Watermark Creator - README

A simple Python application built with Tkinter that lets you add text watermarks to your images.

 🎯 Features
- Upload JPG, PNG, BMP, or GIF images
- Automatically resizes images to 800x800 pixels
- Add custom text watermarks
- Preview watermarked images

 📦 Requirements
- Python 3.x
- Pillow library (PIL fork)

 🛠️ Installation
1. Install Python from [python.org](https://www.python.org/downloads/)
2. Install required libraries:
```bash
pip install pillow
```

 🖼️ How to Use
1. Run the application:
```bash
python watermark_app.py
```
2. Click "Upload Image" and select an image file
3. Enter your watermark text when prompted
4. View the watermarked image in the preview window

 ⚙️ Technical Details
- Uses Tkinter for the GUI interface
- Leverages Pillow (PIL) for image processing
- Automatically resizes images while maintaining aspect ratio
- Places watermarks in bottom-right corner

 📂 Project Structure
```
watermark_app/
└── watermark_app.py      # Main application file
```

 📜 License
This project is licensed under the MIT License. Free to use and modify.
