from flask import Flask, render_template, request
import cv2
import numpy as np
import os
from cartoonify import cartoonify_image

app = Flask(__name__)

os.makedirs("static", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        if "image" not in request.files:
            return render_template("index.html")

        file = request.files["image"]

        if file.filename == "":
            return render_template("index.html")

        try:
            file_bytes = np.frombuffer(file.read(), np.uint8)

            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            if img is None:
                return "Invalid image"

            cartoon = cartoonify_image(img)

            output_path = os.path.join("static", "cartoon.jpg")

            cv2.imwrite(output_path, cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR))

            return render_template(
                "index.html",
                cartoon="cartoon.jpg"
            )

        except Exception as e:
            print("SERVER ERROR:", e)
            return "Error processing image"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)