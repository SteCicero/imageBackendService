import requests
import time

BASE = "http://127.0.0.1:5000/"
DELAY = 2

print("===== IMS TESTBENCH =====")

input()

print("Getting the list of images")
response = requests.get(BASE)
print(response.json())

input()

print("Deleting a non existing image")
response = requests.delete(BASE + "/IMG_X.jpeg")
print(response)

print("Getting the list of images")
response = requests.get(BASE)
print(response.json())

input()

print("Uploading a new image")
response = requests.post(BASE, files = {"file": open("IMG_X.jpeg", "rb")})
print(response.json())

print("Getting the list of images")
response = requests.get(BASE)
print(response.json())

input()

print("Uploading an existing image")
response = requests.post(BASE, files = {"file": open("IMG_X.jpeg", "rb")})
print(response.json())

print("Getting the list of images")
response = requests.get(BASE)
print(response.json())

input()

print("Deleting an existing image")
response = requests.delete(BASE + "/IMG_X.jpeg")
print(response)

print("Getting the list of images")
response = requests.get(BASE)
print(response.json())

input()

print("Uploading a new image")
response = requests.post(BASE, files = {"file": open("IMG_X.jpeg", "rb")})
print(response.json())

print("Getting the list of images")
response = requests.get(BASE)
print(response.json())

input()

print("Resizing an uploaded image at 256x256 px")
response = requests.patch(BASE + "IMG_X.jpeg", {"width" : 256, "height": 256} )
print(response.json())

time.sleep(DELAY)

print("Downloading the resized image")
response = requests.get(BASE + "IMG_XD.jpeg")
open("IMG_X_resized.jpeg", "wb").write(response.content)
