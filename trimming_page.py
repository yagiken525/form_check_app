import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import base64
import boto3
import aws

def show_trimming_page(SAVED_VIDEO_DIR):

    myaws = aws.MYAWS()
    st.title("動画トリミングアプリ")

    uploaded_file = st.file_uploader("動画ファイルを選択してください (.mp4, .avi, .mov, .mkvなど)", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_file.read())
        video = VideoFileClip(tfile.name)

        with open(tfile.name, "rb") as f:
            st.video(f.read(), format="video/mp4")

        start_time = st.slider("開始時間 (秒)", 0, int(video.duration), 0)
        end_time = st.slider("終了時間 (秒)", 0, int(video.duration), int(video.duration))

        if st.button("動画をトリミング"):
            if start_time < end_time:
                trimmed_video = video.subclip(start_time, end_time)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
                    trimmed_video.write_videofile(temp_video_file.name, codec="libx264")

                    # 動画をS3にアップロード
                    s3_filename = f"trimmed_video_{start_time}-{end_time}.mp4"
                    filename = myaws.s3_fileupload(temp_video_file.name, s3_filename)
                    st.success(f"動画を {filename} として保存しました。")

                    with open(temp_video_file.name, "rb") as f:
                        st.video(f.read(), format="video/mp4")
            else:
                st.error("終了時間は開始時間より後にしてください。")

        tfile.close()
