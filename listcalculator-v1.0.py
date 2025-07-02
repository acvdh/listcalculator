#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# List calculator v1
# This tool allows users to input numeric expressions, evaluate them, and maintain a running list of results. 
# It also computes and displays the total sum of all the evaluated items.
# Written by Dr. A.C. van der Heijden


import streamlit as st

st.title("🧮 List Calculator Sum of Total")

# Initialize session state
if 'items' not in st.session_state:
    st.session_state.items = []

# Input area
with st.form("add_item_form", clear_on_submit=True):
    new_item = st.text_input("Enter a number or calculation (e.g., 5, 2*2.5):")
    submitted = st.form_submit_button("Add")
    if submitted:
        try:
            # Evaluate the expression safely
            value = eval(new_item, {"__builtins__": {}}, {})
            if isinstance(value, (int, float)):
                st.session_state.items.append((new_item, value))
            else:
                st.error("Only numeric results are allowed.")
        except Exception as e:
            st.error(f"Invalid input: {e}")

# Display list of items
st.subheader("Items List")

if st.session_state.items:
    for idx, (expression, value) in enumerate(st.session_state.items):
        col1, col2, col3 = st.columns([4, 2, 1])
        col1.write(f"`{expression}` = **{value:.2f}**")
        if col3.button("❌", key=f"remove_{idx}"):
            st.session_state.items.pop(idx)
            st.experimental_rerun()
else:
    st.info("No items added yet.")

# Total
total = sum(val for _, val in st.session_state.items)
st.subheader(f"**Total: {total:.2f}**")

