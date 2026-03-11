# Cartoonify Image Web Application

A web-based application that converts images into cartoon-style visuals using OpenCV and Flask.

Users can upload an image and the system processes it using computer vision techniques to generate a cartoonified version of the image.

---

## Features

- Upload any image
- Convert images into cartoon-style visuals
- Side-by-side comparison of original and cartoon image
- Simple and clean web interface

---

## Technologies Used

- Python
- Flask
- OpenCV
- NumPy
- HTML/CSS

---

## How It Works

The cartoonification pipeline includes:

1. Grayscale conversion
2. Median blur for noise reduction
3. Adaptive thresholding for edge detection
4. K-Means color quantization
5. Bilateral filtering for smoothing
6. Combining edges with the simplified color image

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/cartoonify-app.git
cd cartoonify-app
```
