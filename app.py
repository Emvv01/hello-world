import streamlit as st
import streamlit_extras

st.title("hi")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
