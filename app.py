from flask import Flask, render_template, request
import cv2
import os
from cartoonify import cartoonify_image

os.makedirs("uploads", exist_ok=True)
os.makedirs("static", exist_ok=True)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "static"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["image"]

        original_path = os.path.join("static", "original.jpg")
        file.save(original_path)

        # FIX 1
        cartoon = cartoonify_image(original_path)

        output_path = os.path.join(
            OUTPUT_FOLDER,
            "cartoon.jpg"
        )

        cv2.imwrite(output_path, cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR))

        return render_template(
            "index.html",
            cartoon="cartoon.jpg",
            original="original.jpg"   # FIX 2
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)