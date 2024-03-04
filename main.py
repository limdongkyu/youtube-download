import re

import streamlit as st
from pytube import YouTube



output_path = 'output.mp4'


def is_valid_youtube_url(url):
    # YouTube URL을 확인하기 위한 정규 표현식 패턴
    youtube_url_pattern = re.compile(
        r'(https?://)?(www\.)?'
        '(youtube\.com/watch\?v=|youtu\.be/)'
        '[A-Za-z0-9_-]{11}'
    )
    
    return bool(youtube_url_pattern.match(url))


def download_youtube_video(url, output_path):
    if not is_valid_youtube_url(url):
        raise ValueError('This is not a valid YouTube URL.')
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(filename=output_path)

st.write("## Download a YouTube video")


video_path = st.text_input(
        "Enter YouTube URL 👇",
        # label_visibility=st.session_state.visibility,
        # disabled=st.session_state.disabled,
        # placeholder=st.session_state.placeholder,
    )

if st.button('시작'):

    with st.spinner('Please wait a moment...'):
        
        download_youtube_video(video_path, output_path)
        with open(output_path, "rb") as file:    
            btn = st.download_button(
                    label="Download file",
                    data=file,
                    file_name=output_path,
                    mime="video/mp4"
                )

st.title("Let's all live together.!")


ko_fi_button_html = '''
<a href='https://ko-fi.com/J3J2V8EYP' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
'''
st.markdown(ko_fi_button_html, unsafe_allow_html=True)
