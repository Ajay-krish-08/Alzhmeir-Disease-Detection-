import streamlit as st
import pandas as pd
from datetime import datetime
import uuid
from utils.styling import apply_custom_css, create_attractive_header, create_metric_card, create_floating_elements
from utils.auth import require_auth, show_user_info, is_authenticated

# Configure page
st.set_page_config(
    page_title="AI Dementia Risk Assessment",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())
if 'assessment_started' not in st.session_state:
    st.session_state.assessment_started = False
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

def main():
    # Apply custom styling
    apply_custom_css()
    create_floating_elements()
    
    # Check authentication first
    if not require_auth():
        return
    
    # Show user info in sidebar
    show_user_info()
    
    # Create attractive header
    create_attractive_header(
        "🧠 AI Dementia Risk Assessment",
        "Welcome to our cognitive health assessment tool",
        "🌟"
    )
    
    # Medical disclaimer
    st.warning("""
    ⚠️ **IMPORTANT MEDICAL DISCLAIMER**
    
    This tool is for educational and screening purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. 
    If you have concerns about cognitive health, please consult with a qualified healthcare professional.
    """)
    
    # Introduction
    st.markdown("""
    This assessment uses AI-powered analysis to evaluate cognitive function through various tests. 
    The evaluation takes approximately 15-20 minutes and covers:
    
    - **Memory Assessment** - Short and long-term memory tests
    - **Attention & Focus** - Concentration and attention span evaluation
    - **Language Skills** - Verbal fluency and comprehension
    - **Spatial Awareness** - Visual-spatial processing abilities
    - **Executive Function** - Problem-solving and decision-making skills
    """)
    
    # User information collection
    st.subheader("📝 Basic Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=18, max_value=120, value=65, 
                             help="Your age helps us provide age-appropriate assessments")
        education = st.selectbox("Education Level", 
                                ["Less than High School", "High School", "Some College", 
                                 "Bachelor's Degree", "Graduate Degree"],
                                help="Educational background influences cognitive baselines")
    
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
        has_concerns = st.selectbox("Do you have memory concerns?", 
                                   ["No concerns", "Mild concerns", "Moderate concerns", "Significant concerns"])
    
    # Family history
    st.subheader("🧬 Family History")
    family_history = st.multiselect(
        "Select any conditions present in your family:",
        ["Alzheimer's Disease", "Dementia", "Parkinson's Disease", "Stroke", "None of the above"],
        help="Family history helps assess genetic risk factors"
    )
    
    # Medical history
    st.subheader("🏥 Medical History")
    medical_conditions = st.multiselect(
        "Select any conditions you currently have:",
        ["Diabetes", "High Blood Pressure", "Heart Disease", "Depression", 
         "Sleep Disorders", "Head Injury", "None of the above"],
        help="Certain medical conditions can affect cognitive function"
    )
    
    # Store user data
    if st.button("🚀 Start Assessment", type="primary", use_container_width=True):
        st.session_state.user_data = {
            'age': age,
            'education': education,
            'gender': gender,
            'has_concerns': has_concerns,
            'family_history': family_history,
            'medical_conditions': medical_conditions,
            'timestamp': datetime.now()
        }
        st.session_state.assessment_started = True
        st.balloons()
    
    # Progress tracking and debug info
    if st.session_state.assessment_started:
        st.sidebar.success("✅ Basic Information Complete")
        st.sidebar.info("👉 Go to Assessment page to continue")
        
        # Auto-redirect to Assessment page after clicking Start Assessment
        st.success("✅ Information saved! You can now proceed to the Assessment page.")
        st.info("📍 Use the sidebar navigation to go to 'Assessment' page to begin testing.")
    
    
    # Instructions
    st.subheader("📋 Assessment Instructions")
    st.markdown("""
    **Before you begin:**
    
    1. **Environment**: Find a quiet space free from distractions
    2. **Time**: Allow 15-20 minutes for the complete assessment
    3. **Honesty**: Answer questions honestly for accurate results
    4. **Breaks**: You can take breaks between sections if needed
    5. **Help**: Have someone nearby if you need assistance reading or navigating
    
    **Technical Requirements:**
    - Stable internet connection
    - Screen large enough to read comfortably
    - Audio capability for certain tests (optional)
    """)
    
    # Contact information
    st.subheader("📞 Need Help?")
    st.markdown("""
    If you experience any technical difficulties or have questions about the assessment:
    - Technical Support: support@cognitivehealth.ai
    - Medical Questions: Please consult your healthcare provider
    
    **Crisis Resources:**
    - National Suicide Prevention Lifeline: 988
    - Crisis Text Line: Text HOME to 741741
    """)

if __name__ == "__main__":
    main()
