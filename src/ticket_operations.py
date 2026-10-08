import sqlite3
from datetime import datetime


# Create a new ticket
def create_ticket(ticket_id, customer_id, subject, description, priority):
    connection = sqlite3.connect("database/crm_tickets.db")
    cursor = connection.cursor()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO tickets
        (
            ticket_id,
            customer_id,
            subject,
            description,
            priority,
            status,
            agent_id,
            resolution_notes,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        ticket_id,
        customer_id,
        subject,
        description,
        priority,
        "Open",
        None,
        "",
        current_time,
        current_time
    ))

    connection.commit()
    connection.close()

    print("Ticket created successfully!")


# Assign ticket to an agent
def assign_agent(ticket_id, agent_id):
    connection = sqlite3.connect("database/crm_tickets.db")
    cursor = connection.cursor()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE tickets
        SET agent_id = ?,
            updated_at = ?
        WHERE ticket_id = ?
    """, (agent_id, current_time, ticket_id))

    connection.commit()
    connection.close()

    print("Agent assigned successfully!")


# Change ticket priority
def update_priority(ticket_id, priority):
    connection = sqlite3.connect("database/crm_tickets.db")
    cursor = connection.cursor()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE tickets
        SET priority = ?,
            updated_at = ?
        WHERE ticket_id = ?
    """, (priority, current_time, ticket_id))

    connection.commit()
    connection.close()

    print("Priority updated successfully!")


# Change ticket status
def update_status(ticket_id, status):
    connection = sqlite3.connect("database/crm_tickets.db")
    cursor = connection.cursor()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE tickets
        SET status = ?,
            updated_at = ?
        WHERE ticket_id = ?
    """, (status, current_time, ticket_id))

    connection.commit()
    connection.close()

    print("Status updated successfully!")


# Add resolution notes
def add_resolution_notes(ticket_id, notes):
    connection = sqlite3.connect("database/crm_tickets.db")
    cursor = connection.cursor()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE tickets
        SET resolution_notes = ?,
            updated_at = ?
        WHERE ticket_id = ?
    """, (notes, current_time, ticket_id))

    connection.commit()
    connection.close()

    print("Resolution notes added successfully!")