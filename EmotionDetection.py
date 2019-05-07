import requests
import json

image = None
keyFile = open("key.txt", "r")
try:
    image = open("snapshot.png", 'rb').read()
except:
    print("image not found")

subscription_key = None
if keyFile.mode == 'r':
    subscription_key = keyFile.read()
assert subscription_key

face_api_url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/detect'

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'
 }
    
params = {
    'returnFaceAttributes': 'emotion'
}

response = requests.post(face_api_url, params=params, headers=headers, data=image)
res = response.json()[0]['faceAttributes']['emotion']
print(res)

emotions = {
    'happiness': res['happiness'],
    'sadness': res['sadness'],
    'anger': res['anger']
}

max = 0

for emotion in emotions.values():
    if emotion > max:
        max = emotion

print(list(emotions.keys())[list(emotions.values()).index(max)])