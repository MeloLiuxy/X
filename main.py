import streamlit as st
import os
import streamlit.components.v1 as components

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
        margin: 0;
        font-family: 'Press Start 2P', cursive;
        color: #FFFFFF;
        overflow: hidden;
    }
    .title {
        font-size: 36px;
        color: #FF69B4; /* 粉色 */
        text-align: center;
        margin-top: 50px;
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

# 粒子效果的 HTML 和 JS
particle_effect_html = """
<!DOCTYPE html>
<html>
<head>
    <title>高级粒子效果</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background: #000;
        }
        canvas {
            display: block;
        }
    </style>
</head>
<body>
    <canvas id="canvas"></canvas>

    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        
        function resize() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resize();
        window.addEventListener('resize', resize);

        const particles = [];
        const particleCount = 100;
        const mouse = { x: null, y: null };

        class Particle {
            constructor() {
                this.reset();
                this.baseSize = 2;
            }

            reset() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.vx = -1 + Math.random() * 2;
                this.vy = -1 + Math.random() * 2;
                this.radius = this.baseSize + Math.random() * 2;
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = `hsl(${(this.x/canvas.width)*360}, 70%, 50%)`;
                ctx.fill();
            }

            update() {
                const dx = mouse.x - this.x;
                const dy = mouse.y - this.y;
                const distance = Math.sqrt(dx*dx + dy*dy);
                const force = (canvas.width/2 - distance) / canvas.width/2;

                if (distance < canvas.width/2) {
                    this.x += dx * force * 0.1;
                    this.y += dy * force * 0.1;
                }

                this.x += this.vx;
                this.y += this.vy;

                if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
                if (this.y < 0 || this.y > canvas.height) this.vy *= -1;

                this.radius = this.baseSize + Math.abs(Math.sin(Date.now()*0.001 + this.x)) * 2;
            }
        }

        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }

        canvas.addEventListener('mousemove', (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        });

        function animate() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            particles.forEach((p1, i) => {
                p1.update();
                p1.draw();

                particles.slice(i).forEach(p2 => {
                    const dx = p1.x - p2.x;
                    const dy = p1.y - p2.y;
                    const distance = Math.sqrt(dx*dx + dy*dy);

                    if (distance < 100) {
                        ctx.beginPath();
                        ctx.strokeStyle = `hsl(${(i/particleCount)*360}, 70%, 50%)`;
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(p1.x, p1.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.stroke();
                    }
                });
            });

            requestAnimationFrame(animate);
        }

        animate();
    </script>
</body>
</html>
"""

# 将粒子效果嵌入到Streamlit中
components.html(particle_effect_html, height=700)

# 显示网页标题
st.markdown('<div class="title">💑 欢迎来到我们的情侣个人网页 💑</div>', unsafe_allow_html=True)

# 内容区域
col1, col2 = st.columns([2, 1])

with col1:
    # 显示个人简介
    st.markdown('<div class="subheader">2025</div>', unsafe_allow_html=True)
    st.write("继续爱我")

    # 上传情侣合照
    st.markdown('<div class="subheader">上传想上传的上传</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("选择一张照片上传", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # 将图片保存到指定目录
        file_path = os.path.join(upload_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(file_path, caption="上传想上传的上传", use_column_width=True)

    # 留言板功能
    st.markdown('<div class="subheader">想说的话</div>', unsafe_allow_html=True)
    message = st.text_area("在这里写：", key="message")
    if st.button("提交留言", key="submit_button"):
        if message:
            # 将留言保存到文件
            with open("messages.txt", "a", encoding="utf-8") as msg_file:
                msg_file.write(f"{message}\n")
            st.markdown('<div class="message">嗯呐~</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="message">写啊！</div>', unsafe_allow_html=True)



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
