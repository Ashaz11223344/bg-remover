from flask import Flask, render_template, request
from rembg import remove
from PIL import Image
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        file = request.files.get("image")
        custom_name = request.form.get("custom_name")

        if not file:
            return render_template("index.html")

        if custom_name and custom_name.strip() != "":
            filename = custom_name.strip() + ".png"
        else:
            filename = str(uuid.uuid4()) + ".png"

        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        file.save(input_path)

        img = Image.open(input_path)
        result = remove(img)
        result.save(output_path)

        return render_template(
            "index.html",
            output_image=f"/static/output/{filename}"
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

