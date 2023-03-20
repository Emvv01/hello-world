import streamlit as st
import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import string
import nltk
from nltk.corpus import stopwords
lemmatizer = nltk.stem.WordNetLemmatizer()

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv('listings.csv')

st.title("hi")
