import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker", page_icon=":bar_chart:", layout="centered")

st.markdown("""
    <style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton {width: 50%; color: white; font-size: 18px;}
    </style>
    """, unsafe_allow_html=True)

st.title("Password Strength Checker")
st.write("Enter your password to check its strength")

def check_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at **least 8 characters long.**")
    
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase and lowercase letters.**")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number. (0-9)**")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character.**")

    # Provide feedback based on the score
    if score == 4:
        st.success("✅ **Strong Password**")
    elif score == 3:
        st.info("⚠️ **Medium Password** - Consider adding more characters or symbols.")
    else:
        st.error("❌ **Weak Password** - Follow the below instructions to make it strong.")
    
    if feedback:
        with st.expander("Password Requirements"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password", type="password", help="Ensure your password is strong and secure")

if st.button("Check Strength"):
    if password:
        check_strength(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.")
