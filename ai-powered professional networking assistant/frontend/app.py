import streamlit as st

st.set_page_config(
    page_title="AI Professional Networking Assistant",
    page_icon="🤝",
    layout="wide"
)

st.title("🤝 AI-Powered Professional Networking Assistant")

st.write(
    "Prepare for professional networking events with "
    "AI-powered conversation suggestions."
)

st.divider()

st.header("Event Information")

event_description = st.text_area(
    "Describe the event",
    placeholder="Example: AI for Sustainable Cities"
)

interests = st.text_input(
    "Your interests",
    placeholder="Example: climate change, urban planning, artificial intelligence"
)

networking_goal = st.selectbox(
    "What is your networking goal?",
    [
        "Build professional relationships",
        "Find a mentor",
        "Find career opportunities",
        "Find collaborators",
        "Learn about the industry",
        "Promote my project"
    ]
)

if st.button("Generate Conversation Starters"):
    if not event_description:
        st.warning("Please enter an event description.")
    else:
        st.success("Your personalized conversation starters will appear here.")
