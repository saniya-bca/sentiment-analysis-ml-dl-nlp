# sentiment-analysis-ml-dl-nlp


This project is a **Sentiment Analysis System** that classifies text (movie reviews) as **Positive** or **Negative**.
It combines **Natural Language Processing (NLP)** and **Deep Learning (LSTM)** and is deployed as a web app using Streamlit.

---

## 🚀 Features

* Real-time sentiment prediction
* NLP-based text preprocessing
* Deep Learning model (LSTM)
* Interactive web app using Streamlit

---

## 📂 Dataset

* **IMDB Dataset of 50K Movie Reviews**
* Contains labeled movie reviews (Positive / Negative)

---

## 🧠 Technologies Used

* Python
* Pandas, NumPy
* NLTK
* TensorFlow / Keras (LSTM)
* Streamlit

---

## 🔍 Preprocessing Steps

* Lowercasing text
* Removing special characters
* Tokenization
* Stopword removal (with negation handling)

---

## 🤖 Model

* LSTM (Long Short-Term Memory)
* Captures context and sequence in text

---

## 📊 Model Performance

* Logistic Regression Accuracy: **88.5%**
* LSTM Accuracy: **86.4%**

---

## 🌐 Web App

The model is deployed using Streamlit where users can:

* Enter text
* Click **Predict**
* Get sentiment output (Positive / Negative)

---

## 📸 App preview

## (positive_output.png)
<img width="1463" height="542" alt="postive_output" src="https://github.com/user-attachments/assets/372799f8-a6aa-4328-9e06-35b000acfba0" />



## (negitive_output.png)
<img width="1376" height="532" alt="negitive_output" src="https://github.com/user-attachments/assets/e817979f-4c86-4744-952f-29047dbe459b" />

---

## ▶️ How to Run

1. Install dependencies:


pip install streamlit nltk tensorflow scikit-learn
```

2. Run the app:


streamlit run app.py
```

---

## 💡 Conclusion

This project demonstrates how NLP and Deep Learning can be used together to build a real-time sentiment analysis system. It also highlights that simpler ML models can sometimes outperform deep learning models depending on training conditions.

---
