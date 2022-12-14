import streamlit as st
from pytube import YouTube



link = "https://github.com/tugasbesardaspro/tubesdaspro/tree/main/components/youtube_downloader/"

st.image(f'./components/youtube_downloader/yt.png',use_column_width=True)
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
        getId.download(f"{link}download")        
        video_file = open(f"{link}download/{video.title}.{subtype}", "rb")
        video_bytes = video_file.read()

        st.video(video_bytes)
        
        video.title

    with open(f"{link}download/{video.title}.{subtype}", "rb") as file:
        btn = st.download_button(
                label=f"Download {btntype}",
                data=file,
                file_name=f"{video.title}.{subtype}",            
            )