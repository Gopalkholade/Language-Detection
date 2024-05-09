import pickle
import pandas as pd
import numpy as np
import streamlit as st
from helper_func import TextClean

model = pickle.load(open("./resources/model_pipe.pkl", "rb"))
label = pickle.load(open("./resources/label_enc.pkl", "rb"))


st.set_page_config("Language Detection")
st.header("Language Detection")

st.write("input text below: ")
text = st.text_area(label="Input text here")
if st.button("Predict"):
    response = model.predict([text])
    st.write(label.inverse_transform(response)[0])
