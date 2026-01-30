import streamlit as st

# כותרת
st.title("מערכת המונה של אברהים")

# 1. הוספת תיבת טקסט לקבלת שם העובד
user_name = st.text_input("נא להזין שם עובד:")

# 2. שימוש ב-f כדי להציג ברכה אישית
if user_name:
    st.write(f"### שלום {user_name}, שיהיה לך יום עבודה פורה! 🛠️")

st.divider() # קו מפריד לעיצוב

# יצירת זיכרון למספר
if 'count' not in st.session_state:
    st.session_state.count = 0

# הצגת המונה עם f-string
st.header(f"כמות שיוצרה: {st.session_state.count}")

# כפתור הוספה
if st.button("➕ הוסף יחידה"):
    st.session_state.count += 1
    st.rerun()

# כפתור איפוס
if st.button("🔄 איפוס מונה"):
    st.session_state.count = 0
    st.rerun()

if st.button("ضيف ثلاث"):
    st.session_state.count+=3
    st.rerun()
