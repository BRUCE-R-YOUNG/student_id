import streamlit as st
from datetime import datetime
import os

st.title("スナップ写真撮影アプリ")

# 学科の選択（プルダウン）
departments = [
    "",
    "建築監督科",
    "建築科",
    "インテリア科",
    "情報処理科",
    "IoT+AI科",
    "DS+AI科",
    "ゲームプログラミング科",
    "Web動画クリエイター科",
    "環境テクノロジー科",
    "バイオテクノロジー科"
]
dept = st.selectbox("学科を選択してください", departments)

student_id = st.text_input("学籍番号")
name = st.text_input("名前")

image = st.camera_input("カメラで撮影してください")

if image is not None:
    if student_id and name:
        # 現在時刻を利用してユニークなファイル名を生成
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{dept}_{student_id}_{name}_{timestamp}.png"

        # 学科ごとにディレクトリを作成（存在しない場合）
        save_dir = os.path.join("photos", dept)
        os.makedirs(save_dir, exist_ok=True)

        # 保存先のパス
        save_path = os.path.join(save_dir, filename)

        # 画像データの保存（image は BytesIO オブジェクト）
        with open(save_path, "wb") as f:
            f.write(image.getvalue())

        st.success(f"写真を保存しました: {save_path}")
    else:
        st.warning("学籍番号と名前を入力してください。")
