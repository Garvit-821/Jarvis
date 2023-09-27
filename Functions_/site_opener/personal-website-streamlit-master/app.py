import requests
import sys
print(sys.version_info)
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Fact Planet", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/2.jpg")
img_lottie_animation = Image.open("images/1.png")
img_video = Image.open("images/3.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Garvit :wave:")
    st.title("A student and passionate to science and programming From India")
    st.write("My name is Garvit Prakash. I am currently a student with a passion for space science, programming, and developing IoT and Python projects.In addition, I have published two books on space science and ancient space science. I also produce videos; check out my channel and my books on Amazon")
    st.write("[Learn More >](www.youtube.com/@factplanet_821)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I creates videos for people who:
            - are Intersted in space science.
            - are Interested in ancient science of india.
            - are passionate for Science and programming.
            - are gathering information."

            If this sounds interesting to you, consider subscribing and turning on the notifications, you can also read my books by below links, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@factplanet_821)")
        st.write("[Book link >]https://amzn.eu/d/6N2xZ4N)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("The Secrets Behind Modern Science Volume 1")
        st.write(
            """
This book will teach you about ancient India's scientific growth.
How did things become discovered in ancient times? 
This book has the answers to all of your queries.
I am confident that this will be a valuable resource not just for students
interested in astronomy and ancient science, but also for those interested
in space science and ancient science.
            """
        )
        st.markdown("[Buy Now...](https://amzn.eu/d/6N2xZ4N)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("What If Oxygen Got Disappeared From Earth For 5 seconds")
        st.write(
            """
            Want to know What will happen If oxygen got disappeard for 5 seconds?
            This video will show you what happens if the earth's oxygen supply is cut off for 5 seconds.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=6S3BijI-Y4E)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_video)
    with text_column:
        st.subheader("Can We Survive On Mars")
        st.write(
            """
            Want to know can we survive on mars?
            This video will be a powerfull companion and this will let you know about it.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/2hzHur0s9nM)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/factplanetofficial@gmail.com
" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
