# DEVELOPER_KEY = 'AIzaSyDcyuBK8h2bR4zB5j_a5zHFsJTOK5J0rtA'
# channel_id = 'UCuew8JoX6PBXRcBgdqVy-wQ' # supportvectors

import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pyrsistent import v
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from pytube import YouTube
from pydub import AudioSegment

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
DEVELOPER_KEY = 'AIzaSyDcyuBK8h2bR4zB5j_a5zHFsJTOK5J0rtA'

def get_channel_videos_by_id(channel_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    try:
        # Fetch the channel details using channelId
        channel_response = youtube.channels().list(
            id=channel_id,
            part='contentDetails'
        ).execute()

        # Check if the 'items' key is in the response
        if 'items' not in channel_response or not channel_response['items']:
            print('No channel found for id: %s' % channel_id)
            return []

        uploads_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        videos = []
        next_page_token = None
        while True:
            playlist_response = youtube.playlistItems().list(
                playlistId=uploads_id,
                part='snippet',
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            videos += playlist_response['items']
            next_page_token = playlist_response.get('nextPageToken')

            if next_page_token is None:
                break
                
        
        video_urls = ['https://www.youtube.com/watch?v=' + video['snippet']['resourceId']['videoId'] for video in videos]
        # video_ids = [video['snippet']['resourceId']['videoId'] for video in videos]
       
        return video_urls   

    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
        return []
    except KeyError as e:
        print('KeyError: The response from the API does not contain the expected key:', e)
        return []

# This function fetches transcripts for a given video ID.
def get_transcript(video_id):
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Initialize text formatter
        formatter = TextFormatter()

        # Format the transcript as plain text
        plain_text_transcript = formatter.format_transcript(transcript)

        return plain_text_transcript

    except Exception as e:
        print(f"An error occurred when fetching the transcript for video {video_id}: {e}")
        return None

def download_and_convert_audio(url, output_path):
    yt = YouTube(url)
    audio_stream = yt.streams.get_audio_only()
    download_path = audio_stream.download(output_path)

    # Converting the audio
    audio = AudioSegment.from_file(download_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    
    # Saving the converted audio
    output_file = output_path + "/converted_audio.mp3"
    audio.export(output_file, format="mp3")
    return output_file


if __name__ == '__main__':
    channel_name = '@SupportVectors'  # The '@' is typically not part of the YouTube username.
    channel_id = 'UCuew8JoX6PBXRcBgdqVy-wQ' #'UCD2V0-5WMVJrNo3CCK2M89A'
    video_urls = get_channel_videos_by_id(channel_id)
    print(len(video_urls))
    for url in video_urls[:10]:
        print(url)

    converted_audio_path = download_and_convert_audio(video_urls[0], os.getcwd()+"/audio")

    # Loop over video IDs and fetch transcripts
    transcript = get_transcript(video_urls[0].split('=')[1])
    if transcript:
        print(f"Transcript for video {video_urls[0].split('=')[1]}:\n{transcript}")

