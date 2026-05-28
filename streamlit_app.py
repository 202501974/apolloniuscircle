import streamlit as st

st.title("아폴로니우스의 원 그리기")

st.write("아폴로니우스의 원은 두 고정점 A, B에 대해 PA : PB = m : n을 만족하는 점 P의 자취입니다.")

col1, col2 = st.columns(2)
with col1:
    st.text_input("비율 m", value="2", placeholder="예: 2")
with col2:
    st.text_input("비율 n", value="1", placeholder="예: 1")

st.caption("이 두 비율을 입력하면 A, B 사이의 아폴로니우스의 원을 시각적으로 확인할 수 있습니다.")
