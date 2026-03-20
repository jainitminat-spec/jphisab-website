import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Setup
st.set_page_config(page_title="JPhisabkitab", page_icon="💰")

st.title("💰 JPhisabkitab")
st.write("Welcome, JP. Log your personal expenses below.")

# 2. Simple Entry Form
with st.form("my_form", clear_on_submit=True):
    date = st.date_input("Date", datetime.now())
    amount = st.number_input("Amount (₹)", min_value=0, step=1)
    category = st.selectbox("Category", ["Food", "Transport", "Rent", "Shopping", "Other"])
    note = st.text_input("Description")
    
    submit = st.form_submit_button("Save Expense")

# 3. Success Message
if submit:
    if amount > 0:
        st.success(f"Successfully recorded ₹{amount} for {category}!")
    else:
        st.warning("Please enter an amount greater than 0.")
