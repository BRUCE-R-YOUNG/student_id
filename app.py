import streamlit as st
from datetime import datetime

st.title("スナップ写真撮影アプリ")

image = st.camera_input("カメラで撮影してください")

dept = st.text_input("学科名")
student_id = st.text_input("学籍番号")
name = st.text_input("名前")

if image is not None:
    if dept and student_id and name:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{dept}_{student_id}_{name}_{timestamp}.png"

        with open(filename, "wb") as f:
            f.write(image.getvalue())

        st.success(f"写真を保存しました: {filename}")
    else:
        st.warning("学科名、学籍番号、名前をすべて入力してください。")
