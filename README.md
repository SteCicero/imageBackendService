# IMS - Image Backend Service
IMS is a simple backend service that implements some basic operations on images through HTTP API. The main features of this backend service are:
 - image upload
 - image delete
 - image download
 - image resize with given width and height
 - listing of the available images

This service does not require any user authentication.

## API endpoints
IMS has 2 endpoints in order to offer his services
    
    /
    
    /img_name.jpg

where in the second one `img_name.jpg` is a parameter wich represent the file name of the image. This service runs on port 5000.

## Get list of images
This function return an ordered list of the images available on the server. Images are stored inside the 'storage' folder in the same path of the Python script

### Request

`GET /`
 
     curl http://localhost:5000 -v
 
### Response

     < HTTP/1.0 200 OK
     < Content-Type: application/json
     < Content-Length: 83
     < Server: Werkzeug/2.0.2 Python/3.8.2
     < Date: Sun, 24 Oct 2021 10:55:23 GMT
     < 
     [
        "FHTT3849.jpeg",
        "IMG_2039.jpeg",
        "IMG_2096.jpeg"
     ]
     * Closing connection 0

## Unpload an image
This function allows the upload of an image. Checks about the correctness of the request and the size of the image are performed.

### Request
     
`POST /`

     curl -v -F "file=@IMG_X.jpeg" http://localhost:5000

### Response

     < HTTP/1.0 201 CREATED
     < Content-Type: application/json
     < Content-Length: 30
     < Server: Werkzeug/2.0.2 Python/3.8.2
     < Date: Sun, 24 Oct 2021 11:21:24 GMT
     < 
     "Image successfully uploaded"
     * Closing connection 0

## Delete an image

### Request

`DELETE /img_name.jpeg`

     curl -v -X DELETE http://localhost:5000/IMG_X.jpeg

### Response

     < HTTP/1.0 204 NO CONTENT
     < Content-Type: application/json
     < Server: Werkzeug/2.0.2 Python/3.8.2
     < Date: Sun, 24 Oct 2021 11:29:56 GMT
     < 
     * Closing connection 0

## Resize an image
This function allows to resize an image given file name and width and height parameters. When the service receive a request it spawns a process which perform the resize of the image asynchronously and overwrite the original one. Checks about the correctness of the request are performed.
### Request

`PATCH /img_name.jpeg`

     curl -v -H 'Content-Type: application/json'  -d '{"width":300, "height":300}' -X PATCH http://localhost:5000/IMG_X.jpeg

### Response

     < HTTP/1.0 202 ACCEPTED
     < Content-Type: application/json
     < Content-Length: 32
     < Server: Werkzeug/2.0.2 Python/3.8.2
     < Date: Sun, 24 Oct 2021 13:33:52 GMT
     < 
     "Image resize command received"
     * Closing connection 0

## Get an image
This function allows to download an image available on the server. This has been added in order to simplify the test activity.
### Request

`GET /img_name.jpeg`

     curl -v http://localhost:5000/IMG_X.jpeg --output IMG_XD.jpeg

### Response

     < HTTP/1.0 200 OK
     < Content-Disposition: inline; filename=IMG_X.jpeg
     < Content-Type: image/jpeg
     < Content-Length: 16285
     < Last-Modified: Sun, 24 Oct 2021 12:27:02 GMT
     < Cache-Control: no-cache
     < Date: Sun, 24 Oct 2021 12:31:02 GMT
     < Server: Werkzeug/2.0.2 Python/3.8.2
     < 
     { [8192 bytes data]
     100 16285  100 16285    0     0  5301k      0 --:--:-- --:--:-- --:--:-- 5301k
     * Closing connection 0


## Architecture
IMS has been implemented using Flask framework in Python 3.8 language. The service is made of a single file Python script `main.py`. In the first part of the code some parameters of the service are defined such as the listening port and the on and the maximum upload file size
Then 2 utility functions are defined:
 - `load_img_list()` wich is called during service startup in order to scan the filesystem and generate the file list
 - `img_resize()` wich performs the resize of an image

The API implementation is distributed between 2 classes (one for each endpoint):
 - `ImageList` wich implements image uploading and image listing
 - `Image` wich implements download of an image, delete of an image and resize of an image

The service to work properly needs to keep track of the images available on the server. In order to do so while avoiding the usage of any external data persistence, IMS at startup scans the path on wich images are managed and create a list that will be updated everytime an upload or delete operation is performed.

Since the resizing of an image could be a time consuming operation, this task is performed asynchronously with respect of the request. This is a very simple solution to avoid keeping the client waiting for the operation to be performed. The issue is that the client does not receive any notification on when the operation will be completed. Improvements could be obtained by using architectural solution wich provide some callback mechanism and a queue to manage concurrent requests. The resizing operation is performed through the `Pillow` library. The complete list of the libraries used in this project could be found in the `requirements.txt` file.

## How to run the service
IMS require Python 3.8 interpreter. To install all the required libraries through PIP use the following command

    pip3 install -r requirements.txt

or

    pip install -r requirements.txt
    
To run the service use the following command:

    ./main.py
    
## How to run the service on Docker container
    ./main.py

## How to run the tests
Due to the simplicity of IMS some integration tests have been developed. In order for the tests to be correctly executed the file `IMG_X.jpeg` must be in the same path of the test script.

To run the tests use the following command:
    
    ./test.py
