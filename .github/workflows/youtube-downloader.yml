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

# Validate cookies file
cookies_path = "/tmp/cookies.txt"
if not os.path.exists(cookies_path) or os.path.getsize(cookies_path) == 0:
    print(f"Error: {cookies_path} is missing or empty.")
    exit(1)
with open(cookies_path, "r") as f:
    first_line = f.readline().strip()
    if not first_line.startswith("# Netscape HTTP Cookie File"):
        print(f"Error: {cookies_path} is not in Netscape format.")
        exit(1)

# Download with yt-dlp
cmd = [
    "yt-dlp",
    "-f", "bestvideo[height=360]+bestaudio",
    "--live-from-start",
    "--cookies", cookies_path,
    video_url,
    "-o", OUTPUT_FILE
]
try:
    subprocess.run(cmd, check=True)
    print(f"Downloaded to {OUTPUT_FILE}")
except subprocess.CalledProcessError as e:
    print(f"Download failed: {e}")
    raise  # Re-raise to fail the step if critical
with open(os.environ['GITHUB_ENV'], 'a') as f:
    f.write(f"FILENAME={OUTPUT_FILE}\n")
