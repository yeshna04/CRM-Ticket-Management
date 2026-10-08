from ticket_operations import (
    update_status,
    assign_agent,
    add_resolution_notes,
    get_ticket
)


# Update T001 status
update_status("T001", "In Progress")


# Assign T001 to Amit
assign_agent("T001", "A003")


# Add resolution notes
add_resolution_notes(
    "T001",
    "Customer issue is being investigated."
)


# Display updated ticket
ticket = get_ticket("T001")

print("\nUPDATED TICKET")
print("-" * 40)
print(ticket)