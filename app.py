#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", page_icon="📈", layout="centered")
st.title("Growth Minset Challenge: Web App with Streamlit ")

st.header("✨Welcome to the Growth Mindset Challenge!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection,challenges and achievements! ")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("⏳A growth mindset turns every challenge into a stepping stone, not a stumbling block. - Samra Waseem")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f" You're facing a challenge: {user_input}. Embrace it as an opportunity to grow!")
else:
    st.warning("Please enter a challenge you're facing.")

#reflexing
    st.header("Reflect on Your Growth Mindset")
    reflection = st.text_area("Reflect on your growth mindset journey:")

    if reflection:
        st.success(f"Your reflection: {reflection}. Keep nurturing your growth mindset!")
    else:
        st.info("Reflecting on past experiences helps you grow. Share your thoughts!")


#achievements
st.header("🎉🎉Celebrate Your Wins!")
achievement = st.text_input("Share a recent achievement:")

if achievement:
    st.success(f"🎉Congratulations on your achievement: {achievement}! Celebrate your progress!")
else:
    st.info("👑Big or small , every achievement counts. Share your wins!")

#footer
st.write("---")
st.write("🎉Believe in your ability to create change—every small step counts towards a bigger leap.")
st.write("🤩Thank you for using the Growth Mindset Challenge app!")
st.write("✨**Created by Samra Waseem**")