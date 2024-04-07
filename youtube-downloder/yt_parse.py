from argparse import ArgumentParser

# Create an ArgumentParser object with a description and epilog
parse = ArgumentParser(description="YouTube video downloader.", epilog='Written by Taha Kamali')

# Add command-line arguments
parse.add_argument('-y', '--youtube', type=str, default='', help="Link of YouTube video.")
parse.add_argument('-v', '--onlyvideo', default=False, action='store_true', help="Download just video without audio.")
parse.add_argument('-a', '--onlyaudio', default=False, action='store_true', help="Download just audio of the given link.")
parse.add_argument('-r', '--resolution', type=str, default='', help="Download video by given resolution.")

# Parse the command-line arguments
args = parse.parse_args()