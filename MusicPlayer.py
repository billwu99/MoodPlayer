from pygame import mixer

class MusicPlayer():
    def __init__(self):
        mixer.init()

    def play(self, mood):
        mixer.music.load('Music/' + mood + '.mp3')
        mixer.music.play()

    def stop(self):
        mixer.music.stop()