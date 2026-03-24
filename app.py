import streamlit as st
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

# load model & tokenizer
model = pickle.load(open("model.pkl", "rb"))
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))

st.title("Sentiment Analysis App")

user_input = st.text_area("Enter your text:")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

def predict_sentiment(text):
    text = clean_text(text)
    seq = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(seq, maxlen=100)
    pred = model.predict(pad)[0][0]
    return "Positive 😊" if pred > 0.5 else "Negative 😠"

if st.button("Predict"):
    st.write("Sentiment:", predict_sentiment(user_input))