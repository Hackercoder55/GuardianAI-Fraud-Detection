# 🛡️ GuardianAI: E-Commerce Fraud Detection System

**Team Name:** Expo_Ranker
**Track:** E-Commerce Fraud Detection
**Event:** Manthan AI Hackathon 2025

## 📌 Project Overview
GuardianAI is a Machine Learning-powered engine designed to detect fraudulent transactions in real-time. It solves the problem of "Class Imbalance" in financial datasets using SMOTE and utilizes a Random Forest Classifier to identify high-risk behaviors (high transaction velocity, suspicious device usage, etc.).

## 🛠️ Tech Stack
* **Training:** Python, Scikit-Learn, Pandas, SMOTE (Imbalanced-Learn).
* **Environment:** Kaggle Notebooks (GPU accelerated).
* **Application:** Streamlit (for the interactive dashboard).
* **Model:** Random Forest Classifier.

## ⚙️ How It Works
1.  **Data Processing:** The system takes raw transaction data and handles missing values.
2.  **Balancing:** We applied **SMOTE** to balance the dataset (originally ~1% fraud).
3.  **Prediction:** The trained model analyzes 30+ features to output a `Fraud Probability Score`.

## 🚀 How to Run Locally

1.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 📊 Results
* **Recall:** High sensitivity to fraud cases (minimized false negatives).
Clean Transaction:

* <img width="781" height="977" alt="image" src="https://github.com/user-attachments/assets/27b0701e-11dd-401b-8db3-4d520bdf2e0b" />
Fraud Detected:

<img width="722" height="874" alt="image" src="https://github.com/user-attachments/assets/ac2c9b74-51eb-47ae-a271-b6934d1fff53" />




* **Precision:** Optimized to reduce false alarms for genuine users.
