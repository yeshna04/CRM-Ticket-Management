from filters import get_tickets


# Get all tickets
print("ALL TICKETS")
print(get_tickets())


# Get only open tickets
print("\nOPEN TICKETS")
print(get_tickets("Open"))


# Get only closed tickets
print("\nCLOSED TICKETS")
print(get_tickets("Closed"))