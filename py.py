import os
from pytube import YouTube
import pygame

def download_music(youtube_url):

    yt = YouTube(youtube_url)


    stream = yt.streams.filter(only_audio=True).first()


    print("Baixando música...")
    stream.download(filename='music.mp4')
    print("Música baixada com sucesso!")

def play_music(file_path):

    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print("Tocando música... Pressione Ctrl+C para parar.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("Música parada.")

if __name__ == "__main__":
    youtube_url = input("Cole o link do vídeo do YouTube: ")
    download_music(youtube_url)

    play_music('music.mp4')
