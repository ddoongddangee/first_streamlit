import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 로그인")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

USER_ID = "boxer"
USER_PW = "1234"

st.write("테스트용 계정")
st.code("ID: boxer\nPW: 1234")

user_id = st.text_input("아이디")
user_pw = st.text_input("비밀번호", type="password")

if st.button("로그인"):
    if user_id == USER_ID and user_pw == USER_PW:
        st.session_state.logged_in = True
        st.session_state.username = user_id
        st.success("로그인 성공!")
    else:
        st.session_state.logged_in = False
        st.error("아이디 또는 비밀번호가 틀렸습니다.")

if st.session_state.logged_in:
    st.info(f"현재 로그인 상태입니다. 사용자: {st.session_state.username}")

    if st.button("로그아웃"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("로그아웃되었습니다.")