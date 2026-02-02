# 🏥 Patient Sickness Prediction App

A comprehensive Machine Learning web application built with Python and Streamlit to predict the likelihood of multiple diseases (Diabetes, Heart Disease, and Parkinson's).

![App Interface](https://github.com/AmartyaKumar09/Patient_Sickness_Prediction/blob/main/images/Screenshot%202025-04-28%20205249.png?raw=true)

## 📋 Overview

This project utilizes **Machine Learning models** trained on medical datasets to classify patients. The application provides an interactive interface where users can input health parameters and receive instant predictions. 

Uniquely, this application also visualizes **model performance metrics** (Confusion Matrix and Precision-Recall Curves) in real-time using test data, providing transparency into the model's accuracy.

### 🔍 Supported Predictions
1.  **Diabetes Prediction:** Uses Support Vector Machine (SVM) to analyze glucose, insulin, BMI, etc.
2.  **Heart Disease Prediction:** Uses a **Hybrid Model** to analyze chest pain, cholesterol, and resting BP.
3.  **Parkinson's Prediction:** Uses a **Hybrid Model** to examine vocal frequency variations (MDVP).

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) with `streamlit-option-menu` for navigation.
* **Data Manipulation:** Pandas, NumPy.
* **Machine Learning:** Scikit-Learn (SVM, Logistic Regression).
* **Visualization:** Matplotlib, Seaborn (for heatmaps and PR curves).
* **Model Storage:** Pickle.

## 📂 Project Structure

```text
MULTIPLE DISEASE PREDICTION/
├── Datasets/                   # Original CSV datasets
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
├── Saved models/               # Trained models & Test data
│   ├── diabetes_model.sav
│   ├── diabetes_test_data.pkl  # Used for live visualization
│   ├── hybrid_heart_disease_model.sav
│   ├── hybrid_parkinsons_model.sav
│   └── [other .pkl files]
├── about.py                    # About page logic
├── contact.py                  # Contact page logic
├── home.py                     # Homepage logic
├── main.py                     # Main application entry point
├── Multiple disease predict.py # Training/Logic script
├── Diabetes.ipynb              # Jupyter Notebook for training
└── README.md
```

## 🧠 Model & Visualization Details

The application loads pre-trained models from the `Saved models/` directory. 

**Key Features in `main.py`:**
* **Dynamic Backgrounds:** Custom CSS is injected to provide a visually appealing medical theme.
* **Live Metrics:** When a prediction is made, the app loads `_test_data.pkl` files to plot the **Confusion Matrix** and **Precision-Recall Curve** on the fly, allowing users to see how reliable the model is.

## 📝 Usage

1.  Use the **Sidebar** to navigate between Home, About, Contact, or specific Disease Predictions.
2.  **Select a Disease** (e.g., Diabetes).
3.  **Input Health Data:** Enter values for fields like *Glucose*, *Blood Pressure*, *BMI*, etc.
4.  Click **Predict**.
5.  View the result (e.g., "Diabetic" or "Not Diabetic") and scroll down to see the visual performance graphs.

## 👤 Author

**[Your Name]**
* GitHub: [@AmartyaKumar09](https://github.com/AmartyaKumar09)
* LinkedIn: [amartyakumar09](https://www.linkedin.com/in/amartyakumar09/)

---
*Disclaimer: This project is for educational purposes only and is not a substitute for professional medical diagnosis.*
