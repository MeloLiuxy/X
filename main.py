import streamlit as st
import os

# 设置网页标题
st.set_page_config(page_title="情侣个人网页", page_icon="💑", layout="wide")

# 创建保存文件的目录
upload_dir = "uploaded_photos"
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

# 自定义蓝色和粉色配色的CSS样式
st.markdown("""
    <style>
    body {
        background-color: #1a1a1a;
        font-family: 'Press Start 2P', cursive;
        color: #FFFFFF;
    }
    .title {
        font-size: 36px;
        color: #FF69B4; /* 粉色 */
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
        text-shadow: 2px 2px #000000;
    }
    .subheader {
        font-size: 24px;
        color: #00BFFF; /* 蓝色 */
        margin-bottom: 20px;
        font-weight: bold;
        text-shadow: 1px 1px #000000;
    }
    .message {
        background-color: #333333;
        border: 3px solid #FF69B4; /* 粉色 */
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        font-size: 18px;
    }
    .button {
        background-color: #FF69B4; /* 粉色 */
        color: white;
        border: 3px solid #FF69B4; /* 粉色 */
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 18px;
        cursor: pointer;
        font-family: 'Press Start 2P', cursive;
        text-shadow: 1px 1px #000000;
    }
    .button:hover {
        background-color: #00BFFF; /* 蓝色 */
        color: #222222;
        border-color: #00BFFF; /* 蓝色 */
    }
    .card {
        background-color: #444444;
        border: 3px solid #FF69B4; /* 粉色 */
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        font-size: 18px;
    }
    .card img {
        width: 100%;
        border-radius: 10px;
    }
    .content-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 30px;
    }
    .content-item {
        width: 48%;
        background-color: #555555;
        padding: 20px;
        border-radius: 10px;
        border: 3px solid #FF69B4; /* 粉色 */
    }
    </style>
""", unsafe_allow_html=True)

# 显示网页标题
st.markdown('<div class="title">💑 欢迎来到我们的情侣个人网页 💑</div>', unsafe_allow_html=True)

# 内容区域
col1, col2 = st.columns([2, 1])

with col1:
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
            st.markdown('<div class="message">谢谢您的留言！我们会珍藏每一条祝福。</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="message">请留下你的祝福或留言！</div>', unsafe_allow_html=True)

with col2:
    # 显示互动性内容
    st.markdown('<div class="subheader">情侣小测试</div>', unsafe_allow_html=True)
    test_answer = st.radio("你们通常如何度过周末？", ("看电影", "旅行", "在家休息"))
    st.write(f"你们的选择是：{test_answer}")

# 瀑布流式布局内容展示
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# 展示爱情宣言
st.markdown("""
    <div class="content-item">
        <div class="card">
            <div class="subheader">我们的爱情宣言</div>
            1. 我们相互扶持，共同成长。<br>
            2. 爱是理解与包容，牵手走过每一个春夏秋冬。<br>
            3. 每一次微笑都是我们爱的见证。
        </div>
    </div>
""", unsafe_allow_html=True)

# 展示情侣活动推荐
st.markdown("""
    <div class="content-item">
        <div class="card">
            <div class="subheader">情侣活动推荐</div>
            - 一起看一部浪漫电影<br>
            - 去海边散步，享受宁静<br>
            - 参加情侣瑜伽，提升感情
        </div>
    </div>
""", unsafe_allow_html=True)

# 展示历史留言
st.markdown("""
    <div class="content-item">
        <div class="card">
            <div class="subheader">历史留言</div>
            如果有留言，将在这里展示。
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
