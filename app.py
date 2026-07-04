import streamlit as st

st.set_page_config(
    page_title="복싱 스타일 테스트",
    page_icon="🥊",
    layout="wide"
)

st.title("🥊 나는 어떤 복서일까?")

st.markdown("""
### 제출자 정보

- **학번:** 2020204074  
- **이름:** 김지형
""")

st.divider()

st.subheader("앱 소개")

st.write("""
이 앱은 복싱 수련자의 **경기 철학과 플레이 성향**을 분석하는 테스트 앱입니다.

단순히 '어떤 기술을 좋아하느냐'를 넘어서, MBTI처럼 여러 지표를 통해 
16가지 플레이 스타일(Archetype) 중 당신이 어디에 속하는지 진단해 드립니다.

왼쪽 사이드바에서 **Login 페이지**로 이동해 로그인한 뒤,
**Style Test 페이지**에서 약 24개의 심층 질문에 답변해 보세요.
""")

st.info("먼저 왼쪽 사이드바에서 Login 페이지로 이동하세요.")