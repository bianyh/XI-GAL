import pygame
from pygame import mixer


class Music:
    def __init__(self):
        mixer.init()
        self.song_list = []

    def add_song(self, song_path, volume=1.0):
        song = mixer.Sound(song_path)
        print(song_path)
        nums = len(self.song_list)
        channel = mixer.Channel(nums)
        nums += 1
        channel.set_volume(volume)
        channel.play(song)
        self.song_list.append((channel, song_path))

    def shutdown(self, song_path):
        for i in self.song_list:
            if i[1] == song_path:
                i[0].stop()
