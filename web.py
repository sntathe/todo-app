import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("Thi is  todo app")
st.write("This app is useful for productivity")

for item in todos:
    st.checkbox(item)

st.text_input(label="" , placeholder="Enter a new to do")

