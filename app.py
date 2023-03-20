import streamlit as st

st.title("hi")

option = st.selectbox(
'How would you like to be contacted?',
('Email', 'Home phone', 'Mobile phone'))

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

st.write('You selected:', option)

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodby')
    


