import streamlit as st
from datetime import datetime

st.title("スナップ写真撮影アプリ")

# カメラ入力ウィジェット
image = st.camera_input("カメラで撮影してください")

# 学科名、学籍番号、名前の入力欄
dept = st.text_input("学科名")
student_id = st.text_input("学籍番号")
name = st.text_input("名前")

if image is not None:
    # すべての情報が入力されているかチェック
    if dept and student_id and name:
        # タイムスタンプを利用してユニークなファイル名を生成
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # ファイル名例: "情報工学_123456_山田太郎_20250203_101530.png"
        filename = f"{dept}_{student_id}_{name}_{timestamp}.png"

        # 画像データの保存（image は BytesIO オブジェクト）
        with open(filename, "wb") as f:
            f.write(image.getvalue())

        st.success(f"写真を保存しました: {filename}")
    else:
        st.warning("学科名、学籍番号、名前をすべて入力してください。")
