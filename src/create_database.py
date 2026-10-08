import sqlite3

# Connect to the database
connection = sqlite3.connect("database/crm_tickets.db")

# Create cursor
cursor = connection.cursor()

# Create customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email TEXT,
    phone TEXT
)
""")

# Create agents table
cursor.execute("""
CREATE TABLE IF NOT EXISTS agents (
    agent_id TEXT PRIMARY KEY,
    agent_name TEXT NOT NULL,
    email TEXT
)
""")

# Create tickets table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    subject TEXT NOT NULL,
    description TEXT,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    agent_id TEXT,
    resolution_notes TEXT,
    created_at TEXT,
    updated_at TEXT,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (agent_id)
        REFERENCES agents(agent_id)
)
""")

# Save changes
connection.commit()

# Close database connection
connection.close()

print("Database and tables created successfully!")