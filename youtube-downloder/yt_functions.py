from pytube import YouTube, exceptions  # Importing necessary modules
from requests import get
import os

# Function to clear the console
def clean(): 
    os.system('cls')

# Functions for colorizing output messages
def show(msg): 
    return '\033[94m' + msg + '\033[00m'  # blue

def succeed(msg): 
    return '\033[92m' + msg + '\033[00m'  # green

def alert(msg): 
    return '\033[91m' + msg + '\033[00m'  # red

# Function to check internet connectivity
def checkInternetconnection(timeout=5):
    try:
        # Use IPify API to check internet connection
        response = get('https://api64.ipify.org?format=json').json()
        response = get(f'https://ipapi.co/{response["ip"]}/json/').json()
        print(succeed('Internet is connected.'))

        # Check if the country code is Iran (IR)
        if response["country_code"] == 'IR':
            print(alert('Please check your VPN and try again'))
            return False
        else:
            print(succeed('YouTube is accessible.'))
            return True
    except ConnectionError:
        print(alert("Internet disconnected.\nPlease check your internet connection"))

# Class for YouTube video downloader
class yt_downloader:
    def __init__(self, link):
        # Initialize YouTube object with the provided link
        self.video = YouTube(link)

    def __str__(self):
        # String representation of the YouTube video
        return show(f"""
    Title: {self.video.title}
    Owner: {self.video.channel_id}
    Length: {self.video.length}
    Date Published: {self.video.publish_date}
    Rating: {self.video.rating}
    Views: {self.video.views}

    Highest resolution: {self.video.streams.get_highest_resolution().resolution}
    Size: {round((self.video.streams.get_highest_resolution().filesize)*0.000001, 2)}

    Lowest resolution: {self.video.streams.get_lowest_resolution().resolution}
    Size: {round((self.video.streams.get_lowest_resolution().filesize)*0.000001, 2)}
    """)

    def download_onlyaudio(self, path, name):
        # Download only the audio of the video
        out_file = self.video.streams.filter(
            only_audio=True).first().download(output_path=path, filename=name)
        base, _ = os.path.splitext(out_file)
        os.rename(out_file, base + '.mp3')

    def download_onlyvideo(self, path, name, resolution):
        # Download only the video of the specified resolution
        self.video.streams.filter(only_video=True, resolution=resolution).first(
        ).download(output_path=path, filename=name)

    def download_video(self, path, name, resolution):
        # Download the video of the specified resolution
        self.video.streams.filter(resolution=resolution).first(
        ).download(output_path=path, filename=name)

    def get_other_resolutions(self):
        # Get and show available resolutions
        res = list()
        for i in self.video.streams:
            if (i.resolution not in res) and (i.resolution is not None):
                res.append(str(i.resolution))
        return res

    def get_reso(self):
        # Get the desired resolution from the user
        assure = input("Download highest resolution? [y/n]")
        intended_resolution = str(
            self.video.streams.get_highest_resolution().resolution)

        while assure != 'y':
            res = self.get_other_resolutions()
            # Show available resolutions and get user's intended resolution
            intended_resolution = input(
                show(f'Available resolutions:\n{sorted(res)}\n>>>')) + 'p'

            if intended_resolution not in res:
                print(
                    alert(f'Resolution is not VALID\nThere is no {intended_resolution}'))
                clean()
            else:
                break

        return intended_resolution
