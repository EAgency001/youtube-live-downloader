import os
import requests
import subprocess

CHANNEL_ID = "UClei2Tl5p9-o8txRRTEKtWw"  # John Obidi Africa
API_KEY = os.environ["YOUTUBE_API_KEY"]

# Check for live stream
url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={CHANNEL_ID}&eventType=live&type=video&key={API_KEY}"
response = requests.get(url).json()
items = response.get("items", [])

if not items:
    print("No live stream found.")
    exit(0)

video_id = items[0]["id"]["videoId"]
video_url = f"https://www.youtube.com/watch?v={video_id}"
print(f"Found live stream: {video_url}")

# Use video ID as filename base
OUTPUT_FILE = f"Trade_Winds_{video_id}.mp4"

# Download with yt-dlp
cmd = [
    "yt-dlp",
    "-f", "bestvideo[height=360]+bestaudio",
    "--live-from-start",
    "--cookies", "/tmp/cookies.txt",
    video_url,
    "-o", OUTPUT_FILE
]
try:
    subprocess.run(cmd, check=True)
    print(f"Downloaded to {OUTPUT_FILE}")
except subprocess.CalledProcessError as e:
    print(f"Download failed: {e}, but continuing for artifact.")
with open(os.environ['GITHUB_ENV'], 'a') as f:
    f.write(f"FILENAME={OUTPUT_FILE}\n")
