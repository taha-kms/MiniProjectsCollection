from yt_functions import *
from argparse import Namespace
from yt_parse import args

# Main function to execute the downloading process
def main(args: Namespace):
    clean()  # Clear the console
    
    # Check internet connection status
    if checkInternetconnection():
        try:
            if args.youtube == '':  # If YouTube link is not provided as argument
                args.youtube = input('Please insert link of the YouTube video:\n>>> ')
                
            vid = yt_downloader(args.youtube)  # Create YouTube downloader object
            print(show('Loading video information...'))
            print(vid)  # Display video information

        except exceptions.RegexMatchError:
            print(alert('YouTube link is not valid.'))
            exit()

        except exceptions.VideoUnavailable:
            print(alert('YouTube link is unavailable.'))
            exit()

        intended_path = input('Intended path: ').strip()  # Get intended path for saving the video
        if intended_path == '':
            intended_path = None

        intended_name = input('Intended name: ')  # Get intended name for the video
        if intended_name == '':
            intended_name = None

        if args.resolution == '':
            args.resolution = vid.get_reso()  # Get resolution if not provided in arguments

        print(succeed('Start downloading...'))

        if args.onlyaudio:
            vid.download_onlyaudio(intended_path, intended_name)  # Download only audio if specified

        if args.onlyvideo:
            vid.download_onlyvideo(intended_path, intended_name, args.resolution)  # Download only video if specified
        else:
            vid.download_video(intended_path, intended_name, args.resolution)  # Download full video

        print(succeed('Download completed.'))


if __name__ == '__main__':
    main(args)  # Call the main function with the provided arguments
