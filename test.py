import requests
import time

BASE = "http://127.0.0.1:5000/"
DELAY = 2

print("===== BACKEND APP TESTBENCH =====")

time.sleep(DELAY)

print("Getting the list of images")
response = requests.get(BASE)
print(response.json())

time.sleep(DELAY)

print("Trying to delete an image")
response = requests.delete(BASE + "/IMG_2039.jpeg")
print(response)

print("Getting the list of images")
response = requests.get(BASE)
print(response.json())

time.sleep(DELAY)

print("Uploading an image")
response = requests.post(BASE, files = {"file": open("IMG_X.jpeg", "rb")})
print(response.json())

print("Getting the list of images")
response = requests.get(BASE)
print(response.json())

time.sleep(DELAY)

print("Resizing the uploaded image")
response = requests.patch(BASE + "IMG_X.jpeg", {"width" : 256, "height": 256} )
print(response.json())

time.sleep(DELAY)

print("Downloading the resized image")
response = requests.get(BASE + "IMG_X.jpeg")
open("IMG_X_resized.jpeg", "wb").write(response.content)
