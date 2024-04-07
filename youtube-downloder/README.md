# YouTube Video Downloader

This is a simple command-line tool for downloading YouTube videos. It allows you to download videos either in their entirety or just the audio or video separately. Additionally, you can specify the resolution of the video you want to download.

## Features

- Download YouTube videos by providing the video link.
- Option to download only video or audio.
- Specify the desired resolution for video downloads.

## Installation

1. Clone this repository:
    ```
    git clone https://gitlab.com/simple-python-programs/youtube-downloder.git
    ```

2. Navigate to the project directory:
    ```
    cd youtube-downloder
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

Run the script `main.py` and follow the instructions. Here are the available options:

- `-y, --youtube`: Provide the link of the YouTube video.
- `-v, --onlyvideo`: Download only the video without audio.
- `-a, --onlyaudio`: Download only the audio of the given link.
- `-r, --resolution`: Download the video by the specified resolution.

### Example usage:

```bash
python main.py -y <video_link> -v -r 720p
```

### Requirements

- Python 3.x
- pytube library