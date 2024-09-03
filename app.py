import streamlit as st
from streamlit_option_menu import option_menu
import base64
import pandas as pd
import matplotlib.pyplot as plt


def get_image_as_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


st.set_page_config(
    page_title="Mark Kenneth Badilla's Portfolio", page_icon=":sparkles:", layout="wide"
)


bg_image = get_image_as_base64("bg.png")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), url("data:image/png;base64,{bg_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: left top;
        background-attachment: fixed;
    }}
    .css-18e3th9 {{
        background-color: rgba(250, 250, 250, 0.8); /* Light grey background with transparency for cards */
        border-radius: 10px;
        padding: 10px;
        border: 1px solid 
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    choose = option_menu(
        "Mark Kenneth Badilla",
        ["About", "Education", "Skills", "Experience", "Portfolio", "Contact"],
        icons=[
            "house",
            "book",
            "bar-chart-line",
            "briefcase",
            "collection",
            "envelope",
        ],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

if choose == "About":
    st.header("About Me")
    st.write(
        """
    Welcome to my portfolio! I'm Mark Kenneth Badilla, a fourth-year BSIT student at Cebu Institute of Technology - University, where my curiosity in technology has blossomed into a profound passion. From tinkering with my first computer to mastering complex software development, my journey is defined by relentless learning and a drive to solve real-world problems.

    With certifications like the TESDA NC-II in Computer Systems Servicing and practical experience from Kaggle competitions, I've honed skills that blend technical precision with strategic insight. My projects often merge technology with user experience, focusing on developing intuitive and impactful solutions in Android and web platforms.

    Active participation in the Computer Students Society and the Google Developer Student Club has enriched my network and fueled my enthusiasm for collaborative innovation. As I near graduation, I'm excited about contributing to transformative projects that leverage technology to improve lives.

    Thanks for stopping by, and I'm looking forward to connecting and collaborating with fellow tech enthusiasts!
    """
    )

elif choose == "Education":
    st.header("Education & Certifications")
    st.subheader("Cebu Institute of Technology - University")
    st.write("Fourth-Year BSIT Student")

    st.write(
        """
    **Certifications:**
    - TESDA NC-II Certification in Computer Systems Servicing
    - Certificates of Proficiency in:
        - Java
        - C
        - Python
        - SQL
    - Kaggle Certificates in Data Analytics
    """
    )

elif choose == "Skills":
    st.header("Skills")
    st.write(
        "Below is a detailed view of my proficiency across various technology domains:"
    )

    skills = {
        "Object-Oriented Programming": 95,
        "Web Development": 85,
        "Data Structures and Algorithms": 80,
        "Android Development": 80,
        "Project Management": 75,
        "Databases": 70,
        "Data Analytics": 65,
        "Systems Administration": 60,
        "Networking": 55,
        "Testing and Quality Assurance": 50,
        "Cybersecurity": 45,
    }

    min_level = st.slider("Minimum Skill Level", 0, 100, 45)

    filtered_skills = {
        skill: level for skill, level in skills.items() if level >= min_level
    }

    col1, col2 = st.columns(2)
    half_skills = len(filtered_skills) // 2
    skills_list = list(filtered_skills.items())

    with col1:
        for skill, level in skills_list[:half_skills]:
            st.text(skill)
            st.progress(level)

    with col2:
        for skill, level in skills_list[half_skills:]:
            st.text(skill)
            st.progress(level)

    st.subheader("Skill Distribution")
    skill_names = list(filtered_skills.keys())
    skill_levels = list(filtered_skills.values())

    plt.figure(figsize=(10, 5))
    plt.barh(skill_names, skill_levels, color="teal")
    plt.xlabel("Proficiency Level")
    plt.title("Skill Proficiency Distribution")
    st.pyplot(plt)

elif choose == "Experience":
    st.header("Professional Experience")
    experiences = [
        ("React.js Apps Development", "Developed small-scale React.js apps."),
        (
            "Real-time Geolocation E-commerce Platform",
            "Led a team to create a platform using Spring.",
        ),
        ("Android Recipe App", "Co-led a project, focusing on development and UI/UX."),
        (
            "Java Self-finance Management Platform",
            "Led a team in creating a finance management platform.",
        ),
        ("Capstone Project", "Currently working on an innovative Capstone project."),
    ]
    for title, desc in experiences:
        st.subheader(title)
        st.write(desc)

elif choose == "Portfolio":
    st.header("Portfolio")
    st.write(
        "Here are some highlights of my projects. Use the filter below to sort by technology."
    )

    tech_options = ["All", "React.js", "Java", "AI/ML"]
    selected_tech = st.selectbox("Filter by Technology", tech_options)

    projects = [
        {
            "title": "SyncUp",
            "desc": "A comprehensive platform for team collaboration and communication.",
            "tech": "React.js",
            "repo": "https://github.com/MrJim-Dev/SyncUp",
            "live": "https://syncup-org.vercel.app/",
        },
        {
            "title": "Cebu City AI Symptom Check Helpdesk",
            "desc": "AI-driven platform for symptom checking and guidance in Cebu City.",
            "tech": "AI/ML, React.js",
            "repo": "https://github.com/iammkb2002/hackathon-cebu-city-ai-symptom-check-helpdesk",
            "live": "https://my-app-theta-eight-62.vercel.app",
        },
        {
            "title": "Palit-A Nearby Vendor Commerce App",
            "desc": "A local commerce app connecting nearby vendors and customers.",
            "tech": "Java, React.js",
            "repo": "https://github.com/Palit-A-Nearby-Vendor-Commerce-App/Palit-A-Nearby-Vendor-Commerce-App",
        },
    ]

    if selected_tech != "All":
        projects = [proj for proj in projects if selected_tech in proj["tech"]]

    col1, col2, col3 = st.columns(3)

    if len(projects) > 0:
        with col1:
            for i, proj in enumerate(projects):
                if i % 3 == 0:
                    st.subheader(proj["title"])
                    st.write(proj["desc"])
                    st.markdown(f"[GitHub Repo]({proj['repo']})")
                    if "live" in proj:
                        st.markdown(f"[Live Preview]({proj['live']})")

        with col2:
            for i, proj in enumerate(projects):
                if i % 3 == 1:
                    st.subheader(proj["title"])
                    st.write(proj["desc"])
                    st.markdown(f"[GitHub Repo]({proj['repo']})")
                    if "live" in proj:
                        st.markdown(f"[Live Preview]({proj['live']})")

        with col3:
            for i, proj in enumerate(projects):
                if i % 3 == 2:
                    st.subheader(proj["title"])
                    st.write(proj["desc"])
                    st.markdown(f"[GitHub Repo]({proj['repo']})")
                    if "live" in proj:
                        st.markdown(f"[Live Preview]({proj['live']})")
    else:
        st.write("No projects found for the selected technology.")

elif choose == "Contact":
    st.header("Contact Information")
    st.write("Please fill out the form below to get in touch with me.")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f"Thank you, {name}! Your message has been received.")


st.markdown("<hr>", unsafe_allow_html=True)
st.write("2024 © Mark Kenneth Badilla")
