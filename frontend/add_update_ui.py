import streamlit as st
from datetime import datetime
import requests

# ✅ REMOVE trailing slash
API_URL = "http://127.0.0.1:8000"


def add_update_tab():
    selected_date = st.date_input(
        "Enter Date",
        datetime(2024, 8, 1),
        label_visibility="collapsed"
    )

    # ✅ FORMAT DATE PROPERLY
    formatted_date = selected_date.strftime("%Y-%m-%d")

    # ✅ API CALL
    try:
        response = requests.get(f"{API_URL}/expenses/{formatted_date}")

        # 🔍 DEBUG (VERY IMPORTANT)
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        if response.status_code == 200:
            try:
                existing_expenses = response.json()
            except ValueError:
                st.error("❌ Invalid JSON from server")
                st.text(response.text)
                existing_expenses = []
        else:
            st.error(f"❌ Failed to retrieve expenses ({response.status_code})")
            st.text(response.text)
            existing_expenses = []

    except requests.exceptions.RequestException as e:
        st.error("❌ Cannot connect to backend")
        st.text(str(e))
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i].get('amount', 0.0)
                category = existing_expenses[i].get("category", "Shopping")
                notes = existing_expenses[i].get("notes", "")
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)

            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=float(amount),
                    key=f"amount_{i}",
                    label_visibility="collapsed"
                )

            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=categories.index(category),
                    key=f"category_{i}",
                    label_visibility="collapsed"
                )

            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"notes_{i}",
                    label_visibility="collapsed"
                )

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button()

        if submit_button:
            filtered_expenses = [
                expense for expense in expenses if expense['amount'] > 0
            ]

            try:
                response = requests.post(
                    f"{API_URL}/expenses/{formatted_date}",
                    json=filtered_expenses
                )

                if response.status_code == 200:
                    st.success("✅ Expenses updated successfully!")
                else:
                    st.error(f"❌ Failed to update expenses ({response.status_code})")
                    st.text(response.text)

            except requests.exceptions.RequestException as e:
                st.error("❌ Failed to connect to backend")
                st.text(str(e))