
import streamlit as st

st.title("מעקב תיקון תקלות")

# שלב הזיכרון - האם יש לנו ארגז בשם repairs?
if 'repairs' not in st.session_state:
    st.session_state.repairs = 0

# הצגת המשתנה למשתמש
st.subheader(f"סה"כ תקלות שטופלו היום: {st.session_state.repairs}")

# הפעולה - כפתור שמעדכן את המשתנה
if st.button("✅ סימנתי תקלה כטופלה"):
    st.session_state.repairs += 1  # כאן אנחנו מוסיפים 1 למשתנה המספרי
    st.success("כל הכבוד! העדכון נשמר")
    st.rerun()
