# 💰 ExpenseTracker (Console-based)

A console-based personal Expense Tracker application built with **Python** and **MongoDB**. This project allows users to sign up, log in, manage expenses, and analyze spending habits in a structured and modular way.

---

## 📌 Features
* **User Authentication:** Secure Sign Up & Login (Password strength validation included).
* **Expense Management:** Add, View, Update, and Delete expenses.
* **Calculations:** Calculate total expenses automatically.
* **Analysis:** Compare monthly spending against salary with warning alerts.
* **Technical:** Input validation, error handling, and MongoDB persistence.
* **Architecture:** Clean layered architecture (separation of UI, Logic, and DB).

---

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Database:** MongoDB
* **Driver:** PyMongo
* **Interface:** Console / CLI based

---

## 📂 Project Structure

```text
ExpenseTracker/
│
├── app/
│   ├── config.py          # Configuration
│   ├── expenseTracker.py  # Menu & app flow control
│   ├── main.py            # Entry point
│   ├── services.py        # Business logic / connectors
│   └── user.py            # User class & user actions
│
├── db/
│   ├── db.py              # MongoDB connection
│   ├── expenseDB.py       # Expense-related DB operations
│   └── userDB.py          # User-related DB operations
│
├── utils/
│   ├── test.py
│   └── utils.py           # Validation & helper functions
│
├── .env                   # Environment variables
├── note.txt
└── README.md
```

▶️ How to Run the Project
1️⃣ Prerequisites
Python installed.

MongoDB running locally or via MongoDB Atlas.

Required packages installed:
```text
pip install pymongo python-dotenv
```

2️⃣ Configure Environment Variables
Create a .env file in the root directory and add your MongoDB connection string:
```text
MONGO_URI=mongodb://localhost:27017/
DB_NAME=ExpenseTrackerApp
```

3️⃣ Run the Application
Run the project from the root directory:
```text
python app/main.py
```

🔐 Authentication Flow
Sign Up: User registers with email & password (includes validation).

Login: User logs in with credentials.

Access: On successful login, user is redirected to the main dashboard menu.

💸 Expense Management
Once logged in, users can:
Add Expenses: Input amount, description, and date.
View All: See a list of all recorded expenses.
Update: Modify expense amounts.
Delete: Remove expenses using their ID.
Total: View the sum of all expenses.

📊 Expense Analysis
The app helps track financial health:
User inputs Monthly Salary.
App compares Total Expenses vs Salary.
Warning System: If expenses exceed 50% of salary, a warning is displayed.
Example Output: "Your expenses exceed 50% of your salary. Consider reducing your spending."

🧠 Design Decisions
Identifier: MongoDB ObjectId is used as the primary identifier.
Data Handling: Cursor results are converted to lists for reusability.
Error Handling: DB operations are wrapped in try-except blocks for stability.
Architecture: Clear separation of concerns:
app/ - UI & Control
services/ - Business Logic
db/ - Database Operations
utils/ - Helper Functions

⚠️ Notes & Limitations
Interface: Console-based (No GUI).
Session: Supports single-user session at a time.
Security: Basic authentication (Password hashing to be implemented).
Requirement: MongoDB must be running before starting the app.

🚀 Future Improvements
[ ] Password hashing (bcrypt) implementation.
[ ] Category-wise expense analysis.
[ ] Monthly PDF/Excel reports.
[ ] Export data to CSV.
[ ] Unit tests.

👤 Author
Developed as a learning-focused backend project to practice:
Python Programming
MongoDB Integration
Clean Architecture Principles
Object-Oriented Design (OOD)
