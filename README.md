# Real-Time-Sketch-Generator
🖼️ Sketch Generator App
This is a simple yet powerful Sketch Generator built with Python, OpenCV, and Tkinter.
It lets you:

Upload an image and turn it into a pencil sketch.

Apply a Canny Edge sketch filter.

Use your webcam to detect faces and sketch them in real time.

Save your generated sketches easily.

📸 Features
✅ Image Upload: Supports .jpg, .jpeg, .png, .bmp files.
✅ Pencil Sketch Generator: Classic pencil sketch effect using inversion and division.
✅ Canny Edge Detector: Create high-contrast edge sketches.
✅ Webcam Face Sketch: Detect faces in real-time via webcam and sketch them live.
✅ Save Sketch: Save your sketches in JPEG or PNG format.

🛠️ Tech Stack
Python 3.x

OpenCV

Tkinter

Pillow (PIL)

📂 Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/su-man-dumre/sketch-generator.git
cd sketch-generator
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
Install the required dependencies:

bash
Copy
Edit
pip install opencv-python pillow
Download Haar Cascade:

Make sure you have the haarcascade_frontalface_default.xml file in your project directory.

You can download it here.

▶️ How to Run
bash
Copy
Edit
python sketch_app.py
This will launch the Tkinter GUI.

⚙️ How It Works
Pencil Sketch: Uses grayscale inversion, Gaussian blur, and color dodge blending.

Canny Edge: Uses OpenCV’s Canny Edge Detector.

Webcam: Uses OpenCV’s Haar Cascade for face detection. The detected face area is converted into a pencil sketch in real time.

GUI: Simple, intuitive interface built with Tkinter.

📝 Notes
Ensure your haarcascade_frontalface_default.xml is in the same directory as the Python script or update the HAAR_PATH variable accordingly.

The webcam sketch mode can be exited by pressing q on your keyboard.

The output image size is resized for display but saved in its original resolution.

🚀 Author
Developed by: [Your Name]
💼 Passionate Python Developer
🌏 [Your Website or LinkedIn]

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

❤️ Acknowledgements
OpenCV Team for their excellent computer vision library.

Python community for awesome open-source packages.

Enjoy sketching! 🎨
