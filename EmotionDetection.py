import requests, json

class EmotionDetection():
    def __init__(self):
        keyFile = open("key.txt", "r")

        if keyFile.mode == 'r':
            subscription_key = keyFile.read()
        assert subscription_key

        self.face_api_url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/detect'

        self.headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/octet-stream'
        }
            
        self.params = {
            'returnFaceAttributes': 'emotion'
        }

    def getEmotion(self):
        try:
            image = open("snapshot.png", 'rb').read()
        except:
            print("image not found")

        response = requests.post(self.face_api_url, params=self.params, headers=self.headers, data=image)
        res = response.json()[0]['faceAttributes']['emotion']

        emotions = {
            'happiness': res['happiness'],
            'sadness': res['sadness'],
            'anger': res['anger']
        }

        max = 0

        for emotion in emotions.values():
            if emotion > max:
                max = emotion

        mood = list(emotions.keys())[list(emotions.values()).index(max)]
        print('Detected Emotion: ' + mood)
        return mood
    