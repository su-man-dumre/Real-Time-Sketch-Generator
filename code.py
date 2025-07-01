import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os

# Fix: Put the absolute or relative path to your haarcascade xml file here:
HAAR_PATH = 'haarcascade_frontalface_default.xml'

if not os.path.exists(HAAR_PATH):
    messagebox.showerror("Error", f"Haar cascade file not found: {HAAR_PATH}")
    exit()

face_cascade = cv2.CascadeClassifier(HAAR_PATH)

class SketchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sketch Generator")
        self.img_path = None
        self.sketch = None

        # GUI buttons
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        self.generate_btn = tk.Button(root, text="Generate Sketch", command=self.generate_sketch)
        self.generate_btn.pack(pady=5)

        self.canny_btn = tk.Button(root, text="Generate Canny Edge Sketch", command=self.generate_canny_sketch)
        self.canny_btn.pack(pady=5)

        self.webcam_btn = tk.Button(root, text="Start Webcam Face Sketch", command=self.start_webcam_sketch)
        self.webcam_btn.pack(pady=5)

        self.save_btn = tk.Button(root, text="Save Sketch", command=self.save_sketch)
        self.save_btn.pack(pady=5)

        # Image display label
        self.img_label = tk.Label(root)
        self.img_label.pack()

    def upload_image(self):
        self.img_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
        )
        if self.img_path:
            img = Image.open(self.img_path)
            # Use this new enum in Pillow >= 10.0.0
            img = img.resize((400, 300), Image.Resampling.LANCZOS)
            render = ImageTk.PhotoImage(img)
            self.img_label.config(image=render)
            self.img_label.image = render
            self.sketch = None

    def generate_sketch(self):
        if not self.img_path:
            messagebox.showwarning("Warning", "Please upload an image first.")
            return
        img = cv2.imread(self.img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inverted = cv2.bitwise_not(gray)
        blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
        inverted_blurred = cv2.bitwise_not(blurred)
        self.sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

        self.show_sketch(self.sketch)

    def generate_canny_sketch(self):
        if not self.img_path:
            messagebox.showwarning("Warning", "Please upload an image first.")
            return
        img = cv2.imread(self.img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self.sketch = cv2.Canny(gray, 100, 200)
        self.show_sketch(self.sketch)

    def show_sketch(self, sketch_img):
        # Convert OpenCV image (BGR or grayscale) to PIL format for Tkinter display
        if len(sketch_img.shape) == 2:  # grayscale
            img = Image.fromarray(sketch_img)
        else:
            img = Image.fromarray(cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB))

        img = img.resize((400, 300), Image.Resampling.LANCZOS)
        render = ImageTk.PhotoImage(img)
        self.img_label.config(image=render)
        self.img_label.image = render

    def save_sketch(self):
        if self.sketch is None:
            messagebox.showwarning("Warning", "No sketch to save. Generate a sketch first.")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG files", "*.jpg"),
                                                            ("PNG files", "*.png"),
                                                            ("All files", "*.*")])
        if save_path:
            cv2.imwrite(save_path, self.sketch)
            messagebox.showinfo("Saved", f"Sketch saved to {save_path}")

    def start_webcam_sketch(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "Could not open webcam.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                face = frame[y:y + h, x:x + w]
                gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                inverted = cv2.bitwise_not(gray_face)
                blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
                inverted_blurred = cv2.bitwise_not(blurred)
                sketch = cv2.divide(gray_face, inverted_blurred, scale=256.0)
                frame[y:y + h, x:x + w] = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

            cv2.imshow('Webcam Sketch - Press q to quit', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = tk.Tk()
    app = SketchApp(root)
    root.mainloop()
