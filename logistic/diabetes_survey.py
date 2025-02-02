import streamlit as st
import pandas as pd
import os

# Define the CSV file path
csv_file = "diabetes_survey_responses.csv"

# Function to save data to CSV
def save_data(data):
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    else:
        df = pd.DataFrame(columns=data.keys())
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    
    df.to_csv(csv_file, index=False)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "section1"

# Set page configuration
st.set_page_config(page_title="Diabetes Health Survey", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #D8BFD8; /* Light Purple */
    }
    h1, h2, h3, h4, h5 {
        color: #FF00FF; /* Neon Color */
    }
    .contact {
        background-color: #333;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        color: #D8BFD8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with information about diabetes
st.sidebar.header("Diabetes Information Center")
st.sidebar.markdown("""
**What is Diabetes?**
Diabetes is a chronic health condition that occurs when the body cannot effectively use insulin, leading to high blood sugar levels.

**Types of Diabetes:**
- **Type 1 Diabetes**: The body does not produce insulin.
- **Type 2 Diabetes**: The body does not use insulin properly.
- **Gestational Diabetes**: Develops during pregnancy and usually resolves after giving birth.

**Managing Diabetes:**
- Regular monitoring of blood sugar levels.
- Healthy eating and regular physical activity.
- Medication adherence as prescribed by a healthcare professional.

**Learn More**: [American Diabetes Association](https://www.diabetes.org)
""")

# Main Content
st.title("🩺 Diabetes Health Survey")
st.header("Your Health Matters!")
st.markdown("This survey collects important information about your health and diabetes management. Your responses provide valuable insights that help us better understand your needs and support you effectively in managing diabetes.")
st.markdown("<h5 style='color: blue;'>Thank you for participating!</h5>", unsafe_allow_html=True)

# Page Navigation
if st.session_state.page == "section1":
    # Section 1 questions
    with st.form(key='section1'):
        name = st.text_input("Please enter your name", placeholder="Your Name")
        email = st.text_input("Please enter your email address", placeholder="Your Email")
        age_group = st.text_input("What is your age group?", placeholder="e.g., 30-39")
        gender = st.text_input("What is your gender?", placeholder="e.g., Male/Female/Other")
        blood_pressure = st.text_input("What is your average blood pressure?", placeholder="e.g., 120/80 mmHg")
        fasting_blood_sugar = st.text_input("What is your most recent fasting blood sugar level?", placeholder="e.g., 90 mg/dL")
        random_blood_sugar = st.text_input("What is your most recent random blood sugar level?", placeholder="e.g., 150 mg/dL")
        diagnosed_diabetes = st.text_input("Have you been diagnosed with diabetes? (Yes/No)", placeholder="Yes or No")
        diabetes_type = st.text_input("What type of diabetes have you been diagnosed with?", placeholder="Type 1/Type 2/Gestational/Not diagnosed")
        bmi = st.text_input("What is your body mass index (BMI)?", placeholder="e.g., 22.5")
        exercise_frequency = st.text_input("How often do you exercise?", placeholder="e.g., Regularly, Occasionally")
        diet = st.text_input("What is your typical diet?", placeholder="e.g., Balanced, Low-carb")
        resources = st.text_input("What resources or support do you feel would help you manage your diabetes better?")
        medications = st.text_input("Are you currently taking any medications for diabetes? (Yes/No)", placeholder="Yes or No")

        # Submit button for section 1
        submitted = st.form_submit_button("Next")
        if submitted:
            st.session_state.section1_data = {
                "name": name,
                "email": email,
                "age_group": age_group,
                "gender": gender,
                "blood_pressure": blood_pressure,
                "fasting_blood_sugar": fasting_blood_sugar,
                "random_blood_sugar": random_blood_sugar,
                "diagnosed_diabetes": diagnosed_diabetes,
                "diabetes_type": diabetes_type,
                "bmi": bmi,
                "exercise_frequency": exercise_frequency,
                "diet": diet,
                "resources": resources,
                "medications": medications,
            }
            st.session_state.page = "section2"  # Navigate to section 2

# Section 2: Medication Management
if st.session_state.page == "section2":
    st.title("💊 Medication Management")
    st.markdown("We want to understand how you manage your diabetes medications.")
    
    # Section 2 questions
    with st.form(key='section2'):
        medication_types = st.text_input("What type of diabetes medications are you taking? (List all that apply)", placeholder="e.g., Insulin, Metformin")
        medication_duration = st.text_input("How long have you been taking these medications?", placeholder="e.g., 1 year")
        medication_frequency = st.text_input("How often do you take your diabetes medications?", placeholder="e.g., Once daily")
        side_effects = st.text_input("Do you experience any side effects from your diabetes medications? (Yes/No)", placeholder="Yes or No")
        side_effects_specify = st.text_input("If yes, please specify:", placeholder="e.g., Nausea")
        medication_needs_changed = st.text_input("Have your medication needs changed over time? (Yes/No)", placeholder="Yes or No")
        tracking_methods = st.text_input("How do you keep track of your medication regimen? (List all that apply)", placeholder="e.g., Pill organizer, Mobile app")

        # Submit button for section 2
        submitted_section2 = st.form_submit_button("Submit")
        if submitted_section2:
            section2_data = {
                "medication_types": medication_types,
                "medication_duration": medication_duration,
                "medication_frequency": medication_frequency,
                "side_effects": side_effects,
                "side_effects_specify": side_effects_specify,
                "medication_needs_changed": medication_needs_changed,
                "tracking_methods": tracking_methods,
            }
            # Save all data to CSV
            save_data({**st.session_state.section1_data, **section2_data})
            st.success("🎉 Thank you for completing the survey!")
            # Reset for a new submission if needed
            st.session_state.page = "section1"  # Go back to section 1 if desired

# Contact Information Section
st.markdown(
    """
    <div class="contact">
        <h4>Contact Your Doctor</h4>
        <p>If you have any specific issues, feel free to reach out:</p>
        <p><strong>Clinic Address:</strong> Yeshwanthpur, Bangalore</p>
        <p><strong>Contact Number:</strong> 9945434243</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Run the app using: streamlit run diabetes_survey.py
