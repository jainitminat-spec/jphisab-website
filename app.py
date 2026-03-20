import streamlit as st
import pandas as pd
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="JPhisabkitab", layout="centered")

st.title("💰 JPhisabkitab")
st.subheader("Personal Expense Manager")

# --- INPUT SECTION ---
with st.form("entry_form", clear_on_submit=True):
    date = st.date_input("Date", datetime.now())
    amount = st.number_input("Amount (₹)", min_value=0, step=10)
    category = st.selectbox("Category", ["Food", "Transport", "Bills", "Shopping", "Other"])
    note = st.text_input("Note (e.g. Dinner with friends)")
    
    submitted = st.form_submit_button("Log Expense")
    if submitted:
        if amount > 0:
            st.success(f"Logged: ₹{amount} for {category}")
            # Later, we will add the code here to save to Google Sheets
        else:
            st.error("Please enter an amount.")

# --- DISPLAY SECTION (Coming Soon) ---
st.divider()
st.info("Charts and Google Sheets sync will appear here once connected.")
Create initial app file
