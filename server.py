import os
import base64
import mimetypes

from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from fashn import Fashn


# ==========================================
# PROJECT SETTINGS
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

load_dotenv(
    os.path.join(BASE_DIR, ".env")
)

API_KEY = os.getenv(
    "FASHN_API_KEY"
)

if not API_KEY:
    raise Exception(
        "FASHN_API_KEY was not found."
    )


app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = (
    10 * 1024 * 1024
)


# ==========================================
# FASHN CONNECTION
# ==========================================

client = Fashn(
    api_key=API_KEY
)


# ==========================================
# PRODUCT IMAGES
# ==========================================

PRODUCT_IMAGES = {

    "1": "black-shirt.jpg",
    "2": "black-casual.jpg",
    "3": "blue-shirt.jpg",
    "4": "white-tshirt.jpg",
    "5": "black-tshirt.jpg",
    "6": "green-shirt.jpg",

    "7": "navy-casual-shirt.jpg",
    "8": "white-formal-shirt.jpg",
    "9": "blue-casual-tshirt.jpg",
    "10": "green-tshirt.jpg",
    "11": "black-executive-shirt.jpg",
    "12": "white-street-tshirt.jpg",
    "13": "blue-polo-shirt.jpg",
    "14": "premium-black-tshirt.jpg",
    "15": "green-formal-shirt.jpg",
    "16": "premium-white-shirt.jpg"
}


# ==========================================
# ALLOWED CUSTOMER IMAGE TYPES
# ==========================================

ALLOWED_IMAGE_TYPES = {

    "image/jpeg",
    "image/jpg",
    "image/png"

}


# ==========================================
# CONVERT LOCAL PRODUCT IMAGE TO BASE64
# ==========================================

def file_to_base64(path):

    mime_type, _ = (
        mimetypes.guess_type(path)
    )

    if not mime_type:
        mime_type = "image/jpeg"

    with open(path, "rb") as file:

        encoded = base64.b64encode(
            file.read()
        ).decode("utf-8")

    return (
        f"data:{mime_type};"
        f"base64,{encoded}"
    )


# ==========================================
# CONVERT CUSTOMER UPLOAD TO BASE64
# ==========================================

def uploaded_file_to_base64(file):

    image_bytes = file.read()

    encoded = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    mime_type = (
        file.mimetype
        or "image/jpeg"
    )

    return (
        f"data:{mime_type};"
        f"base64,{encoded}"
    )


# ==========================================
# HOME WEBSITE
# ==========================================

@app.route("/")
def home():

    return send_from_directory(
        BASE_DIR,
        "index.html"
    )


# ==========================================
# NORMAL WEBSITE
# ==========================================

@app.route("/normal.html")
def normal_page():

    return send_from_directory(
        BASE_DIR,
        "normal.html"
    )


# ==========================================
# TRY-ON PAGE
# ==========================================

@app.route("/tryon.html")
def tryon_page():

    return send_from_directory(
        BASE_DIR,
        "tryon.html"
    )


# ==========================================
# INDEX PAGE
# ==========================================

@app.route("/index.html")
def index_page():

    return send_from_directory(
        BASE_DIR,
        "index.html"
    )


# ==========================================
# CSS
# ==========================================

@app.route("/style.css")
def style_file():

    return send_from_directory(
        BASE_DIR,
        "style.css"
    )


# ==========================================
# JAVASCRIPT
# ==========================================

@app.route("/products.js")
def products_file():

    return send_from_directory(
        BASE_DIR,
        "products.js"
    )


@app.route("/script.js")
def script_file():

    return send_from_directory(
        BASE_DIR,
        "script.js"
    )


@app.route("/normal.js")
def normal_script():

    return send_from_directory(
        BASE_DIR,
        "normal.js"
    )


# ==========================================
# PRODUCT IMAGES
# ==========================================

@app.route(
    "/images/<path:filename>"
)
def product_images(filename):

    image_folder = os.path.join(
        BASE_DIR,
        "images"
    )

    return send_from_directory(
        image_folder,
        filename
    )


# ==========================================
# AI VIRTUAL TRY-ON
# ==========================================

@app.route(
    "/tryon",
    methods=["POST"]
)
def tryon():

    try:

        # --------------------------------
        # CUSTOMER PHOTO
        # --------------------------------

        user_photo = request.files.get(
            "userPhoto"
        )

        if not user_photo:

            return jsonify({

                "success": False,

                "error":
                "Please upload your photo."

            }), 400


        # --------------------------------
        # CHECK IMAGE TYPE
        # --------------------------------

        if (
            user_photo.mimetype
            not in ALLOWED_IMAGE_TYPES
        ):

            return jsonify({

                "success": False,

                "error":
                "Only JPG, JPEG and PNG images are allowed."

            }), 400


        # --------------------------------
        # SELECTED PRODUCT
        # --------------------------------

        product_id = request.form.get(
            "productId"
        )


        if product_id not in PRODUCT_IMAGES:

            return jsonify({

                "success": False,

                "error":
                "Selected clothing was not found."

            }), 400


        # --------------------------------
        # PRODUCT IMAGE PATH
        # --------------------------------

        garment_filename = (
            PRODUCT_IMAGES[
                product_id
            ]
        )


        garment_path = os.path.join(

            BASE_DIR,

            "images",

            garment_filename

        )


        if not os.path.exists(
            garment_path
        ):

            return jsonify({

                "success": False,

                "error":
                "Product image was not found."

            }), 404


        print(
            "Preparing customer image..."
        )


        # --------------------------------
        # CUSTOMER IMAGE -> BASE64
        # --------------------------------

        model_image = (
            uploaded_file_to_base64(
                user_photo
            )
        )


        print(
            "Preparing garment image..."
        )


        # --------------------------------
        # CLOTHING IMAGE -> BASE64
        # --------------------------------

        garment_image = (
            file_to_base64(
                garment_path
            )
        )


        print(
            "Sending request to FASHN AI..."
        )


        # =================================
        # FASHN AI
        # =================================

        result = (
            client.predictions.subscribe(

                model_name=
                "tryon-v1.6",

                inputs={

                    "model_image":
                    model_image,

                    "garment_image":
                    garment_image,

                    "category":
                    "tops",

                    "garment_photo_type":
                    "auto",

                    "mode":
                    "quality",

                    "num_samples":
                    1,

                    "output_format":
                    "png",

                    "return_base64":
                    True
                }
            )
        )


        # --------------------------------
        # CHECK AI RESULT
        # --------------------------------

        if result.status != "completed":

            error_message = (
                "AI generation failed."
            )

            if result.error:

                error_message = str(
                    result.error
                )


            return jsonify({

                "success": False,

                "error":
                error_message

            }), 500


        if not result.output:

            return jsonify({

                "success": False,

                "error":
                "AI returned no image."

            }), 500


        # --------------------------------
        # GENERATED IMAGE
        # --------------------------------

        generated_image = (
            result.output[0]
        )


        print(
            "AI Try-On completed!"
        )


        # --------------------------------
        # SEND RESULT TO WEBSITE
        # --------------------------------

        return jsonify({

            "success": True,

            "image":
            generated_image

        })


    except Exception as error:

        print(
            "SERVER ERROR:",
            error
        )


        return jsonify({

            "success": False,

            "error":
            str(error)

        }), 500


# ==========================================
# START SERVER
# ==========================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(

        host="0.0.0.0",

        port=port,

        debug=True

    )