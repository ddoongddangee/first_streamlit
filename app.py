import  streamlit as st
import pandas as pd
import numpy as np

#페이지 설정
st.set_page_config(
    page_title="My first Streamlit App",
    page_icon=":tada:",
    layout="wide",
    initial_sidebar_state="expanded"
)

#제목과 소개
st.title("환영합니다! :wave:")
st.markdown('## streamlit 어플리케이션')

st.write("""이앱은 STREAMLIT의 기본 기능을 보여줍니다.
        아래에서 다양한 요소들을 확인헤보세요""")

#사이드바
st.sidebar.header("사이드바 메뉴")
option = st.sidebar.selectbox(
    '원하는 기능을 선택하세요',
    ['데이터 보기', '차트 보기', '정보']
)



#샘플 데이터 생성

if option == '데이터 보기':
    st.header("샘플 데이터")
    data = pd.DataFrame({
        '이름' : ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        '나이' : [25, 30, 35, 40, 45],
        '점수' : [85, 90, 95, 80, 70]
    })
    st.dataframe(data)
    
elif option == '차트 보기':
    st.header("샘플 차트")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)

elif option == '정보':
    st.header("정보")
    st.info("이 앱은 Streamlit을 사용하여 만들어졌습니다.")
    st.balloons()