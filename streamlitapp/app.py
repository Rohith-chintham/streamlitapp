import streamlit as st
from form_handler import submit_application
from database import get_collection

# Page config
st.set_page_config(page_title="Application Portal", page_icon="📝", layout="centered")

# ---------- NAVBAR ----------
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📝 Application Form", "📋 View Applications", "ℹ️ About","📞 Contact", "📊 Analytics"])

# ---------- FEATURED SIDEBAR ----------
st.sidebar.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=150)
st.sidebar.title("📂 Menu")

st.sidebar.markdown("---")
st.sidebar.subheader("🔧 Features")

# Feature checkboxes or toggles (for future control)
show_footer = st.sidebar.checkbox("Show Footer", value=True)
dark_mode = st.sidebar.checkbox("Enable Dark Mode (UI)", value=False)
enable_debug = st.sidebar.toggle("Enable Debug Logs")

st.sidebar.markdown("---")
st.sidebar.info("📅 Today: " + str(st.session_state.get("today", "")))
st.sidebar.markdown("Built with ❤️ using Streamlit + MongoDB")


# ---------- HOME PAGE ----------
if page == "🏠 Home":
    st.title("🏠 Welcome to the Application Portal")
    st.markdown("""
    This is a demo application built with **Streamlit** and **MongoDB**.

    **Features:**
    - 📄 Submit applications
    - 💾 Store data in MongoDB
    - 📊 View submissions

    Use the sidebar to navigate.
    """)

# ---------- APPLICATION FORM ----------
elif page == "📝 Application Form":
    st.title("📝 Application Form")

    with st.form("application_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        age = st.number_input("Age", min_value=10, max_value=100, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        reason = st.text_area("Why are you applying?")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if name and email and reason:
                data = {
                    "name": name,
                    "email": email,
                    "age": age,
                    "gender": gender,
                    "reason": reason
                }
                success = submit_application(data)
                if success:
                    st.success("✅ Application submitted successfully!")
            else:
                st.error("❌ Please fill in all required fields.")

# ---------- VIEW APPLICATIONS ----------
elif page == "📋 View Applications":
    st.title("📋 Submitted Applications")

    applications = list(get_collection().find({}, {"_id": 0}))
    if not applications:
        st.info("No applications submitted yet.")
    else:
        for app in applications:
            with st.expander(f"{app['name']} ({app['email']})"):
                st.write(f"**Age:** {app['age']}")
                st.write(f"**Gender:** {app['gender']}")
                st.write(f"**Reason:** {app['reason']}")

# ---------- ABOUT PAGE ----------
elif page == "ℹ️ About":
    st.title("ℹ️ About This App")

    st.markdown("""
    **Application Portal** is a demo web app built using **Streamlit** and **MongoDB**.

    #### 🔍 Purpose:
    This app allows users to:
    - Fill and submit application forms
    - Store application data securely in MongoDB
    - View all submitted applications

    #### 🛠 Tech Stack:
    - **Frontend/UI**: Streamlit
    - **Backend DB**: MongoDB (local or Atlas)
    - **Language**: Python

    #### 👨‍💻 Developer:
    - Name: Rohit Chintham
    - Contact: [rohitchintham0527@gmail.com](mailto:rohitchintham0527@gmail.com)

    ---

    Feel free to reuse and customize this project for job portals, event registrations, or surveys.
    """)

    # ---------- CONTACT ----------
elif page == "📞 Contact":
    st.title("📞 Contact Us")
    st.write("📧 Email: rohitchintham@example.com")
    st.write("🌐 Website: https://github.com/rohitchintham")
    st.write("📍 Address: India")

# ---------- ANALYTICS ----------
elif page == "📊 Analytics":
    st.title("📊 Application Stats (Mock)")

    applications = list(get_collection().find({}, {"_id": 0}))
    if not applications:
        st.warning("No data yet to analyze.")
    else:
        ages = [a["age"] for a in applications]
        genders = [a["gender"] for a in applications]

        st.subheader("📈 Age Distribution")
        st.bar_chart(ages)

        st.subheader("📊 Gender Count")
        st.write({g: genders.count(g) for g in set(genders)})

# ---------- FOOTER ----------
st.markdown("""
    <hr style="margin-top: 2rem; margin-bottom: 0.5rem;">
    <div style='text-align: center; color: grey; font-size: 0.9rem;'>
        © 2025 Streamlit MongoDB App | Built by Rohit 🚀
    </div>
""", unsafe_allow_html=True)
