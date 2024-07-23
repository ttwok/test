import streamlit as st

st.title('My title')
st.header('header')
st.subheader('subheader')
             
a =1
b =2
c = a+b

def write():
  st.write('Hello, world!!!!!!!!!!!!!!!!!')
  st.write(c)
  st.code(c)
  st.caption('안녕하세요')
  st.text('안녕하세요')
  return st.caption('안녕')
write()
'매직커맨드 방법'
'_매직커맨드 방법'
'매직:red[커맨드] 방법'
f'매직 :red[{c}] f-string 변수 호출'
