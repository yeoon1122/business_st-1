import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image

st.title('배스킨라빈스 Baskin Robbins')
img = Image.open('배라logo.PNG')
st.image(img, width=100)
st.write('배스킨라빈스는 다양한 맛으로 유명한 아이스크림 브랜드입니다 🍨.')
st.markdown('[배스킨라빈스 코리아](https://www.baskinrobbins.co.kr)')
st.divider()

st.subheader('1. 배스킨라빈스의 역사')
st.markdown('1945년 어바인 리반스(''Irvine Robbins)와 버트 배스킨(Bust Baskin)이 ' \
'설립한 다국적 아이스크림 브랜드로, 로고에 적힌 31은 한 달 내내 매일 1가지씩 ' \
' 수 있는 다양한 맛을 갖추었다는 의미를 담고 있다.')
st.write('')

st.subheader('2. 아이스크림 사이즈')
st.markdown('**1) 콘/컵**으로 제공되는 아이스크림')
st.markdown('->  싱글레귤러 / 싱글킹 / 더블주니어 / 더블레귤러')
st.warning('이 4종류의 아이스크림은 뚜껑이나 포장이 제공되지 않는다!')
st.markdown('**2) 핸드팩**으로 제공되는 아이스크림')
st.markdown('->  파인트(3가지 맛) / 쿼터(4가지 맛) / 패밀리(5가지 맛) / 하프갤런(6가지 맛)')
st.markdown('**3) 박스** (싱글레귤러)으로 제공되는 아이스크림')
st.markdown('->  아빠왔다팩(4가지 맛) / 버라이어티팩(6가지 맛)'
'/ 옹기종기팩(8가지 맛) / 핸드팩 세트(12가지 맛)')
st.write('')

st.subheader('3. 플레이버')
st.text('약 20가지의 상시 플레이버가 있다. (매장별상이)')
st.text('31요거트 / 그린티 / 레인보우 샤베트 / 민트 초콜릿 칩 / 베리베리 스트로베리 / ' \
'바닐라 / 바람과 함께 사라지다 / 슈팅스타 / 아몬드 봉봉 / 엄마는 외계인 / 자모카 아몬드 훠지 /' \
'뉴욕 치즈 케이크 / 체리 쥬빌레 / 초콜릿 / 초콜릿 무스 / 쿠키 앤 크림 / 피스타치오 아몬드 /' \
'이상한 나라의 솜사탕')

st.subheader('4. SPC')
img = Image.open('spclogo.PNG')
st.image(img, width=100)
st.markdown('배스킨라빈스는 대한민국 제빵업계의 선두주자인 SPC계열 업체이다.')
st.write('')
st.markdown('_**<SPC의 월별 주가>**_')

plt.figure(figsize=(10, 5))
plt.plot(['3', '4', '5', '6'],[50500, 61100, 63400, 53100],
         c="b", lw=3, ls="-")
plt.xlabel('월')
plt.ylabel('주가')
plt.rc('font', family='Malgun Gothic')
plt.yticks(range(50000, 65001, 5000))
st.pyplot(plt)