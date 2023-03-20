import streamlit as st

st.title("hi")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    
    
option = st.selectbox(
'How would you like to be contacted?',
('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
