from pytube import YouTube
from pytube import Playlist


downloadType = input("you need download particular video?[Y/N]")

if downloadType == 'Y':
    link = input("Please enter youtube link here: ")

    video = YouTube(link)
    print("IMPORTANT INFORMATION ABOUT THIS VIDEO")
    print("video title " + video.title)
    print("video description " + video.description)

    video.streams.get_lowest_resolution().download(output_path="/Users/mohamednasr/Downloads/tubeDownloader/")
else:
    link = input("Please enter youtube playlist link here: ")

    playlist = Playlist(link)

    for video in playlist.videos:
        video.streams.get_lowest_resolution().download(output_path="/Users/mohamednasr/Downloads/tubeDownloader/")



