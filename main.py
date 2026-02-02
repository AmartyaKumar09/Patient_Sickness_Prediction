import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc
import streamlit as st
from streamlit_option_menu import option_menu

from home import app as show_home_page
from about import app as show_about_page
from contact import app as show_contact_page

st.set_page_config(
    page_title="Patient Sickness Prediction App",
    page_icon="🏥",
    layout="wide"
)
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGRhcmt8ZW58MHx8MHx8fDA%3D");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
background-size: cover;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://images.unsplash.com/photo-1637775297458-7443ffd545b2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YmxhY2t8ZW58MHx8MHx8fDA%3D");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
models_dir = os.path.join(os.path.dirname(__file__), 'Saved models')

def load_model(model_path):
    if not os.path.exists(model_path):
        st.error(f"Model file missing: {model_path}")
        st.stop()
    with open(model_path, 'rb') as file:
        return pickle.load(file)

def load_test_data(file_name):
    file_path = os.path.join(models_dir, file_name)
    if not os.path.exists(file_path):
        st.error(f"❌ Missing test data file: {file_name}")
        st.stop()
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Load models + test data
diabetes_model = load_model(os.path.join(models_dir, 'diabetes_model.sav'))
diabetes_X_test, diabetes_y_test = load_test_data('diabetes_test_data.pkl')

heart_model = load_model(os.path.join(models_dir, 'hybrid_heart_disease_model.sav'))
heart_X_test, heart_y_test = load_test_data('heart_test_data.pkl')

parkinsons_model = load_model(os.path.join(models_dir, 'hybrid_parkinsons_model.sav'))
parkinsons_X_test, parkinsons_y_test = load_test_data('parkinsons_test_data.pkl')

# Sidebar
with st.sidebar:
    selected = option_menu('Patient Sickness Prediction App',
                           ['Home', 'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'About', 'Contact'],
                           icons=['house', 'activity', 'heart', 'person', 'info-circle', 'envelope'],
                           default_index=0)

# Confusion Matrix & PR Curve
def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    st.pyplot(fig)

def plot_pr_curve(y_test, y_probs):
    precision, recall, _ = precision_recall_curve(y_test, y_probs)
    pr_auc = auc(recall, precision)
    fig, ax = plt.subplots()
    ax.plot(recall, precision, label=f'PR Curve (AUC = {pr_auc:.2f})', color='green')
    ax.legend()
    st.pyplot(fig)

if selected == 'Home':
    show_home_page()

elif selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')
    Pregnancies = st.number_input('Pregnancies', 0)
    Glucose = st.number_input('Glucose', 0)
    BloodPressure = st.number_input('BloodPressure', 0)
    SkinThickness = st.number_input('SkinThickness', 0)
    Insulin = st.number_input('Insulin', 0)
    BMI = st.number_input('BMI', 0.0)
    DPF = st.number_input('DiabetesPedigreeFunction', 0.0)
    Age = st.number_input('Age', 0)

    if st.button('Predict Diabetes'):
        X_input = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]]
        result = diabetes_model.predict(X_input)[0]
        st.success('Diabetic' if result else 'Not Diabetic')

        # Show Metrics
        y_probs = diabetes_model.predict_proba(diabetes_X_test)[:, 1]
        y_preds = diabetes_model.predict(diabetes_X_test)
        st.subheader("Confusion Matrix")
        plot_confusion_matrix(diabetes_y_test, y_preds)
        st.subheader("Precision-Recall Curve")
        plot_pr_curve(diabetes_y_test, y_probs)

# (Repeat similarly for Heart & Parkinson's Prediction)

elif selected == 'About':
    show_about_page()

elif selected == 'Contact':
    show_contact_page()
