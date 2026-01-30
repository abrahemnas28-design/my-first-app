import streamlit as st
st.tittle("המונה של אברהים")
if 'count' not in st.session_state
      st.session_state=0
st.write(f"המספר הנוכחי הוא: {st.session_state.count}")

if st.button("לחץ כאן כדי להוסיף 1"):
    st.session_state.count += 1
    st.rerun()

