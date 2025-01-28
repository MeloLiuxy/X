import streamlit as st
import requests
import os
from streamlit_lottie import st_lottie

st.set_page_config(page_title="情侣网页", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_o6spyjnc.json")

# ---- 文件和留言设置 ----
留言文件 = "messages.json"


# 获取历史留言
def load_messages():
    if os.path.exists(留言文件):
        with open(留言文件, "r", encoding="utf-8") as f:
            return f.readlines()
    return []


# 保存留言
def save_message(user, message):
    with open(留言文件, "a", encoding="utf-8") as f:
        f.write(f"User: {user} - Message: {message}\n")


# -----------Header section------------
with st.container():
    st.subheader("🩷🩵👩🏽‍❤️‍👩🏻😻🌃")  # 更改为情侣介绍
    st.title("🐯🐍")
    st.write("每天！必须！多喜欢我一点！")

# ------------What We Do------------------


# ----------------------------My Message to You------------------

# ---- 留言功能 ----
with st.container():
    st.write("---")
    st.header("☁️😉")
    st.write("##")

    # 用户选择
    user = st.selectbox("选择留言人：", ["lxy", "yx"])

    # 留言
    user_message = st.text_area("今天想说什么🐱:", height=150)

    if st.button("点这里提交（最好是好听的话）💓👅"):
        if user_message:
            # 保存留言
            save_message(user, user_message)
            st.success("说出来的话不能撤回的!")

# ---- 显示历史留言 ----
with st.container():
    st.write("---")
    st.header("说了啥")
    st.write("##")

    messages = load_messages()
    if messages:
        for message in messages:
            st.write(message)
    else:
        st.write("No messages yet.")
