import sqlite3

# Connect to the database
connection = sqlite3.connect("database/crm_tickets.db")

# Create cursor
cursor = connection.cursor()

# Add customers
customers = [
    ("C001", "Aarav Sharma", "aarav@example.com", "9876543210"),
    ("C002", "Beena Singh", "beena@example.com", "9876543211"),
    ("C003", "Chahat Verma", "chahat@example.com", "9876543212"),
    ("C004", "Dev Kumar", "dev@example.com", "9876543213"),
    ("C005", "Esha Patel", "esha@example.com", "9876543214")
]

cursor.executemany("""
INSERT OR IGNORE INTO customers
(customer_id, customer_name, email, phone)
VALUES (?, ?, ?, ?)
""", customers)


# Add agents
agents = [
    ("A001", "Rahul", "rahul@example.com"),
    ("A002", "Priya", "priya@example.com"),
    ("A003", "Amit", "amit@example.com")
]

cursor.executemany("""
INSERT OR IGNORE INTO agents
(agent_id, agent_name, email)
VALUES (?, ?, ?)
""", agents)

# Add tickets
tickets = [
    (
        "T001",
        "C001",
        "Login Problem",
        "Customer is unable to log in to the account.",
        "High",
        "Open",
        "A001",
        "",
        "2026-10-01",
        "2026-10-01"
    ),
    (
        "T002",
        "C002",
        "Payment Failure",
        "Customer payment is failing during checkout.",
        "Critical",
        "In Progress",
        "A002",
        "",
        "2026-10-02",
        "2026-10-02"
    ),
    (
        "T003",
        "C003",
        "Account Update",
        "Customer wants to update account information.",
        "Medium",
        "Resolved",
        "A003",
        "Account information was updated successfully.",
        "2026-10-03",
        "2026-10-04"
    ),
    (
        "T004",
        "C004",
        "Password Reset",
        "Customer forgot the account password.",
        "High",
        "Closed",
        "A001",
        "Password was reset successfully.",
        "2026-10-04",
        "2026-10-05"
    ),
    (
        "T005",
        "C005",
        "Product Question",
        "Customer needs information about a product.",
        "Low",
        "Open",
        "A002",
        "",
        "2026-10-05",
        "2026-10-05"
    )
]

cursor.executemany("""
INSERT OR IGNORE INTO tickets
(ticket_id, customer_id, subject, description, priority,
 status, agent_id, resolution_notes, created_at, updated_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", tickets)

# Save changes
connection.commit()

# Close connection
connection.close()

print("Customers and agents added successfully!")