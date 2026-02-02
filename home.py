import streamlit as st


def app():
    
    # Set the title with a larger, bolder heading
    st.title("**Patient Sickness Prediction App** 🩺")

    # Introduction to Diseases
    st.markdown(
        """
        ## Disease Overview 🩺

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

    # Footer with a simple, encouraging note
    st.markdown("---")
    st.markdown("© 2025 Patient Sickness Prediction App | Made with ❤️ by Amartya Kumar and Team")

# Run the app only if the script is executed directly
if __name__ == "__main__":
    app()
