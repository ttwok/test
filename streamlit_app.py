import streamlit as st

st.title('My Streamlit App')
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
write()
