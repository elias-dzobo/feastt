import streamlit as st 
import os 


def register():
  st.title("Feedback Page")
  email = st.text_input("Email")
  password = st.text_area("Roast our product")
  submit = st.button("Submit")

  if submit:
    with open("feedback.txt", "a") as f:
      f.write(f"Email: {email}\n")
      f.write(f"Feedback: {password}\n\n")
      st.success("Thank you for your feedback!")
  


if __name__ == "__main__":
  register()