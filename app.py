import streamlit as st
# רשימת המכונות במחלקה
machines = ["מכונה א", "מכונה ב", "מכונה ג"]
selected = st.selectbox("בחר מכונה:", machines)
