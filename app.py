from flask import Flask, render_template, request
import cv2
import os
import numpy as np
from cartoonify import cartoonify_image

os.makedirs("static", exist_ok=True)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        if "image" not in request.files:
            return render_template("index.html")

        file = request.files["image"]

        if file.filename == "":
            return render_template("index.html")

        try:
            # Read uploaded file directly into memory
            file_bytes = np.frombuffer(file.read(), np.uint8)

            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            if img is None:
                return "Invalid image file"

            cartoon = cartoonify_image(img)

            output_path = os.path.join("static", "cartoon.jpg")

            cv2.imwrite(output_path, cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR))

            return render_template(
                "index.html",
                cartoon="cartoon.jpg",
                original=None
            )

        except Exception as e:
            print("SERVER Error:", e)
            return "Error processing image"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)