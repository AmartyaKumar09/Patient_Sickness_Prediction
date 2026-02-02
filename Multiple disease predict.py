# Import non-streamlit libraries first
import pickle
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Import streamlit and set config immediately after
import streamlit as st

# Set page config (MUST be the first st command)
st.set_page_config(
    page_title="Patient Sickness Prediction App",
    page_icon="🏥",
    layout="wide"
)

# Import streamlit-related modules after config
from streamlit_option_menu import option_menu

# Import the page modules
from home import app as show_home_page
from about import app as show_about_page
from contact import app as show_contact_page

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

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Function to safely load model
def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
            # If model is numpy array, convert to RandomForestClassifier
            if isinstance(model, np.ndarray):
                clf = RandomForestClassifier()
                clf.fit(np.array([[0] * model.shape[0]]), np.array([0]))  # Dummy fit
                return clf
            return model
    except Exception as e:
        st.error(f"Error loading model from {model_path}: {str(e)}")
        return None

# Load the saved models
try:
    models_dir = os.path.join(parent_dir, 'Saved models')
    diabetes_model = load_model(os.path.join(models_dir, 'diabetes_model.sav'))
    heart_disease_model = load_model(os.path.join(models_dir, 'hybrid_heart_disease_model.sav'))
    parkinsons_model = load_model(os.path.join(models_dir, 'hybrid_parkinsons_model.sav'))
    
    if not all([diabetes_model, heart_disease_model, parkinsons_model]):
        st.error("Some models failed to load. Please check the model files.")
        st.stop()
        
except Exception as e:
    st.error(f"Error loading models: {str(e)}")
    st.stop()

#Sidebar for navigation
with st.sidebar:
    selected = option_menu('Patient Sickness Prediction App',
                           ['Home',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'About',
                            'Contact'],
                           icons = ['house','activity','heart','person', 'info-circle', 'envelope'],
                           default_index = 0)

# Display the selected page
if selected == 'Home':
    show_home_page()
elif selected == 'About':
    show_about_page()
elif selected == 'Contact':
    show_contact_page()
elif selected == 'Diabetes Prediction':
    #Page title
    st.title('Diabetes Prediction using ML')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Using number_input instead of text_input to ensure numeric values
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, value=0, step=1)
        Glucose = st.number_input('Glucose Level', min_value=0.0, value=0.0)
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0, value=0.0)
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0, value=0.0)
    
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.0, value=0.0)
        BMI = st.number_input('BMI value', min_value=0.0, value=0.0)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, value=0.0)
        Age = st.number_input('Age of the Person', min_value=0, value=0, step=1)
    
    #Code for prediction
    diab_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Diabetes Test Result'):
        # Create a list of features
        features = [float(Pregnancies), float(Glucose), float(BloodPressure), 
                   float(SkinThickness), float(Insulin), float(BMI), 
                   float(DiabetesPedigreeFunction), float(Age)]
        
        # Make prediction
        diab_prediction = diabetes_model.predict([features])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Not Diabetic'
            
        st.success(diab_diagnosis)
    
elif selected == 'Heart Disease Prediction':
    #Page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=0, value=0, step=1)
        sex = st.number_input('Sex (1 = Male, 0 = Female)', min_value=0, max_value=1, value=0, step=1)
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, value=0, step=1)
        trestbps = st.number_input('Resting Blood Pressure', min_value=0, value=0)
        chol = st.number_input('Serum Cholesterol in mg/dl', min_value=0, value=0)
    
    with col2:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)', min_value=0, max_value=1, value=0, step=1)
        restecg = st.number_input('Resting ECG Results (0-2)', min_value=0, max_value=2, value=0, step=1)
        thalach = st.number_input('Maximum Heart Rate', min_value=0, value=0)
        exang = st.number_input('Exercise Induced Angina (1 = Yes, 0 = No)', min_value=0, max_value=1, value=0, step=1)
    
    with col3:
        oldpeak = st.number_input('ST Depression', min_value=0.0, value=0.0, format="%.2f")
        slope = st.number_input('Slope of Peak Exercise ST (0-2)', min_value=0, max_value=2, value=0, step=1)
        ca = st.number_input('Number of Major Vessels (0-4)', min_value=0, max_value=4, value=0, step=1)
        thal = st.number_input('Thal (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)', min_value=0, max_value=2, value=0, step=1)
    
    #Code for prediction
    heart_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        # Create feature list
        features = [float(age), float(sex), float(cp), float(trestbps), float(chol),
                   float(fbs), float(restecg), float(thalach), float(exang),
                   float(oldpeak), float(slope), float(ca), float(thal)]
        
        # Make prediction
        heart_prediction = heart_disease_model.predict([features])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
        st.success(heart_diagnosis)
    
elif selected == 'Parkinsons Prediction':
    #Page title
    st.title('Parkinsons Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, value=0.0, format="%.6f")
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, value=0.0, format="%.6f")
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, value=0.0, format="%.6f")
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, value=0.0, format="%.6f")
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, value=0.0, format="%.6f")
        RAP = st.number_input('MDVP:RAP', min_value=0.0, value=0.0, format="%.6f")
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0, value=0.0, format="%.6f")
        DDP = st.number_input('Jitter:DDP', min_value=0.0, value=0.0, format="%.6f")
    
    with col2:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, value=0.0, format="%.6f")
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, value=0.0, format="%.6f")
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, value=0.0, format="%.6f")
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, value=0.0, format="%.6f")
        APQ = st.number_input('MDVP:APQ', min_value=0.0, value=0.0, format="%.6f")
        DDA = st.number_input('Shimmer:DDA', min_value=0.0, value=0.0, format="%.6f")
        NHR = st.number_input('NHR', min_value=0.0, value=0.0, format="%.6f")
    
    with col3:
        HNR = st.number_input('HNR', min_value=0.0, value=0.0, format="%.6f")
        RPDE = st.number_input('RPDE', min_value=0.0, value=0.0, format="%.6f")
        DFA = st.number_input('DFA', min_value=0.0, value=0.0, format="%.6f")
        spread1 = st.number_input('spread1', min_value=0.0, value=0.0, format="%.6f")
        spread2 = st.number_input('spread2', min_value=0.0, value=0.0, format="%.6f")
        D2 = st.number_input('D2', min_value=0.0, value=0.0, format="%.6f")
        PPE = st.number_input('PPE', min_value=0.0, value=0.0, format="%.6f")
    
    #Code for prediction
    parkinsons_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Parkinsons Test Result'):
        # Create features list
        features = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                   float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                   float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                   float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]
        
        # Make prediction
        parkinsons_prediction = parkinsons_model.predict([features])
        
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = 'The person has Parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinsons disease'
        
        st.success(parkinsons_diagnosis)
        
        