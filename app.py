import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Helper function to get base64 string
def get_image_as_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Configure page
st.set_page_config(page_title="Mark Kenneth Badilla's Portfolio", page_icon=":sparkles:", layout="wide")

# Embedding the background image using Base64
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
        border: 1px solid #e1e4e8;
    }}
    </style>
    """, unsafe_allow_html=True
)

# Sidebar and other content code remains the same
with st.sidebar:
    choose = option_menu("Mark Kenneth Badilla", ["About", "Education", "Skills", "Experience", "Portfolio", "Contact"],
                         icons=['house', 'book', 'bar-chart-line', 'briefcase', 'collection', 'envelope'],
                         menu_icon="cast", default_index=0, orientation="vertical")

if choose == "About":
    st.header("About Me")
    st.write("""
    Welcome to my portfolio! I'm Mark Kenneth Badilla, a fourth-year BSIT student at Cebu Institute of Technology - University, where my curiosity in technology has blossomed into a profound passion. From tinkering with my first computer to mastering complex software development, my journey is defined by relentless learning and a drive to solve real-world problems.

    With certifications like the TESDA NC-II in Computer Systems Servicing and practical experience from Kaggle competitions, I've honed skills that blend technical precision with strategic insight. My projects often merge technology with user experience, focusing on developing intuitive and impactful solutions in Android and web platforms.

    Active participation in the Computer Students Society and the Google Developer Student Club has enriched my network and fueled my enthusiasm for collaborative innovation. As I near graduation, I'm excited about contributing to transformative projects that leverage technology to improve lives.

    Thanks for stopping by, and I'm looking forward to connecting and collaborating with fellow tech enthusiasts!
    """)


elif choose == "Education":
    st.header("Education & Certifications")
    st.subheader("Cebu Institute of Technology - University")
    st.write("Fourth-Year BSIT Student")
    
    # Displaying certification details
    st.write("""
    **Certifications:**
    - TESDA NC-II Certification in Computer Systems Servicing
    - Certificates of Proficiency in:
        - Java
        - C
        - Python
        - SQL
    - Kaggle Certificates in Data Analytics
    """)


elif choose == "Skills":
    st.header("Skills")
    st.write("Below is a detailed view of my proficiency across various technology domains:")
    
    # Dictionary for skills and their proficiency levels
    skills = {
        "Data Structures and Algorithms": 80,
        "Web Development": 80,
        "Android Development": 80,
        "Project Management": 80,
        "Databases": 80,
        "Object-Oriented Programming": 80,
        "Data Analytics": 80,
        "Networking": 80,
        "Systems Administration": 80,
        "Testing and Quality Assurance": 80,
        "Cybersecurity": 80
    }
    
    # Using columns to make it more readable, splitting into two columns
    col1, col2 = st.columns(2)
    half_skills = len(skills) // 2  # Determine the split point
    skills_list = list(skills.items())  # Convert to list to use slicing
    
    with col1:
        for skill, level in skills_list[:half_skills]:
            st.text(skill)
            st.progress(level)
            
    with col2:
        for skill, level in skills_list[half_skills:]:
            st.text(skill)
            st.progress(level)


elif choose == "Experience":
    st.header("Professional Experience")
    experiences = [
        ("React.js Apps Development", "Developed small-scale React.js apps."),
        ("Real-time Geolocation E-commerce Platform", "Led a team to create a platform using Spring."),
        ("Android Recipe App", "Co-led a project, focusing on development and UI/UX."),
        ("Java Self-finance Management Platform", "Led a team in creating a finance management platform."),
        ("Capstone Project", "Currently working on an innovative Capstone project.")
    ]
    for title, desc in experiences:
        st.subheader(title)
        st.write(desc)

elif choose == "Portfolio":
    st.header("Portfolio")
    st.write("Here are some highlights of my projects. Click on the cards to view the GitHub repositories and live demos.")

    # Layout for cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("SyncUp")
        st.write("A comprehensive platform for team collaboration and communication.")
        st.markdown("[GitHub Repo](https://github.com/MrJim-Dev/SyncUp)")
        st.markdown("[Live Preview](https://syncup-org.vercel.app/)")

    with col2:
        st.subheader("Cebu City AI Symptom Check Helpdesk")
        st.write("AI-driven platform for symptom checking and guidance in Cebu City.")
        st.markdown("[GitHub Repo](https://github.com/iammkb2002/hackathon-cebu-city-ai-symptom-check-helpdesk)")
        st.markdown("[Live Preview](https://my-app-theta-eight-62.vercel.app)")

    with col3:
        st.subheader("Palit-A Nearby Vendor Commerce App")
        st.write("A local commerce app connecting nearby vendors and customers.")
        st.markdown("[GitHub Repo](https://github.com/Palit-A-Nearby-Vendor-Commerce-App/Palit-A-Nearby-Vendor-Commerce-App)")


elif choose == "Contact":
    st.header("Contact Information")
    st.write("Email: markkenneth.badilla@cit.edu")

# Footer
st.markdown('<hr>', unsafe_allow_html=True)
st.write("2024 © Mark Kenneth Badilla")
