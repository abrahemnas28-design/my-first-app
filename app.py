import streamlit as st

st.title("הפרויקט החדש של אברהים")
st.write("ברוכים הבאים לאפליקציה הראשונה שבניתי לבד!")

name = st.text_input("איך קוראים לך?")
if st.button("לחץ כאן"):
    st.success(f"שלום {name}, הקוד עובד!")
