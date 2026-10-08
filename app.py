import streamlit as st
import sys
import os
import sqlite3
import pandas as pd


# =========================
# DATABASE CONNECTION
# =========================

connection = sqlite3.connect("database/crm_tickets.db")


# =========================
# ADD SRC FOLDER TO PATH
# =========================

sys.path.append(
    os.path.join(os.path.dirname(__file__), "src")
)


# Import functions
from filters import get_tickets

from ticket_operations import (
    create_ticket,
    assign_agent,
    update_priority,
    update_status,
    add_resolution_notes
)


# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="CRM Ticket Management",
    page_icon="🎫",
    layout="wide"
)


# =========================
# MAIN TITLE
# =========================

st.title("CRM Ticket Management System")

st.write(
    "Manage customer support tickets in one place."
)


# =========================
# GET ALL TICKETS
# =========================

all_tickets = get_tickets()


# =========================
# DASHBOARD SUMMARY
# =========================

st.subheader("Dashboard Summary")


total_tickets = len(all_tickets)

open_tickets = len(
    all_tickets[
        all_tickets["status"] == "Open"
    ]
)

in_progress_tickets = len(
    all_tickets[
        all_tickets["status"] == "In Progress"
    ]
)

resolved_tickets = len(
    all_tickets[
        all_tickets["status"] == "Resolved"
    ]
)

closed_tickets = len(
    all_tickets[
        all_tickets["status"] == "Closed"
    ]
)


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Tickets", total_tickets)

with col2:
    st.metric("Open Tickets", open_tickets)

with col3:
    st.metric("In Progress", in_progress_tickets)

with col4:
    st.metric("Resolved", resolved_tickets)

with col5:
    st.metric("Closed Tickets", closed_tickets)


# =========================
# PRIORITY SUMMARY
# =========================

st.subheader("Priority Summary")


critical_tickets = len(
    all_tickets[
        all_tickets["priority"] == "Critical"
    ]
)

high_tickets = len(
    all_tickets[
        all_tickets["priority"] == "High"
    ]
)

medium_tickets = len(
    all_tickets[
        all_tickets["priority"] == "Medium"
    ]
)

low_tickets = len(
    all_tickets[
        all_tickets["priority"] == "Low"
    ]
)


priority_col1, priority_col2, priority_col3, priority_col4 = st.columns(4)


with priority_col1:
    st.metric(
        "Critical",
        critical_tickets
    )


with priority_col2:
    st.metric(
        "High",
        high_tickets
    )


with priority_col3:
    st.metric(
        "Medium",
        medium_tickets
    )


with priority_col4:
    st.metric(
        "Low",
        low_tickets
    )


# =========================
# CREATE NEW TICKET
# =========================

st.subheader("Create New Ticket")


with st.form("create_ticket_form"):

    ticket_id = st.text_input(
        "Ticket ID"
    )

    customer_id = st.selectbox(
        "Customer",
        [
            "C001",
            "C002",
            "C003",
            "C004",
            "C005"
        ]
    )

    subject = st.text_input(
        "Subject"
    )

    description = st.text_area(
        "Description"
    )

    priority = st.selectbox(
        "Priority",
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ]
    )

    submit_button = st.form_submit_button(
        "Create Ticket"
    )


if submit_button:

    if ticket_id == "":
        st.error(
            "Please enter a Ticket ID."
        )

    elif subject == "":
        st.error(
            "Please enter a subject."
        )

    else:

        try:

            create_ticket(
                ticket_id,
                customer_id,
                subject,
                description,
                priority
            )

            st.success(
                "Ticket created successfully!"
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )


# =========================
# ASSIGN AGENT
# =========================

st.subheader(
    "Assign Ticket to Agent"
)


with st.form("assign_agent_form"):

    assign_ticket_id = st.text_input(
        "Ticket ID for Assignment"
    )

    agent_id = st.selectbox(
        "Select Agent",
        [
            "A001",
            "A002",
            "A003"
        ]
    )

    assign_button = st.form_submit_button(
        "Assign Agent"
    )


if assign_button:

    if assign_ticket_id == "":
        st.error(
            "Please enter a Ticket ID."
        )

    else:

        try:

            assign_agent(
                assign_ticket_id,
                agent_id
            )

            st.success(
                "Agent assigned successfully!"
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )


# =========================
# UPDATE TICKET
# =========================

st.subheader(
    "Update Ticket"
)


with st.form("update_ticket_form"):

    update_ticket_id = st.text_input(
        "Ticket ID for Update"
    )

    new_priority = st.selectbox(
        "New Priority",
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ]
    )

    new_status = st.selectbox(
        "New Status",
        [
            "Open",
            "In Progress",
            "Resolved",
            "Closed"
        ]
    )

    update_button = st.form_submit_button(
        "Update Ticket"
    )


if update_button:

    if update_ticket_id == "":
        st.error(
            "Please enter a Ticket ID."
        )

    else:

        try:

            update_priority(
                update_ticket_id,
                new_priority
            )

            update_status(
                update_ticket_id,
                new_status
            )

            st.success(
                "Ticket updated successfully!"
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )


# =========================
# RESOLUTION NOTES
# =========================

st.subheader(
    "Add Resolution Notes"
)


with st.form("resolution_notes_form"):

    notes_ticket_id = st.text_input(
        "Ticket ID for Resolution"
    )

    resolution_notes = st.text_area(
        "Resolution Notes"
    )

    notes_button = st.form_submit_button(
        "Save Resolution Notes"
    )


if notes_button:

    if notes_ticket_id == "":
        st.error(
            "Please enter a Ticket ID."
        )

    elif resolution_notes == "":
        st.error(
            "Please enter resolution notes."
        )

    else:

        try:

            add_resolution_notes(
                notes_ticket_id,
                resolution_notes
            )

            st.success(
                "Resolution notes saved successfully!"
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )


# =========================
# FILTER TICKETS
# =========================

st.subheader(
    "Filter Tickets"
)


filter_col1, filter_col2 = st.columns(2)


with filter_col1:

    status = st.selectbox(
        "Select Status",
        [
            "All",
            "Open",
            "In Progress",
            "Resolved",
            "Closed"
        ]
    )


with filter_col2:

    priority_filter = st.selectbox(
        "Select Priority",
        [
            "All",
            "Low",
            "Medium",
            "High",
            "Critical"
        ]
    )


# Get tickets according to status

if status == "All":

    tickets = get_tickets()

else:

    tickets = get_tickets(
        status
    )


# Apply priority filter

if priority_filter != "All":

    tickets = tickets[
        tickets["priority"] == priority_filter
    ]


# =========================
# TICKET LIST
# =========================

st.subheader(
    "Ticket List"
)


st.dataframe(
    tickets,
    width="stretch"
)


# =========================
# CLOSE DATABASE
# =========================

connection.close()