import streamlit as st
import re

# 输入均值和标准差
def parse_input(value):
    match = re.match(r"(\d+(\.\d+)?)±(\d+(\.\d+)?)", value)
    if match:
        mean = float(match.group(1))
        std = float(match.group(3))
        return mean, std
    else:
        raise ValueError("输入格式错误，请使用 '均值±标准差' 格式")

# Streamlit 页面标题
st.title("Z分数比较计算器")

# 输入两个均值和标准差
input1 = st.text_input("请输入第一组数据的均值和标准差 (例如 179±12):")
input2 = st.text_input("请输入第二组数据的均值和标准差 (例如 180±15):")

# 如果两个输入都存在，进行计算
if input1 and input2:
    try:
        # 提取均值和标准差
        mean1, std1 = parse_input(input1)
        mean2, std2 = parse_input(input2)

        # 计算z分数
        z1 = (mean1 - mean1) / std1  # 对于均值的z分数
        z2 = (mean2 - mean2) / std2  # 对于均值的z分数

        # 显示结果
        st.write(f"第一组数据的z分数: {z1}")
        st.write(f"第二组数据的z分数: {z2}")

        # 比较两个z分数
        if z1 > z2:
            st.write("第一组数据的Z分数更大，表示第一组数据更偏离其均值。")
        elif z1 < z2:
            st.write("第二组数据的Z分数更大，表示第二组数据更偏离其均值。")
        else:
            st.write("两个数据点的Z分数相同，表示它们偏离各自均值的程度相同。")

    except ValueError as e:
        st.error(str(e))
