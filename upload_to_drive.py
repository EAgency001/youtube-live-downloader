from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import sys
import os

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def upload_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        exit(1)
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {'name': filename}
    media = MediaFileUpload(filename, mimetype='video/mp4')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Uploaded {filename} to Drive with ID: {file.get('id')}")

if __name__ == '__main__':
    upload_file(sys.argv[1])
