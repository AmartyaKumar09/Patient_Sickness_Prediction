import streamlit as st

def app():
    # Set the title of the page
    st.title("Patient Prediction App 🩺")

    # Introduction to Diseases
    st.markdown(
        """
        ## Disease Overview 

        This application focuses on three major diseases: Diabetes, Heart Disease, and Parkinson's. Each of these conditions has unique risk factors and symptoms, making early detection and management crucial for maintaining health.

        ### Common Causes of Each Disease 🏥:
        - **Diabetes 🩸**: 
          - High blood sugar levels over time can damage blood vessels and nerves.
          - Risk factors include obesity, sedentary lifestyle, and family history.
        - **Heart Disease 💖**: 
          - Factors such as high blood pressure, high cholesterol, smoking, and diabetes can increase the risk.
          - Lifestyle choices, including diet and exercise, play a significant role.
        - **Parkinson's Disease 🧠**: 
          - The exact cause is unknown, but genetic and environmental factors may contribute.
          - Symptoms often include tremors, stiffness, and difficulty with balance and coordination.
        """
    )

    # About the App
    st.markdown(
        """
        ## About This Application ��‍💻

        The **Unified Disease Prediction App** is a comprehensive tool designed to assess your risk for multiple diseases, including Diabetes, Heart Disease, and Parkinson's, using a single platform. It combines modern machine learning techniques with your personal health information to provide a holistic understanding of your health risks.

        ### Key Features ⚙️:
        - **Multi-Disease Risk Prediction 📊**: The app uses advanced algorithms trained on large datasets to predict your likelihood of having Diabetes, Heart Disease, or Parkinson's.
        - **Comprehensive Health Assessment 🏋️‍♂️🍏**: It evaluates your medical data and lifestyle choices to provide a complete picture of your health.
        - **Combined Risk Score 🧮**: The app generates a combined risk score by considering various health factors to help you better understand your overall risk.
        - **Early Detection 🕵️‍♂️**: By recognizing early signs of these diseases, you can take proactive steps to manage your health.

        ### How It Works ⚙️:
        1. **Medical Data 🩺**: The app requires information such as your BMI, blood pressure, cholesterol levels, and other relevant health markers to calculate your risk.
        2. **Lifestyle Input 🍏🍷**: You will also be asked to provide information about your smoking habits, drinking patterns, exercise routines, and diet.
        3. **Risk Calculation 💡**: After processing the inputs, the app provides:
           - **Disease Probability 🏥**: A percentage indicating your likelihood of having one of the diseases.
           - **Lifestyle Risk Score ⚖️**: A score reflecting the impact of your lifestyle choices on your health.
           - **Combined Risk 🧮**: A final score that combines both your medical and lifestyle risks to give you a comprehensive view of your health status.

        This holistic approach ensures that you're not just looking at your medical history but also at the day-to-day habits that contribute to your overall health.

        ### Technology Behind the App 💻:
        The app uses machine learning models to analyze the input data. These models have been trained on large datasets that include various medical and lifestyle factors. By utilizing predictive algorithms, the app can provide an accurate assessment of your risk for multiple diseases based on the data you provide.
        """
    )

    # Why Early Detection Matters
    st.markdown(
        """
        ## Why Early Detection is Crucial ⏳

        **Early detection** of these diseases is vital because it allows for timely intervention, which can significantly slow down the progression of the conditions. In the early stages, these diseases can often be managed with lifestyle changes and medications.

        ### Benefits of Early Detection ✅:
        - **Prevention of Complications 🚫**: Early detection can help prevent severe complications associated with each disease.
        - **Better Management of Risk Factors ⚖️**: Early diagnosis allows healthcare providers to address underlying conditions that contribute to these diseases.
        - **Improved Quality of Life 🌟**: Catching these diseases early can help maintain an active and healthy lifestyle.
        - **Reduced Healthcare Costs 💰**: Addressing these diseases early can prevent expensive treatments that may be required in advanced stages.

        **Remember**, even if you do not show symptoms, regular screenings for these diseases are important if you have risk factors like family history or lifestyle choices.

        ### What You Can Do 🏃‍♀️:
        - **Monitor your health 🩺**: Regular checkups and lab tests can help detect these diseases before symptoms appear.
        - **Adopt a healthy lifestyle 🍏**: Managing your weight, quitting smoking 🚭, limiting alcohol intake 🍷, and eating a balanced diet can help protect your health.
        - **Follow medical advice 👨‍⚕️**: If diagnosed with any of these diseases, work closely with your healthcare provider to manage the condition and slow its progression.
        """
    )

    # Disclaimer
    st.markdown(
        """
        ---
        ## Disclaimer ⚠️
        The Disease Prediction App is an educational tool and should not replace medical advice. The results provided by this app are based on algorithms and predictive models that estimate the likelihood of Diabetes, Heart Disease, and Parkinson's. Please consult with a healthcare professional for a thorough evaluation and diagnosis. 

        The app aims to help individuals become more aware of their health, but it is not intended to diagnose or treat any medical condition. Always seek the guidance of your physician or other qualified health provider with any questions you may have regarding your health.
        """
    )

    # Footer
    st.markdown("---")
    st.markdown("© 2025 Patient Sickness Prediction App | Developed with ❤️ by Amartya Kumar and Team.")

# Run the app only if the script is executed directly
if __name__ == "__main__":
    app()
