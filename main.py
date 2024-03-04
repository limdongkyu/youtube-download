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
        raise ValueError('유효한 YouTube URL이 아닙니다.')
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(filename=output_path)

st.write("## 유튜브 영상 다운로드")


video_path = st.text_input(
        "Enter YouTube URL 👇",
        # label_visibility=st.session_state.visibility,
        # disabled=st.session_state.disabled,
        # placeholder=st.session_state.placeholder,
    )

if st.button('시작'):

    with st.spinner('잠시만 기다려주세요...'):
        
        download_youtube_video(video_path, output_path)
        with open(output_path, "rb") as file:    
            btn = st.download_button(
                    label="Download file",
                    data=file,
                    file_name=output_path,
                    mime="video/mp4"
                )
