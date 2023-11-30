import streamlit as st
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="NICO_BLOG",
    page_icon=":wave:",
    layout="wide",
)

# Apply custom CSS to set the background color
st.markdown(
    """
    <style>
        body {
            background-color: #add8e6; /* Light blue color */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container():
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st.title("Hi, I'm Romel Charlz Nico C. Dela Cruz and Welcome To my Blog :wave:, \n where you'll learn more about me")
        st.header("I'm a 2nd Year College Student in BSCPE Course")
        st.write("I'm learning how to code and program, since this is the field that I'm best at")
        st.write("Message me on Gmail [Click here >](https://www.gmail.com/rdelacruz4@ssct.edu.ph)")

    with right_column:
        img = Image.open(r"C:\Users\admin\Desktop\file\look.jpg")
        st.image(img, width=600, channels="RGB")

with st.container():
    st.write("---")
    st.header("Some information About me:")
    st.write("##")
    st.write(
        """
        - I'm a 2nd year irregular student who transferred courses from Bachelor of Science in Electronic Engineering (BSECE) to Bachelor of Science in Computer Engineering (BSCpE).
        - As a second-year irregular student, my academic journey has taken a fascinating turn, marked by a significant transition from my initial pursuit of a Bachelor of Science in Electronic Engineering (BSECE) to a dynamic new path in the field of Bachelor of Science in Computer Engineering (BSCpE).
        - This decision to shift courses reflects not just a change in academic focus but a deliberate choice to explore and align my educational journey with the evolving landscape of technology.
        - As a newcomer to the vast and ever-evolving field of computing, I find myself on an exhilarating exploration eager to unravel the intricacies that span the entire spectrum of this technological landscape.
        - My journey commences with a keen interest in programming, where I am navigating through the diverse languages and frameworks that serve as the building blocks for creating innovative software solutions.
        """
    )
    st.header("\n More Story about me:")
    st.write("##")
    st.write(
        """
        - In the past, my creative endeavors found a unique outlet as I immersed myself in the world of Warcraft 3 World Editor. This engaging platform became the canvas for my imaginative pursuits, where I delved into the intricate art of encoding triggers and crafting meticulously designed maps.
        - My passion for creating immersive gaming experiences reached new heights as I harnessed the tools provided by the World Editor to breathe life into custom scenarios and trigger-based events within the Warcraft 3 universe.
        - Upon completing my masterpieces, the natural next step was to share them with the vibrant community of gaming enthusiasts. HIVEWORKSHOP.COM emerged as the go-to platform for this purpose, providing a collaborative space where creators from around the world converged to showcase their creations.
        - Here are some links for samples of what I do [Click link to know more >](https://www.hiveworkshop.com/threads/hivewe-world-editor-0-6.303110/)
        """
    )

with st.container():
    st.image(r"C:\Users\admin\Desktop\file\Images\look.jpg", use_column_width=True)
