import os
import requests
from flask import Flask, jsonify
from flask import request
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import mongo_client

gallery = mongo_client.gallery  # created 'gallery' database in MongoDB
images_collection = gallery.images  # Created 'images_collection' in database

load_dotenv(dotenv_path="./.env.local")
print(os.environ.get("UNSPLASH_KEY", ""))

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError(
        "Please create .env.local file and insert there UNSPLASH_KEY"
    )

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = DEBUG


@app.route("/new-image")
def new_image():
    word = request.args.get("query")
    headers = {"Accept-Version": "v1", "Authorization": "Client-ID " + UNSPLASH_KEY}
    params = {"query": word}
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)

    data = response.json()
    return data


@app.route("/images", methods=["GET", "POST"])
def images():
    if request.method == "GET":
        # read images from database using .find in images-collection and return Json {} in database
        images = images_collection.find(
            {}
        )  # this find operation refers to all data in the images collection
        return jsonify(
            [img for img in images]
        )  # return Json object, that contains array of objects, where each object= separate image in "images_collection" collection
    if request.method == "POST":
        # save image to the database
        image = (
            request.get_json()
        )  # we use data, that sent from client in Json format, using get method
        image["_id"] = image.get(
            "id"
        )  # here we are able to modify such object(we created new field: "_id")
        result = images_collection.insert_one(
            image
        )  # We perform insert_one operation, and insert one new data in our collection
        inserted_id = result.inserted_id
        return {
            "inserted_id": inserted_id
        }  # flask automatically convert such dictionary to JSON format


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
