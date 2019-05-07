import vlc, pafy, time

class MusicPlayer():
    def __init__(self):
        self.music = {
                    "happiness": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
                    "sadness": "https://www.youtube.com/watch?v=Oa-ae6_okmg",
                    "anger": "https://www.youtube.com/watch?v=04F4xlWSFh0"
                }
        self.media = None

    def play(self, mood):
        url = self.music[mood]
        vidUrl = pafy.new(url).getbest().url
        self.media = vlc.MediaPlayer(vidUrl)
        self.media.play()
        print (self.media.get_state())


    def stop(self):
        self.media.stop()