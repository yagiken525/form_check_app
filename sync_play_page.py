import streamlit as st
import os
import tempfile
import aws

def show_sync_play_page(SAVED_VIDEO_DIR):
    st.title("保存済み動画の同時再生")
    
    myaws = aws.MYAWS()

    # S3バケットから動画リストを取得
    response = myaws.s3_listobjects()
    saved_videos = [content['Key'] for content in response.get('Contents', [])]
    if not saved_videos:
        st.error("保存済み動画がありません。トリミングページで動画を保存してください。")
    else:
        st.header("保存済み動画を選択")
        selected_videos = st.multiselect("動画を選択", saved_videos)

        if selected_videos:
            st.header("選択した動画の同時再生")

            cols = st.columns(len(selected_videos))
            for idx, selected_video in enumerate(selected_videos):
                with cols[idx]:
                    st.write(selected_video)

                    # 動画をS3からダウンロード
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
                        myaws.s3_filedownload(selected_video, temp_video_file.name)

                        with open(temp_video_file.name, "rb") as f:
                            cols[idx].video(f.read(), format="video/mp4")