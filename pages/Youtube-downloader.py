import streamlit as st
from pytube import YouTube


link = '../components/youtube_downloader/download/'

st.image(f'./components/youtube_downloader/yt.png', use_column_width=True)
st.header("APLIKASI DOWNLOAD VIDEO DAN AUDIO YOUTUBE")


video_url = st.text_input("Masukkan Link Video Youtube yang anda salin")

genre = st.radio(
    "Pilih Format of Video",
    ('360 P', '720 P', '1080 P', 'audio/mp4 (128 kbps)', 'audio/webm (50 kbps)', 'audio/webm (70 kbps)', 'audio/webm (160 kbps)'))


if video_url:

    video = YouTube(video_url)

    st.image(video.thumbnail_url, width=300)
    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {} 
    '''.format(video.title, video.length, video.rating))

    if genre == '360 P':
        video_streams = video.streams.filter(file_extension='mp4')
        getId = video_streams.get_by_itag(18)
        subtype = 'mp4'
        btntype = 'video'
    if genre == '720 P':
        video_streams = video.streams.filter(file_extension='mp4')
        getId = video_streams.get_by_itag(22)
        subtype = 'mp4'
        btntype = 'video'
    if genre == '1080 P':
        video_streams = video.streams.filter(file_extension='mp4')
        getId = video_streams.get_by_itag(137)
        subtype = 'mp4'
        btntype = 'video'
    if genre == 'audio/mp4 (128 kbps)':
        video_streams = video.streams.filter(only_audio=True)
        getId = video_streams.get_by_itag(140)
        subtype = 'mp4'
        btntype = 'audio'
    if genre == 'audio/webm (50 kbps)':
        video_streams = video.streams.filter(only_audio=True)
        getId = video_streams.get_by_itag(249)
        subtype = 'webm'
        btntype = 'audio'
    if genre == 'audio/webm (70 kbps)':
        video_streams = video.streams.filter(only_audio=True)
        getId = video_streams.get_by_itag(250)
        subtype = 'webm'
        btntype = 'audio'
    if genre == 'audio/webm (160 kbps)':
        video_streams = video.streams.filter(only_audio=True)
        getId = video_streams.get_by_itag(251)
        subtype = 'webm'
        btntype = 'audio'

    if getId:
        getId.download(f"{link}")
        video_file = open(f"{link}{video.title}.{subtype}", "rb")
        video_bytes = video_file.read()

        st.video(video_bytes)

        video.title

    with open(f"{link}{video.title}.{subtype}", "rb") as file:
        btn = st.download_button(
            label=f"Download {btntype}",
            data=file,
            file_name=f"{video.title}.{subtype}",
        )
