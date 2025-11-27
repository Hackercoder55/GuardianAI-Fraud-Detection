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
1.  **Clone the Repository**
    ```bash
    git clone [Your-GitHub-Link-Here]
    cd Manthan_Fraud_Detection
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 📊 Results
* **Recall:** High sensitivity to fraud cases (minimized false negatives).
* **Precision:** Optimized to reduce false alarms for genuine users.