import streamlit as st

# 设置网页标题
st.set_page_config(page_title="情侣个人网页", page_icon="💑", layout="centered")

# 显示网页标题
st.title("💑 欢迎来到我们的情侣个人网页 💑")

# 显示一个个人简介
st.subheader("关于我们")
st.write("我们是两位热爱生活、喜欢旅行、共同成长的情侣！")

# 上传情侣合照
st.subheader("我们的合照")
st.image("path_to_your_photo.jpg", caption="我们的合照", use_column_width=True)

# 显示一些爱情宣言
st.subheader("我们的爱情宣言")
st.write("""
    1. 我们相互扶持，共同成长。
    2. 爱是理解与包容，牵手走过每一个春夏秋冬。
    3. 每一次微笑都是我们爱的见证。
""")

# 提供一个留言板
st.subheader("留言给我们")
message = st.text_area("写下你的祝福或留言：")
if st.button("提交留言"):
    if message:
        st.write("谢谢您的留言！我们会珍藏每一条祝福。")
    else:
        st.write("请留下你的祝福或留言！")

# 展示情侣活动推荐
st.subheader("情侣活动推荐")
st.write("""
    - 一起看一部浪漫电影
    - 去海边散步，享受宁静
    - 参加情侣瑜伽，提升感情
""")

# 添加一些互动内容
st.subheader("情侣小测试")
test_answer = st.radio("你们通常如何度过周末？", ("看电影", "旅行", "在家休息"))
st.write(f"你们的选择是：{test_answer}")
