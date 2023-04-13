import streamlit as st
import os
from trimming_page import show_trimming_page
from sync_play_page import show_sync_play_page

st.set_page_config(page_title="動画トリミングアプリ", layout="wide")

SAVED_VIDEO_DIR = "saved_videos"
if not os.path.exists(SAVED_VIDEO_DIR):
    os.makedirs(SAVED_VIDEO_DIR)

page = st.sidebar.selectbox("ページを選択", ["トリミング", "同時再生"])

if page == "トリミング":
    show_trimming_page(SAVED_VIDEO_DIR)
elif page == "同時再生":
    show_sync_play_page(SAVED_VIDEO_DIR)
