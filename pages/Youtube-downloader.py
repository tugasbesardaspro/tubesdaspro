import streamlit as st
from pytube import YouTube
from pathlib import Path
import os

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


st.image('./components/youtube_downloader/yt.png', use_column_width=True)
st.header("APLIKASI DOWNLOAD VIDEO DAN AUDIO YOUTUBE")



video_url = st.text_input("Masukkan Link Video Youtube yang anda salin")

genre = st.radio(
"Pilih Format of Video",
('360 P', '720 P', '1080 P', 'audio/mp4 (128 kbps)', 'audio/webm (50 kbps)', 'audio/webm (70 kbps)', 'audio/webm (160 kbps)'))


if st.button("download"):

    video = YouTube(video_url)

    st.image(video.thumbnail_url, width=300)
    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {} 
    '''.format(video.title , video.length , video.rating))

    # @st.cache
    def subType(param1, param2):
        global subtype
        global btntype

        subtype = param1
        btntype = param2

        return subtype, btntype

    if genre == '360 P':
        video_streams = video.streams.filter(file_extension='mp4')
        getId = video_streams.get_by_itag(18)
        subType('mp4', 'video')
    elif genre == '720 P':
        video_streams = video.streams.filter(file_extension='mp4')
        getId = video_streams.get_by_itag(22)
        subType('mp4', 'video')        
    elif genre == '1080 P':
        video_streams = video.streams.filter(file_extension='mp4')
        getId = video_streams.get_by_itag(137)
        subType('mp4', 'video')
    elif genre == 'audio/mp4 (128 kbps)':
        video_streams = video.streams.filter(only_audio=True)
        getId = video_streams.get_by_itag(140)
        subType('mp4', 'audio')
    elif genre == 'audio/webm (50 kbps)':
        video_streams = video.streams.filter(only_audio=True)
        getId = video_streams.get_by_itag(249)
        subType('webm', 'audio')
    elif genre == 'audio/webm (70 kbps)':
        video_streams = video.streams.filter(only_audio=True)
        getId = video_streams.get_by_itag(250)
        subType('webm', 'audio')
    elif genre == 'audio/webm (160 kbps)':
        video_streams = video.streams.filter(only_audio=True)
        getId = video_streams.get_by_itag(251)
        subType('webm', 'audio')

    if getId:
        downloads_path = str(Path.home() / "Downloads")
        getId.download(get_download_path())        
        st.success("Video anda telah berhasil di download ke folder downloads")