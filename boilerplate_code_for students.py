"""
Digital Wallet (UPI-style)

Purpose: Menus are runnable; However Students have to implement all the functions themselves (Mentos Zindagi).

Compiled by : Sanket Dodya

"""

import json
import time
from datetime import datetime

TRAVERSE_MODE = True

CATEGORIES = ["Food", "Travel", "Bills", "Shopping", "Education", "Health", "Other"]

# Mock data Base for you Guys !!!!!
data = {
    "accounts": {
        "alice": {
            "pin": "1111",
            "balance": 830.0,
            "transactions": [
                {
                    "id": "tx-a1",
                    "timestamp": "2025-09-20 09:30:05",
                    "type": "deposit",
                    "amount": 1000.0,
                    "note": "Initial top-up",
                    "category": None,
                    "counterparty": "self"
                },
                {
                    "id": "tx-a2",
                    "timestamp": "2025-09-20 10:05:12",
                    "type": "transfer_out",
                    "amount": 250.0,
                    "note": "Lunch split",
                    "category": "Food",
                    "counterparty": "bob"
                },
                {
                    "id": "tx-a3",
                    "timestamp": "2025-09-21 18:22:40",
                    "type": "qr_out",
                    "amount": 120.0,
                    "note": "Movie tickets",
                    "category": "Entertainment",
                    "counterparty": "charlie"
                },
                {
                    "id": "tx-a4",
                    "timestamp": "2025-09-22 08:10:01",
                    "type": "withdraw",
                    "amount": 100.0,
                    "note": "Cash",
                    "category": "Other",
                    "counterparty": "cash"
                },
                {
                    "id": "tx-a5",
                    "timestamp": "2025-09-23 12:45:33",
                    "type": "transfer_in",
                    "amount": 300.0,
                    "note": "Project reimbursement",
                    "category": None,
                    "counterparty": "disha"
                }
            ]
        },
        "bob": {
            "pin": "2222",
            "balance": 625.0,
            "transactions": [
                {
                    "id": "tx-b1",
                    "timestamp": "2025-09-19 12:00:00",
                    "type": "deposit",
                    "amount": 500.0,
                    "note": "Bank add",
                    "category": None,
                    "counterparty": "self"
                },
                {
                    "id": "tx-b2",
                    "timestamp": "2025-09-20 10:05:12",
                    "type": "transfer_in",
                    "amount": 250.0,
                    "note": "Lunch split",
                    "category": None,
                    "counterparty": "alice"
                },
                {
                    "id": "tx-b3",
                    "timestamp": "2025-09-21 18:23:10",
                    "type": "qr_in",
                    "amount": 75.0,
                    "note": "Snacks",
                    "category": None,
                    "counterparty": "charlie"
                },
                {
                    "id": "tx-b4",
                    "timestamp": "2025-09-22 20:05:49",
                    "type": "transfer_out",
                    "amount": 200.0,
                    "note": "Gift",
                    "category": "Shopping",
                    "counterparty": "disha"
                }
            ]
        },
        "charlie": {
            "pin": "3333",
            "balance": 300.0,
            "transactions": [
                {
                    "id": "tx-c1",
                    "timestamp": "2025-09-19 09:10:20",
                    "type": "deposit",
                    "amount": 300.0,
                    "note": "Pocket money",
                    "category": None,
                    "counterparty": "self"
                },
                {
                    "id": "tx-c2",
                    "timestamp": "2025-09-21 18:23:10",
                    "type": "qr_out",
                    "amount": 75.0,
                    "note": "Snacks",
                    "category": "Food",
                    "counterparty": "bob"
                },
                {
                    "id": "tx-c3",
                    "timestamp": "2025-09-21 18:22:40",
                    "type": "qr_in",
                    "amount": 120.0,
                    "note": "Movie tickets",
                    "category": None,
                    "counterparty": "alice"
                },
                {
                    "id": "tx-c4",
                    "timestamp": "2025-09-22 21:00:03",
                    "type": "withdraw",
                    "amount": 45.0,
                    "note": "Auto fare",
                    "category": "Travel",
                    "counterparty": "cash"
                }
            ]
        },
        "disha": {
            "pin": "4444",
            "balance": 100.0,
            "transactions": [
                {
                    "id": "tx-d1",
                    "timestamp": "2025-09-19 08:00:00",
                    "type": "deposit",
                    "amount": 200.0,
                    "note": "Initial load",
                    "category": None,
                    "counterparty": "self"
                },
                {
                    "id": "tx-d2",
                    "timestamp": "2025-09-22 20:05:49",
                    "type": "transfer_in",
                    "amount": 200.0,
                    "note": "Gift",
                    "category": None,
                    "counterparty": "bob"
                },
                {
                    "id": "tx-d3",
                    "timestamp": "2025-09-23 12:45:33",
                    "type": "transfer_out",
                    "amount": 300.0,
                    "note": "Project reimbursement",
                    "category": "Bills",
                    "counterparty": "alice"
                }
            ]
        }
    }
}

def make_txn(txn_type, amount, note, category, counterparty):
    """Create a transaction dict (optional helper to reuse)."""
    return {
        "id": str(int(time.time() * 1000)),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": txn_type,
        "amount": round(float(amount), 2),
        "note": note,
        "category": category,
        "counterparty": counterparty
    }

# ----------------- You Guys Have to Implement this  -------------------

def create_account(d):
    """B1: Create username + 4-digit PIN; init balance & transactions."""
    print(" NOt Implemented B1: create_account")

def login(d):
    """B2: Validate username exists and PIN in ≤3 attempts; return username."""
    if TRAVERSE_MODE:
        return input("Username (traverse mode): ").strip().lower()

def change_pin(d, username):
    """B3: Verify old PIN; set new 4-digit PIN."""
    print(" NOt Implemented B3: change_pin")

def deposit(d, username):
    """C1: Add money; record 'deposit' transaction."""
    print(" NOt Implemented C1: deposit")

def withdraw(d, username):
    """C2: Withdraw with sufficient balance check; record 'withdraw'."""
    print(" NOt Implemented C2: withdraw")

def transfer(d, sender):
    """D1: Sender→Receiver transfer; confirm PIN; record out/in transactions."""
    print(" NOt Implemented D1: transfer")

def qr_generate(d, username):
    """E1/E2: Print compact JSON payload to request a payment (QR simulation)."""
    print(" NOt Implemented E2: qr_generate")

def qr_pay(d, payer):
    """E3: Parse payload, confirm funds & PIN, move money; record qr_out/qr_in."""
    print(" NOt Implemented E3: qr_pay")

def show_transactions(d, username):
    """F1: Print user's transactions (id, time, type, amount, cp, category, note)."""
    print(" NOt Implemented F1: show_transactions")

def report_category_spend(d, username):
    """F2: Sum outgoing by category (transfer_out, qr_out, withdraw)."""
    print(" NOt Implemented F2: report_category_spend")

def report_monthly_summary(d, username):
    """F3: YYYY-MM wise inflow vs outflow totals."""
    print(" NOt Implemented F3: report_monthly_summary")

def report_top_payees(d, username):
    """F4: Rank counterparties by count and total for outgoing transfers."""
    print(" NOt Implemented F4: report_top_payees")

def show_balance(d, username):
    """Show current balance for user."""
    print(" NOt Implemented Balance: show_balance")

# ----------------- Menus -----------------

def user_menu():
    print("""
==== Digital Wallet ====
1. Add Money (Deposit)
2. Withdraw Money
3. Show Balance
4. Transfer (UPI)
5. Generate QR to Receive Payment
6. Pay via QR (scan/paste payload)
7. Transaction History
8. Report: Spend by Category
9. Report: Monthly In/Out
10. Report: Top Payees
11. Change PIN
0. Logout
""")

def main_menu():
    print("""
==== Welcome ====
1. Create Account
2. Login
0. Exit
""")

# ----------------- Main loop -----------------

def main():
    d = data
    while True:
        main_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                create_account(d)
            except NotImplementedError as e:
                print(e)
        elif choice == "2":
            try:
                user = login(d)
            except NotImplementedError as e:
                print(e)
                continue
            if not user:
                continue
            while True:
                user_menu()
                c = input("Choose: ").strip()
                try:
                    if c == "1":
                        deposit(d, user)
                    elif c == "2":
                        withdraw(d, user)
                    elif c == "3":
                        show_balance(d, user)
                    elif c == "4":
                        transfer(d, user)
                    elif c == "5":
                        qr_generate(d, user)
                    elif c == "6":
                        qr_pay(d, user)
                    elif c == "7":
                        show_transactions(d, user)
                    elif c == "8":
                        report_category_spend(d, user)
                    elif c == "9":
                        report_monthly_summary(d, user)
                    elif c == "10":
                        report_top_payees(d, user)
                    elif c == "11":
                        change_pin(d, user)
                    elif c == "0":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")
                except NotImplementedError as e:
                    print(e)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
