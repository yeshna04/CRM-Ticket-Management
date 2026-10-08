import sqlite3
import pandas as pd


def get_tickets(status=None):
    # Connect to database
    connection = sqlite3.connect("database/crm_tickets.db")

    # Base query
    query = """
    SELECT
        tickets.ticket_id,
        customers.customer_name,
        tickets.subject,
        tickets.priority,
        tickets.status,
        agents.agent_name,
        tickets.resolution_notes,
        tickets.created_at
    FROM tickets
    JOIN customers
        ON tickets.customer_id = customers.customer_id
    LEFT JOIN agents
        ON tickets.agent_id = agents.agent_id
    """

    # If a status is selected, add a filter
    if status:
        query += " WHERE tickets.status = ?"

        data = pd.read_sql_query(
            query,
            connection,
            params=(status,)
        )
    else:
        data = pd.read_sql_query(
            query,
            connection
        )

    # Close database
    connection.close()

    return data