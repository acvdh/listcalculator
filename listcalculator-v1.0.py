import streamlit as st

# Initialize session state if not already initialized
if 'items' not in st.session_state:
    st.session_state.items = []

# Debugging: Display current session state
st.write(f"Session State (before): {st.session_state.items}")

# Title of the app
st.title("🧮 List Calculator Sum of Total")

# Input area for adding items
with st.form("add_item_form", clear_on_submit=True):
    new_item = st.text_input("Enter a number or calculation (e.g., 5, 2*2.5):")
    submitted = st.form_submit_button("Add")
    if submitted:
        try:
            # Safely evaluate the expression
            value = eval(new_item, {"__builtins__": {}}, {})
            if isinstance(value, (int, float)):
                st.session_state.items.append((new_item, value))
                st.write(f"Item added: {new_item} = {value}")
            else:
                st.error("Only numeric results are allowed.")
        except Exception as e:
            st.error(f"Invalid input: {e}")

# Debugging: Display session state after adding
st.write(f"Session State (after adding item): {st.session_state.items}")

# Display list of items
st.subheader("Items List")
if st.session_state.items:
    for idx, (expression, value) in enumerate(st.session_state.items):
        col1, col2, col3 = st.columns([4, 2, 1])
        col1.write(f"`{expression}` = **{value:.2f}**")
        if col3.button("❌", key=f"remove_{idx}"):
            st.session_state.items.pop(idx)
            st.experimental_rerun()  # Rerun the app after item removal
else:
    st.info("No items added yet.")

# Debugging: Display session state after removing an item
st.write(f"Session State (after removing): {st.session_state.items}")

# Calculate and display total sum
total = sum(val for _, val in st.session_state.items)
st.subheader(f"**Total: {total:.2f}**")
