import streamlit as st
from datetime import datetime

# App Configurations
st.set_page_config(page_title="Cherish", page_icon="✨", layout="centered")

# Splash Screen
if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

if not st.session_state.splash_done:
    st.title("✨ Welcome to Cherish ✨")
    st.write("Collect, Share, and Cherish Memories Together")
    if st.button("Get Started"):
        st.session_state.splash_done = True
    st.stop()

# User Authentication Placeholder
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False

if not st.session_state.user_authenticated:
    st.title("Login / Sign Up")
    option = st.selectbox("Login Options", ["Sign in with Email", "Sign in with Google"])
    if st.button("Continue"):
        st.session_state.user_authenticated = True
    st.stop()

# Home Screen
st.title("Cherish: Home")
st.write("Your Memory Profiles")
profiles = st.session_state.get("profiles", [])

# Create New Profile
if st.button("Create New Profile"):
    with st.form("Create Profile"):
        name = st.text_input("Name")
        description = st.text_area("Description")
        photo = st.file_uploader("Upload a Cover Photo")
        submitted = st.form_submit_button("Save Profile")
        if submitted:
            profiles.append({"name": name, "description": description, "photo": photo, "memories": []})
            st.session_state["profiles"] = profiles
            st.success("Profile created successfully!")

# List Profiles
for profile in profiles:
    st.subheader(profile["name"])
    st.write(profile["description"])
    if st.button(f"View {profile['name']}"):
        st.session_state.selected_profile = profile
        st.session_state.viewing_profile = True

# Profile View
if "viewing_profile" in st.session_state and st.session_state.viewing_profile:
    selected_profile = st.session_state.selected_profile
    st.title(selected_profile["name"])
    st.image(selected_profile["photo"], caption=selected_profile["name"])

    # Tabs for Timeline, Gallery, Collaborators
    tab = st.radio("Select Tab", ["Timeline", "Gallery", "Collaborators"])

    if tab == "Timeline":
        st.write("### Timeline")
        for memory in selected_profile["memories"]:
            st.write(f"- {memory['content']} ({memory['date']})")

        if st.button("Add Memory"):
            with st.form("Add Memory"):
                content = st.text_area("Memory Content")
                date = st.date_input("Date", value=datetime.today())
                submit_memory = st.form_submit_button("Save Memory")
                if submit_memory:
                    selected_profile["memories"].append({"content": content, "date": date})
                    st.success("Memory added!")

    elif tab == "Gallery":
        st.write("### Gallery")
        st.write("(Photos and Videos will be displayed here)")

    elif tab == "Collaborators":
        st.write("### Collaborators")
        st.write("(Manage collaborators here)")

# Settings Screen
st.sidebar.title("Settings")
if st.sidebar.button("Upgrade to Premium"):
    st.sidebar.write("Premium features coming soon!")
if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.experimental_rerun()
