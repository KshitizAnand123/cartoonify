from flask import Flask, render_template, request
import cv2
import os
from cartoonify import cartoonify_image

os.makedirs("uploads", exist_ok=True)
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
            original_path = os.path.join("uploads", "original.jpg")
            file.save(original_path)

            cartoon = cartoonify_image(original_path)

            output_path = os.path.join("static", "cartoon.jpg")

            cv2.imwrite(output_path, cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR))

            return render_template(
                "index.html",
                cartoon="cartoon.jpg",
                original="original.jpg"
            )

        except Exception as e:
            print("SERVER Error:", e)
            return "Error processing image"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)