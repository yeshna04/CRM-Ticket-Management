from ticket_operations import (
    create_ticket,
    assign_agent,
    update_priority,
    update_status,
    add_resolution_notes
)


# Create a new ticket
create_ticket(
    "T008",
    "C003",
    "Internet Problem",
    "Customer is unable to access the internet.",
    "High"
)

# Assign ticket to Rahul
assign_agent("T008", "A001")

# Change priority
update_priority("T008", "Critical")

# Change status
update_status("T008", "In Progress")

# Add resolution notes
add_resolution_notes(
    "T008",
    "Internet connection issue is being investigated."
)