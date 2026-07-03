import streamlit as st

st.set_page_config(
    page_title="주짓수 스타일 테스트",
    page_icon="🥋",
    layout="wide"
)

st.title("🥋 주짓수 스타일 테스트 앱")

st.markdown("""
### 제출자 정보

- **학번:** 2020204074  
- **이름:** 김지형
""")

st.divider()

st.subheader("앱 소개")

st.write("""
이 앱은 사용자가 주짓수 상황별 질문에 답하면,
답변을 바탕으로 자신의 주짓수 스타일을 분석해주는 테스트 앱입니다.

왼쪽 사이드바에서 **Login 페이지**로 이동해 로그인한 뒤,
**Style Test 페이지**에서 퀴즈를 풀 수 있습니다.
""")

st.info("먼저 왼쪽 사이드바에서 Login 페이지로 이동하세요.")