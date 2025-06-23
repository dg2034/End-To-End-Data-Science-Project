# End-To-End-Data-Science-Project

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: DEEP GHEEWALA

*INTERN ID*: CT04DF578

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

# 📰 Fake News Detection using Machine Learning (End-to-End Project)

This repository contains an end-to-end machine learning project that detects whether a news article is **REAL** or **FAKE** based on its content. The project includes everything from data preprocessing and model training to API development and deployment using Flask and Render.

---

## 📌 Project Overview

Fake news has become a serious issue in the digital age, influencing public perception and spreading misinformation. This project aims to build a machine learning model that classifies news articles as *real* or *fake*, and deploys this model via a simple API using Flask.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas, Scikit-learn**
- **TF-IDF Vectorizer**
- **Multinomial Naive Bayes Classifier**
- **Flask** (for serving the model)
- **Gunicorn** (for deployment)
- **Render** (for live API hosting)
- **Postman** (for API testing)

---

## 📁 Dataset Information

We used a publicly available dataset containing real and fake news articles:

- `True.csv` contains real news articles  
- `Fake.csv` contains fake news articles

📥 **NOTE:**  
The dataset files are **not included in this repository** due to size constraints.  
Please download them from Kaggle:  
🔗 https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset

Place the downloaded `True.csv` and `Fake.csv` in the project root directory before running the notebook.

---

## 💡 Project Workflow

1. **Data Collection & Labeling**: Real and fake articles are combined and labeled.
2. **Text Preprocessing**: TF-IDF vectorization is applied.
3. **Model Training**: A Multinomial Naive Bayes classifier is trained and evaluated.
4. **Model Saving**: The trained model and vectorizer are saved using `joblib`.
5. **API Development**: A Flask API is created with a `/predict` route.
6. **Deployment**: The app is deployed to Render with a public URL.

---

## 🚀 How to Run This Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/fake-news-detection-api.git
cd fake-news-detection-api
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

### 3. Download Dataset from Kaggle
Place True.csv and Fake.csv in the root directory.

### 4. Run the Notebook
a. Open task_3.ipynb and run all cells to:

b. Train the model

c. Save fake_news_model.pkl and tfidf_vectorizer.pkl

### 5. Run the Flask app
```bash
python app.py
```

### 6. Test with Postman or curl

Send a POST request to:
```bash
http://127.0.0.1:5000/predict
```

With JSON body:
```json
{
  "text": "NASA confirms existence of liquid water on Mars."
}
```

Response:
```json
{
  "prediction": "REAL"
}
```

### 7. 🌐 Live API Demo

The project is deployed on Render and publicly available at:
🔗 https://fake-news-detection-api-ksr0.onrender.com/

To test it, send a POST request to:

```bash
https://fake-news-detection-api-ksr0.onrender.com/predict
```

With this JSON body:

```json
{
  "text": "Aliens have landed in New York and started negotiations with government officials."
}
```

Response:
```json
{
  "prediction": "FAKE"
}
```
