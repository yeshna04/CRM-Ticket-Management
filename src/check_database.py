import streamlit as st
import sys
import os

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from filters import get_tickets
from ticket_operations import create_ticket


# Page settings
st.set_page_config(
    page_title="CRM Ticket Management",
    page_icon="🎫",
    layout="wide"
)


# Title
st.title("CRM Ticket Management System")

st.write("Manage customer support tickets in one place.")


# Get all tickets
all_tickets = get_tickets()


# Dashboard summary
st.subheader("Dashboard Summary")

total_tickets = len(all_tickets)
open_tickets = len(all_tickets[all_tickets["status"] == "Open"])
in_progress_tickets = len(
    all_tickets[all_tickets["status"] == "In Progress"]
)
closed_tickets = len(
    all_tickets[all_tickets["status"] == "Closed"]
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Tickets", total_tickets)

with col2:
    st.metric("Open Tickets", open_tickets)

with col3:
    st.metric("In Progress", in_progress_tickets)

with col4:
    st.metric("Closed Tickets", closed_tickets)


# Create ticket section
st.subheader("Create New Ticket")

with st.form("create_ticket_form"):

    ticket_id = st.text_input("Ticket ID")

    customer_id = st.selectbox(
        "Customer",
        ["C001", "C002", "C003", "C004", "C005"]
    )

    subject = st.text_input("Subject")

    description = st.text_area("Description")

    priority = st.selectbox(
        "Priority",
        ["Low", "Medium", "High", "Critical"]
    )

    submit_button = st.form_submit_button("Create Ticket")


# Create ticket when button is clicked
if submit_button:

    if ticket_id == "":
        st.error("Please enter a Ticket ID.")

    elif subject == "":
        st.error("Please enter a subject.")

    else:
        try:
            create_ticket(
                ticket_id,
                customer_id,
                subject,
                description,
                priority
            )

            st.success("Ticket created successfully!")

        except Exception as e:
            st.error(f"Error: {e}")


# Filter section
st.subheader("Filter Tickets")

status = st.selectbox(
    "Select Status",
    ["All", "Open", "In Progress", "Resolved", "Closed"]
)


# Get tickets based on filter
if status == "All":
    tickets = get_tickets()
else:
    tickets = get_tickets(status)


# Ticket list
st.subheader("Ticket List")

st.dataframe(
    tickets,
    width="stretch"
)