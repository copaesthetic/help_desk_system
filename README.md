# Help Desk System

## Description

This is a simple help desk system built with Flask and SQLite. It allows users to submit tickets, which are then stored in a SQLite database.

Step 1: Set Up Your Development Environment

1. Install Python:
•	Ensure you have Python installed. You can download it from python.org.
2. Install Flask:
• pip install Flask
3. Install SQLite:
•	SQLite is included with Python, so no additional installation is required.

Step 2: Project Structure

1. Create a project folder and structure it as follows:

help_desk_system/

│

├── app.py
 
├── templates/
 
│   ├── index.html

│   ├── submit_ticket.html

│   ├── view_tickets.html

 ├── static/
 
│   ├── style.css

 ├── db/
 
 
│   └── helpdesk.db

## Installation

Clone this repository to your local machine.
Install the required packages using pip:
```bash
pip install -r requirements.txt

# Run the application

python app.py

# Usage

Once the application is running, you can access it at http://127.0.0.1:5000 in your web browser.
To submit a ticket, navigate to http://127.0.0.1:5000/submit_ticket.
To view all tickets, navigate to http://127.0.0.1:5000/view_tickets.

# Contributing

Contributions are welcome! Please read the contributing guidelines before getting started.

# License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.
