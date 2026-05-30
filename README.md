# Digital Wallet Simulator

## Overview

Digital Wallet Simulator is a console-based financial management application developed in Python. The system simulates the core functionalities of a modern digital wallet, allowing users to securely manage funds, perform transactions, track spending activity, and maintain savings goals through a menu-driven interface.

The application uses JSON-based storage to maintain persistent user data, ensuring that account information, balances, and transaction records remain available across multiple program executions.

---

## Features

### User Account Management
- User Registration
- Secure PIN-Based Login
- User Authentication
- PIN Change Functionality

### Wallet Operations
- Deposit Funds
- Withdraw Funds
- Balance Inquiry
- Real-Time Balance Updates

### Money Transfer System
- Transfer Funds Between Registered Users
- Recipient Validation
- Automatic Balance Synchronization

### Transaction Tracking
- Complete Transaction History
- Deposit Records
- Withdrawal Records
- Transfer Records
- Bill Payment Records
- Timestamp-Based Logging

### Savings Goal Management
- Create Savings Goals
- Track Goal Progress
- Monitor Remaining Target Amount

### Bill Payment Module
- Utility Bill Payment Simulation
- Automatic Wallet Deduction
- Transaction Recording

### Data Persistence
- Persistent User Accounts
- Persistent Wallet Balances
- Persistent Transaction Records
- JSON-Based Data Storage

---

## Technical Implementation

The project follows a modular function-based architecture where each wallet operation is implemented as an independent function. User interactions are handled through a menu-driven interface that validates inputs and guides users through available operations.

User data is stored in JSON files, allowing account information, balances, transaction histories, and savings goals to persist between sessions without requiring a database management system.

The application includes validation checks for:

- User Authentication
- PIN Verification
- Valid Transaction Amounts
- Sufficient Wallet Balance
- Existing Recipient Accounts
- Input Validation and Error Handling

---

## Technology Stack

### Programming Language
- Python 3

### Data Storage
- JSON Files

### Libraries Used
- `json`
- `datetime`
- `time`

### Python Concepts Implemented
- Functions
- Dictionaries
- Lists
- Loops
- Conditional Statements
- Exception Handling
- File Handling
- Modular Programming

---

## Project Structure

```text
Digital-Wallet-Simulator/
│
├── digital_wallet.py
├── users.json
├── transactions.json
├── README.md
└── LICENSE
```

---

## Functional Workflow

1. User registers an account and creates a secure PIN.
2. User credentials are stored in JSON format.
3. User logs in using account credentials.
4. Wallet operations are accessed through the dashboard menu.
5. Transactions are validated before execution.
6. Account balances are updated automatically.
7. Transaction details are recorded and stored permanently.
8. User data remains available across future sessions.

---

## Key Highlights

- Console-Based Digital Wallet Application
- Multi-User Support
- Secure PIN Authentication
- Persistent JSON Storage
- Transaction History Management
- Savings Goal Tracking
- Bill Payment Simulation
- Input Validation and Error Handling
- Modular Function-Based Design
- User-Friendly Menu-Driven Interface

---

## Author
Adrika Kumari

Developed as an academic Python project to simulate real-world digital wallet operations while applying Python programming, file handling, data management, and software design principles.
