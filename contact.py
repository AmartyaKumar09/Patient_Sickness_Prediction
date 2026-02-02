import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def app():
    
    # Set the title of the page
    st.title("Contact Us")

    # Introduction to the Contact Us page
    st.markdown(
        """
        ## Get in Touch
        If you have any questions, feedback, or suggestions, please feel free to contact us using the form below.
        We would love to hear from you!
        """
    )

    # Contact Form
    with st.form("contact_form"):
        # User input fields
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        # Submit button
        submit_button = st.form_submit_button("Send Message")

    if submit_button:
        if not name or not email or not message:
            st.error("Please fill in all fields.")
        elif not validate_email(email):
            st.error("Please enter a valid email address.")
        else:
            # Send email (example: replace with your email server settings)
            send_email(name, email, message)
            st.success("Your message has been sent successfully!")

# Email validation function
def validate_email(email):
    return '@' in email and '.' in email

# Function to send email
def send_email(name, email, message):
    try:
        sender_email = "your_email@example.com"  # Replace with your email
        receiver_email = "receiver_email@example.com"  # Replace with your email address
        password = "your_email_password"  # Replace with your email password

        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"Contact Us Message from {name}"

        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        # Establish SMTP connection and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

    except Exception as e:
        st.error(f"Error sending email: {e}")
        print(e)

# Run the app only if the script is executed directly
if __name__ == "__main__":
    app()
