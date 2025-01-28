import streamlit as st
import os

# 设置网页标题
st.set_page_config(page_title="情侣个人网页", page_icon="💑", layout="centered")

# 创建保存文件的目录
upload_dir = "uploaded_photos"
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

# 自定义CSS样式
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 36px;
        color: #FF69B4;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 24px;
        color: #FF1493;
    }
    .message {
        background-color: #FFF0F5;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .message-text {
        font-size: 18px;
        color: #8B008B;
    }
    .button {
        background-color: #FF1493;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #FF69B4;
    }
    </style>
""", unsafe_allow_html=True)

# 显示网页标题
st.markdown('<div class="title">💑 欢迎来到我们的情侣个人网页 💑</div>', unsafe_allow_html=True)

# 显示个人简介
st.markdown('<div class="subheader">关于我们</div>', unsafe_allow_html=True)
st.write("我们是两位热爱生活、喜欢旅行、共同成长的情侣！")

# 上传情侣合照
st.markdown('<div class="subheader">上传我们的合照</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("选择一张照片上传", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # 将图片保存到指定目录
    file_path = os.path.join(upload_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(file_path, caption="我们的合照", use_column_width=True)

# 留言板功能
st.markdown('<div class="subheader">留言给我们</div>', unsafe_allow_html=True)
message = st.text_area("写下你的祝福或留言：", key="message")
if st.button("提交留言", key="submit_button"):
    if message:
        # 将留言保存到文件
        with open("messages.txt", "a", encoding="utf-8") as msg_file:
            msg_file.write(f"{message}\n")
        st.markdown('<div class="message"><div class="message-text">谢谢您的留言！我们会珍藏每一条祝福。</div></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="message"><div class="message-text">请留下你的祝福或留言！</div></div>', unsafe_allow_html=True)

# 显示留言内容
st.markdown('<div class="subheader">历史留言</div>', unsafe_allow_html=True)
if os.path.exists("messages.txt"):
    with open("messages.txt", "r", encoding="utf-8") as msg_file:
        messages = msg_file.readlines()
        if messages:
            for msg in messages:
                st.write(f"- {msg.strip()}")
        else:
            st.write("暂无留言。")
else:
    st.write("暂无留言。")

# 显示一些爱情宣言
st.markdown('<div class="subheader">我们的爱情宣言</div>', unsafe_allow_html=True)
st.write("""
    1. 我们相互扶持，共同成长。
    2. 爱是理解与包容，牵手走过每一个春夏秋冬。
    3. 每一次微笑都是我们爱的见证。
""")

# 展示情侣活动推荐
st.markdown('<div class="subheader">情侣活动推荐</div>', unsafe_allow_html=True)
st.write("""
    - 一起看一部浪漫电影
    - 去海边散步，享受宁静
    - 参加情侣瑜伽，提升感情
""")

# 添加一些互动内容
st.markdown('<div class="subheader">情侣小测试</div>', unsafe_allow_html=True)
test_answer = st.radio("你们通常如何度过周末？", ("看电影", "旅行", "在家休息"))
st.write(f"你们的选择是：{test_answer}")

# 调整页面布局为两列
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://via.placeholder.com/300", caption="浪漫时刻", use_column_width=True)
    
with col2:
    st.write("在我们的生活中，记录每一个浪漫时刻，珍惜每一次相伴的时光！")
