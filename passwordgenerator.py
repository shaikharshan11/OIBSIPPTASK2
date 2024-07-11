import streamlit as st
import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
  
  characters = ""
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_lowercase:
    characters += string.ascii_lowercase
  if include_numbers:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  min_chars = sum([include_uppercase, include_lowercase, include_numbers, include_symbols])
  if min_chars > len(characters):
    st.error("Selected criteria require more character types than available.")
    return None

  password = ''.join(random.sample(characters, length))
  return password

st.markdown("## Password Generator by Mohammad Arshan Shaikh")

password_length = st.slider("Choose password length (minimum 8 characters):", min_value=8, max_value=32, step=1)

include_uppercase = st.checkbox("Include uppercase letters (A-Z)")
include_lowercase = st.checkbox("Include lowercase letters (a-z)")
include_numbers = st.checkbox("Include numbers (0-9)")
include_symbols = st.checkbox("Include symbols (!@#$%^&*)")

if st.button("Generate Password"):
  password = generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_symbols)

  if password:
    st.success(f"Your generated password is: {password}")
  else:
    st.warning("Password generation failed. Please ensure at least one character type is selected.")
