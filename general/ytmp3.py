import pytube
import argparse

def download_video_audio(url,fname):
    """
    Download audio from a youtube url and saves as file name fname
    """
    yt = pytube.YouTube(url)
    v = yt.streams.filter(only_audio=True).first()
    v.download(filename=fname)

# Parse args, both are required
parser = argparse.ArgumentParser(description='Download audio from a YouTube video.')
parser.add_argument('--url', required=True, help='URL of the YouTube video')
parser.add_argument('--name', required=True, help='Human name for file')
args = parser.parse_args()


print("Downloading....")
download_video_audio(args.url, args.name)
print("[OK]")
print(f"Audio downloaded as {args.name}")
