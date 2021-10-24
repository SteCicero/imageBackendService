# IMS - Image Backend Service
IMS is a simple backend service that implements some basic operations on images through HTTP API. The main feature of this backend service are:
 - image upload
 - image delete
 - image download
 - image resize with given width and height
 - listing of the available images

## API endpoints
IMS has 2 endpoints in order to offer his services
    
    `/`
    
    `/img_name.jpg`

where in the second one "img_name.jpg" is a parameter wich represent the file name of the image.

## Get list of images

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

### Request

`PATCH /img_name.jpeg`

     curl -v -H 'Content-Type: application/json'  -d '{"width":300, "height":300}' -X PATCH http://localhost:5000/IMG_X.jpeg

### Response

     < HTTP/1.0 202 ACCEPTED
     < Content-Type: application/json
     < Content-Length: 29
     < Server: Werkzeug/2.0.2 Python/3.8.2
     < Date: Sun, 24 Oct 2021 12:27:01 GMT
     < 
     "Image successfully resized"
     * Closing connection 0

## Get an image

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
This service has been implemented using Flask framework in Python 3.8 language.

## How to run the service
    ./main.py

## How to run the tests
    ./test.py
