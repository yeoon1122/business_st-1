import streamlit as st

st.title('첫번째 웹 어플 만들기')
st.write('#1. Markdown 텍스트 작성하기')

st.write('🌀')
st.write('# 마크다운 H1 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('')    #빈 줄 추가

st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.next()')
st.text('')

st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1 **굵게** 표시
    - 마크다운 목록 2 *기울임* 표시
        -마크다운 목록 2-1
        -마크다운 목록 2-2
    
    ## 마크다운 헤더 2
    -[네이버] (https://naver.com)
    -[구글] (https://google.com)
    '''
)

st.divider()

#형식이 있는 텍스트

st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

st.code('print("Hello, World!")', language='Python')
st.code('print("Hello, World!")', language='Python', line_numbers=True)

st.write(
    '''
    이것은 코드블럭입니다.
    ```cpp
    print("Hello, Python!")
    ```
    '''
)

st.write('##### 코드+결과 : st.echo()')
with st.echo():
    name = 'Chunghun Ha'
    st.write("Hello, Streamlit!", name)

    st.write('##### Latex 수식 작성: st.latex()')
    st.latex('\int_a^b f(x)dx')
    st.latex('\sum_a^b f(x)dx')
    st.latex('\sum_{k=1}^n f(x)dx')
    st.latex('\dfrac{\partial f}{\partial l}')
             
# %dffd% 를 쓰면 문자 가운데 수식을 넣을 수 있음

st.write('**색상 [문자열]** : 문자열에 색상을 적용')
'''#### 텍스트 색상 변경
    - :red[빨간색 텍스트]
'''

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
    )

st.line_chart(chart_data)

'#### :orange[st.map()]'
df = pd.DataFrame(
    np.random.randn(100,2) / [100,100] + [37.55, 126.92],
    columns=["lat", "lon"],
)
st.map(df)
