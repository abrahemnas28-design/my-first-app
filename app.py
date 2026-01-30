import streamlit as st
st.title("המונה של אברהים")
if 'count' not in st.session_state:
    st.session_state.count = 0
st.write(f"המספר הנוכחי הוא: {st.session_state.count}")

if st.button("לחץ כאן כדי להוסיף 1"):
    st.session_state.count += 1
    st.rerun()

