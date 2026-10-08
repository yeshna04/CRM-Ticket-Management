# CRM Ticket Management System

A simple CRM-based ticket management system for managing customer support tickets.

## Project Overview

The CRM Ticket Management System helps manage customer support tickets in one place. It allows users to create tickets, assign them to support agents, update ticket priority and status, add resolution notes, and filter tickets.

The system uses Python and SQLite for backend processing and Streamlit for the user interface.

## Objectives

- Manage customer support tickets
- Link tickets with customers
- Assign tickets to support agents
- Manage ticket priorities
- Track ticket status
- Add resolution notes
- Filter tickets by status and priority
- Display ticket information in a table
- Provide dashboard summaries

## Technologies Used

- Python
- SQLite
- Pandas
- Streamlit

## Main Features

### 1. Dashboard Summary

The dashboard displays:

- Total Tickets
- Open Tickets
- In Progress Tickets
- Resolved Tickets
- Closed Tickets

It also provides a priority summary for:

- Critical
- High
- Medium
- Low

### 2. Create New Ticket

Users can create a new support ticket by entering:

- Ticket ID
- Customer
- Subject
- Description
- Priority

New tickets are created with an initial status of `Open`.

### 3. Assign Ticket to Agent

Tickets can be assigned to available support agents.

### 4. Update Ticket

Users can update:

- Ticket Priority
- Ticket Status

Available statuses are:

- Open
- In Progress
- Resolved
- Closed

### 5. Resolution Notes

Users can add resolution notes to record how a customer issue was handled.

### 6. Ticket Filtering

Tickets can be filtered by:

- Status
- Priority

Both filters can also be used together.

### 7. Ticket List

The application displays ticket information including:

- Ticket ID
- Customer
- Subject
- Priority
- Status
- Assigned Agent
- Resolution Notes
- Created Date

## Project Structure

```text
CRM Ticket Management/
│
├── app.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── check_database.py
│   ├── create_database.py
│   ├── filters.py
│   ├── load_data.py
│   ├── test_filters.py
│   ├── test_operations.py
│   ├── test_ticket_operations.py
│   └── ticket_operations.py
│
├── data/
│
├── database/
│
└── reports/
```

## Database

The project uses SQLite.

The main tables are:

### Customers

Stores customer information.

### Agents

Stores support agent information.

### Tickets

Stores ticket details such as customer, subject, priority, status, assigned agent, resolution notes, and timestamps.

The ticket table connects customers and agents using their IDs.

## Application Workflow

```text
Customer
   ↓
Create Ticket
   ↓
Assign Agent
   ↓
Set Priority
   ↓
Update Status
   ↓
Add Resolution Notes
   ↓
Close Ticket
   ↓
Filter and View Tickets
```

## How to Run

Clone the repository and open the project folder.

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in the browser.

## Testing

The application was tested for:

- Ticket creation
- Agent assignment
- Priority updates
- Status updates
- Resolution notes
- Status filtering
- Priority filtering
- Combined filtering
- Ticket listing
- Dashboard summary

## Future Enhancements

Possible future improvements include:

- Login and authentication
- Dynamic customer and agent selection
- Search functionality
- Ticket editing and deletion
- Charts and visual analytics
- Email notifications
- Role-based access
- Deployment to a cloud platform

## Conclusion

The CRM Ticket Management System provides a simple way to manage customer support tickets. It combines Python, SQLite, Pandas, and Streamlit to provide ticket management, agent assignment, status tracking, filtering, and dashboard reporting in one application.