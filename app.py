import streamlit as st

st.title("hi")

option = st.selectbox(
'How would you like to be contacted?',
('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    
    

