# ExpenseTracker (Console-based)

A console-based personal Expense Tracker application built with Python and MongoDB.
This project allows users to sign up, log in, manage expenses, and analyze spending habits in a structured and modular way.

📌 Features

User Sign Up & Login

Add new expenses

View all expenses

Update existing expenses

Delete expenses

Calculate total expenses

Analyze spending against salary

Input validation & error handling

MongoDB persistence

Clean layered architecture

🛠 Tech Stack

Python 3.10+

MongoDB

PyMongo

Console / CLI based interface

💾 Project Structure

ExpenseTracker/
│
├── app/
│   ├── main.py              # Entry point
│   ├── expenseTracker.py    # Menu & app flow control
│   ├── user.py              # User class & user actions
│   ├── services.py          # Business logic / connectors
│   └── config.py            # Configuration
│
├── db/
│   ├── db.py                # MongoDB connection
│   ├── userDB.py            # User-related DB operations
│   └── expenseDB.py         # Expense-related DB operations
│
├── utils/
│   └── utils.py             # Validation & helper functions
│
├── .env                     # Environment variables
└── README.md


▶️ How to Run the Project
1️⃣ Prerequisites

Python installed

MongoDB running locally or MongoDB Atlas

Required packages installed:

pip install pymongo python-dotenv

2️⃣ Configure Environment Variables

Create a .env file in the root directory:

MONGO_URI=mongodb://localhost:27017
DB_NAME=ExpenseTrackerApp

3️⃣ Run the Application

From the root directory:

python app/main.py

🔐 Authentication Flow

User signs up with email & password

Password strength is validated

User logs in

On successful login, user is redirected to the user menu

💸 Expense Management

Users can:

Add expenses (amount, description, date)

View all expenses

Update expense amount

Delete expenses using expense ID

Calculate total expenses

📊 Expense Analysis

User inputs monthly salary

App compares total expenses

If expenses exceed 50% of salary, a warning is shown

Example:

Your expenses exceed 50% of your salary.
Consider reducing your spending.

🧠 Design Decisions

MongoDB ObjectId is used as the primary identifier

Cursor results are converted to lists for reuse

DB operations are wrapped in try-except

Clear separation of concerns:

UI (app)

Business logic (services / user)

Database (db)

Utilities (utils)

⚠️ Notes & Limitations

Console-based (no GUI)

Single-user session at a time

No password hashing (can be added later)

MongoDB must be running before starting the app

🚀 Future Improvements

Password hashing (bcrypt)

Category-wise expense analysis

Monthly reports

Export data to CSV

Unit tests

👤 Author

Developed as a learning-focused backend project to practice:

Python

MongoDB

Clean architecture

Error handling

Object-oriented design
