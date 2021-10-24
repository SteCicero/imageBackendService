from flask import Flask, request, send_from_directory
from flask_restful import Api, Resource, reqparse, abort
import os
from werkzeug.utils import secure_filename
import PIL.Image
from multiprocessing import Process


app = Flask(__name__)
api = Api(app)
STORAGE_PATH = "storage/"
MAX_WIDTH = 2000
MAX_HEIGHT = 2000


img_resize_args = reqparse.RequestParser()
img_resize_args.add_argument("width", type=int, help="Width of the image is required", required=True)
img_resize_args.add_argument("height", type=int, help="Height of the image is required", required=True)

images = []

def load_img_list():
    for img in os.listdir(STORAGE_PATH):
        images.append(img)
    images.sort()

def img_resize(filename, width, height):
    image = PIL.Image.open(STORAGE_PATH + filename)
    resized_image = image.resize((width, height))
    resized_image.save(STORAGE_PATH + filename)
    

class ImageList(Resource):
    def get(self):
        return images
    
    def post(self):
        if "file" not in request.files:
            abort(400 , message="No file part in the request")

        file = request.files["file"]

        if file.filename == "":
            abort(400, message="No image selected for uploading")

        filename = secure_filename(file.filename)

        if filename in images:
            abort(409, message="Image already exists with that name...")

        file.save(os.path.join(STORAGE_PATH, filename))
        file.close()
        images.append(filename)
        images.sort()
        return "Image successfully uploaded", 201


class Image(Resource):
    def get(self, img_name):
        filename = secure_filename(img_name)
        if filename not in images:
            abort(404, message="Could not find image...")
        
        path = os.path.join(app.root_path, STORAGE_PATH)
        #return path
        return send_from_directory(path, filename)

    def delete(self, img_name):
        filename = secure_filename(img_name)
        if filename not in images:
            abort(404, message="Could not find image...")
        images.remove(filename)
        os.remove(STORAGE_PATH + filename)
        images.sort()
        return "", 204


    def patch(self, img_name):
        filename = secure_filename(img_name)
        if filename not in images:
            abort(404, message="Could not find image")

        args = img_resize_args.parse_args()

        if args["width"] > MAX_WIDTH or args["height"] > MAX_HEIGHT:
            abort(404, message="Out of bound parameters")

        p = Process(target=img_resize, args=(filename, args["width"], args["height"]))
        p.start()

        return "Image successfully resized",202


api.add_resource(ImageList, "/")
api.add_resource(Image, "/<string:img_name>")


if __name__ == "__main__":
    load_img_list()
    app.run(debug=True, port = 5000)
