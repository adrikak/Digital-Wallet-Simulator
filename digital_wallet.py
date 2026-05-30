"""
Digital Wallet Simulator
"""

import json
import time
from datetime import datetime

TRAVERSE_MODE = False

CATEGORIES = [
    "Food",
    "Travel",
    "Bills",
    "Shopping",
    "Education",
    "Health",
    "Other"
]

locked_accounts = set()

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
                    "category": "Other",
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

    return {
        "id": str(int(time.time() * 1000)),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": txn_type,
        "amount": round(float(amount), 2),
        "note": note,
        "category": category,
        "counterparty": counterparty
    }


def valid_pin(pin):

    return len(pin) == 4 and pin.isdigit()


def valid_amount(amount):

    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except:
        return False


def create_account(d):

    print("\n" + "=" * 40)
    print("CREATE ACCOUNT")
    print("=" * 40)

    username = input("Enter username: ").strip().lower()

    if username == "":
        print("Username cannot be empty.")
        return

    if " " in username:
        print("Username cannot contain spaces.")
        return

    if username in d["accounts"]:
        print("Username already exists.")
        return

    pin = input("Enter 4-digit PIN: ").strip()

    if not valid_pin(pin):
        print("PIN must be exactly 4 digits.")
        return

    d["accounts"][username] = {
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    print("Account created successfully.")


def login(d):

    print("\n" + "=" * 40)
    print("LOGIN")
    print("=" * 40)

    username = input("Username: ").strip().lower()

    if username not in d["accounts"]:
        print("Username not found.")
        return None

    if username in locked_accounts:
        print("Account locked. Restart program.")
        return None

    attempts = 0

    while attempts < 3:

        pin = input("PIN: ").strip()

        if pin == d["accounts"][username]["pin"]:
            print("Login successful.")
            return username

        attempts += 1

        print(f"Incorrect PIN. Attempts left: {3 - attempts}")

    locked_accounts.add(username)

    print("Account locked after 3 failed attempts.")

    return None

def change_pin(d, username):

    print("\n" + "=" * 40)
    print("CHANGE PIN")
    print("=" * 40)

    old_pin = input("Enter current PIN: ").strip()

    if old_pin != d["accounts"][username]["pin"]:
        print("Incorrect PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()

    if not valid_pin(new_pin):
        print("PIN must be exactly 4 digits.")
        return

    d["accounts"][username]["pin"] = new_pin

    print("PIN changed successfully.")


def show_balance(d, username):

    balance = d["accounts"][username]["balance"]

    print("\n" + "=" * 40)
    print("CURRENT BALANCE")
    print("=" * 40)
    print(f"Balance : ₹{balance:.2f}")


def deposit(d, username):

    print("\n" + "=" * 40)
    print("ADD MONEY")
    print("=" * 40)

    amount = input("Enter amount: ")

    if not valid_amount(amount):
        print("Amount must be positive.")
        return

    amount = float(amount)

    note = input("Enter note: ").strip()

    account = d["accounts"][username]

    account["balance"] += amount

    txn = make_txn(
        "deposit",
        amount,
        note,
        None,
        "self"
    )

    account["transactions"].append(txn)

    print(f"₹{amount:.2f} added successfully.")
    print(f"New Balance : ₹{account['balance']:.2f}")


def withdraw(d, username):

    print("\n" + "=" * 40)
    print("WITHDRAW MONEY")
    print("=" * 40)

    amount = input("Enter amount: ")

    if not valid_amount(amount):
        print("Amount must be positive.")
        return

    amount = float(amount)

    account = d["accounts"][username]

    if amount > account["balance"]:
        print("Insufficient Balance.")
        return

    print("\nExpense Categories")

    for i in range(len(CATEGORIES)):
        print(f"{i + 1}. {CATEGORIES[i]}")

    choice = input("Choose category: ")

    if not choice.isdigit():
        print("Invalid category.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(CATEGORIES):
        print("Invalid category.")
        return

    category = CATEGORIES[choice - 1]

    note = input("Enter note: ").strip()

    account["balance"] -= amount

    txn = make_txn(
        "withdraw",
        amount,
        note,
        category,
        "cash"
    )

    account["transactions"].append(txn)

    print("Withdrawal successful.")
    print(f"Remaining Balance : ₹{account['balance']:.2f}")


def transfer(d, sender):

    print("\n" + "=" * 40)
    print("UPI TRANSFER")
    print("=" * 40)

    receiver = input("Enter receiver username: ").strip().lower()

    if receiver not in d["accounts"]:
        print("Username not found.")
        return

    if receiver == sender:
        print("Cannot transfer to yourself.")
        return

    amount = input("Enter amount: ")

    if not valid_amount(amount):
        print("Amount must be positive.")
        return

    amount = float(amount)

    sender_account = d["accounts"][sender]

    if amount > sender_account["balance"]:
        print("Insufficient Balance.")
        return

    pin = input("Confirm PIN: ").strip()

    if pin != sender_account["pin"]:
        print("Incorrect PIN.")
        return

    print("\nExpense Categories")

    for i in range(len(CATEGORIES)):
        print(f"{i + 1}. {CATEGORIES[i]}")

    choice = input("Choose category: ")

    if not choice.isdigit():
        print("Invalid category.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(CATEGORIES):
        print("Invalid category.")
        return

    category = CATEGORIES[choice - 1]

    note = input("Enter note: ").strip()

    sender_account["balance"] -= amount
    d["accounts"][receiver]["balance"] += amount

    sender_txn = make_txn(
        "transfer_out",
        amount,
        note,
        category,
        receiver
    )

    receiver_txn = make_txn(
        "transfer_in",
        amount,
        note,
        None,
        sender
    )

    sender_account["transactions"].append(sender_txn)
    d["accounts"][receiver]["transactions"].append(receiver_txn)

    print("\nTransfer Successful")
    print(f"Sent ₹{amount:.2f} to {receiver}")
    print(f"Remaining Balance : ₹{sender_account['balance']:.2f}")

def qr_generate(d, username):

    print("\n" + "=" * 40)
    print("GENERATE QR PAYMENT REQUEST")
    print("=" * 40)

    amount = input("Enter amount to request: ")

    if not valid_amount(amount):
        print("Amount must be positive.")
        return

    amount = float(amount)

    note = input("Enter note: ").strip()

    payload = {
        "receiver": username,
        "amount": amount,
        "note": note
    }

    payload_text = json.dumps(payload)

    print("\n" + "=" * 50)
    print("DIGITAL WALLET QR")
    print("=" * 50)
    print(f"Receiver : {username}")
    print(f"Amount   : ₹{amount:.2f}")
    print(f"Note     : {note}")
    print("-" * 50)
    print("QR Payload")
    print(payload_text)
    print("-" * 50)
    print("Copy the payload and send it to payer.")
    print("=" * 50)


def qr_pay(d, payer):

    print("\n" + "=" * 40)
    print("PAY USING QR")
    print("=" * 40)

    payload_text = input("Paste QR Payload: ").strip()

    try:
        payload = json.loads(payload_text)

    except:
        print("Invalid QR Payload.")
        return

    if "receiver" not in payload:
        print("Invalid QR Payload.")
        return

    if "amount" not in payload:
        print("Invalid QR Payload.")
        return

    receiver = str(payload["receiver"]).lower()

    if receiver not in d["accounts"]:
        print("Receiver account not found.")
        return

    if receiver == payer:
        print("Cannot pay yourself.")
        return

    try:
        amount = float(payload["amount"])

    except:
        print("Invalid amount in QR.")
        return

    if amount <= 0:
        print("Invalid amount in QR.")
        return

    note = payload.get("note", "")

    payer_account = d["accounts"][payer]

    if amount > payer_account["balance"]:
        print("Insufficient Balance.")
        return

    pin = input("Confirm PIN: ").strip()

    if pin != payer_account["pin"]:
        print("Incorrect PIN.")
        return

    print("\nExpense Categories")

    for i in range(len(CATEGORIES)):
        print(f"{i + 1}. {CATEGORIES[i]}")

    choice = input("Choose category: ")

    if not choice.isdigit():
        print("Invalid category.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(CATEGORIES):
        print("Invalid category.")
        return

    category = CATEGORIES[choice - 1]

    payer_account["balance"] -= amount
    d["accounts"][receiver]["balance"] += amount

    payer_txn = make_txn(
        "qr_out",
        amount,
        note,
        category,
        receiver
    )

    receiver_txn = make_txn(
        "qr_in",
        amount,
        note,
        None,
        payer
    )

    payer_account["transactions"].append(payer_txn)
    d["accounts"][receiver]["transactions"].append(receiver_txn)

    print("\nQR Payment Successful")
    print(f"Paid ₹{amount:.2f} to {receiver}")
    print(f"Remaining Balance : ₹{payer_account['balance']:.2f}")


def show_transactions(d, username):

    print("\n" + "=" * 40)
    print("TRANSACTION HISTORY")
    print("=" * 40)

    transactions = d["accounts"][username]["transactions"]

    if len(transactions) == 0:
        print("No transactions found.")
        return

    for txn in transactions:

        print("\n" + "-" * 60)
        print("Transaction ID :", txn["id"])
        print("Time           :", txn["timestamp"])
        print("Type           :", txn["type"])
        print("Amount         : ₹" + str(txn["amount"]))
        print("Counterparty   :", txn["counterparty"])
        print("Category       :", txn["category"])
        print("Note           :", txn["note"])

    print("\n" + "-" * 60)
    print("Total Transactions :", len(transactions))

def report_category_spend(d, username):

    print("\n" + "=" * 40)
    print("CATEGORY SPENDING REPORT")
    print("=" * 40)

    totals = {}

    for category in CATEGORIES:
        totals[category] = 0

    transactions = d["accounts"][username]["transactions"]

    for txn in transactions:

        if txn["type"] == "transfer_out" or \
           txn["type"] == "qr_out" or \
           txn["type"] == "withdraw":

            category = txn["category"]

            if category in totals:
                totals[category] += txn["amount"]

    found = False

    for category in totals:

        if totals[category] > 0:
            found = True

    if not found:
        print("No spending data available.")
        return

    print()

    grand_total = 0

    for category in totals:

        amount = totals[category]

        print(f"{category:<12} : ₹{amount:.2f}")

        grand_total += amount

    print("-" * 30)
    print(f"Total Spend : ₹{grand_total:.2f}")


def report_monthly_summary(d, username):

    print("\n" + "=" * 40)
    print("MONTHLY SUMMARY REPORT")
    print("=" * 40)

    summary = {}

    transactions = d["accounts"][username]["transactions"]

    for txn in transactions:

        month = txn["timestamp"][:7]

        if month not in summary:

            summary[month] = {
                "inflow": 0,
                "outflow": 0
            }

        if txn["type"] == "deposit" or \
           txn["type"] == "transfer_in" or \
           txn["type"] == "qr_in":

            summary[month]["inflow"] += txn["amount"]

        elif txn["type"] == "withdraw" or \
             txn["type"] == "transfer_out" or \
             txn["type"] == "qr_out":

            summary[month]["outflow"] += txn["amount"]

    if len(summary) == 0:
        print("No transactions found.")
        return

    print()

    print("-" * 45)
    print("Month      Inflow       Outflow")
    print("-" * 45)

    for month in sorted(summary):

        inflow = summary[month]["inflow"]
        outflow = summary[month]["outflow"]

        print(
            f"{month:<10} ₹{inflow:<10.2f} ₹{outflow:<10.2f}"
        )

    print("-" * 45)


def report_top_payees(d, username):

    print("\n" + "=" * 40)
    print("TOP PAYEES REPORT")
    print("=" * 40)

    payees = {}

    transactions = d["accounts"][username]["transactions"]

    for txn in transactions:

        if txn["type"] != "transfer_out" and \
           txn["type"] != "qr_out":
            continue

        person = txn["counterparty"]

        if person not in payees:

            payees[person] = {
                "count": 0,
                "amount": 0
            }

        payees[person]["count"] += 1
        payees[person]["amount"] += txn["amount"]

    if len(payees) == 0:
        print("No outgoing payments found.")
        return

    ranking = []

    for person in payees:

        ranking.append([
            person,
            payees[person]["count"],
            payees[person]["amount"]
        ])

    for i in range(len(ranking)):

        for j in range(i + 1, len(ranking)):

            if ranking[j][2] > ranking[i][2]:

                temp = ranking[i]
                ranking[i] = ranking[j]
                ranking[j] = temp

    print()

    print("-" * 60)
    print("Rank  User        Transactions    Amount")
    print("-" * 60)

    position = 1

    for item in ranking:

        person = item[0]
        count = item[1]
        amount = item[2]

        print(
            f"{position:<5} "
            f"{person:<12} "
            f"{count:<15} "
            f"₹{amount:.2f}"
        )

        position += 1

    print("-" * 60)

def user_menu():

    print("""
==================================================
                DIGITAL WALLET
==================================================
1. Add Money (Deposit)
2. Withdraw Money
3. Show Balance
4. Transfer (UPI)
5. Generate QR to Receive Payment
6. Pay via QR
7. Transaction History
8. Report: Spend by Category
9. Report: Monthly In/Out
10. Report: Top Payees
11. Change PIN
0. Logout
==================================================
""")


def main_menu():

    print("""
==================================================
          DIGITAL WALLET SIMULATOR
==================================================
1. Create Account
2. Login
0. Exit
==================================================
""")


def main():

    d = data

    print("\nWelcome to Digital Wallet Simulator")

    while True:

        main_menu()

        choice = input("Choose: ").strip()

        if choice == "1":

            create_account(d)

        elif choice == "2":

            user = login(d)

            if not user:
                continue

            while True:

                user_menu()

                option = input("Choose: ").strip()

                if option == "1":

                    deposit(d, user)

                elif option == "2":

                    withdraw(d, user)

                elif option == "3":

                    show_balance(d, user)

                elif option == "4":

                    transfer(d, user)

                elif option == "5":

                    qr_generate(d, user)

                elif option == "6":

                    qr_pay(d, user)

                elif option == "7":

                    show_transactions(d, user)

                elif option == "8":

                    report_category_spend(d, user)

                elif option == "9":

                    report_monthly_summary(d, user)

                elif option == "10":

                    report_top_payees(d, user)

                elif option == "11":

                    change_pin(d, user)

                elif option == "0":

                    print("\nLogging out...\n")
                    break

                else:

                    print("Invalid choice.")

        elif choice == "0":

            print("\nThank you for using Digital Wallet Simulator.")
            print("Goodbye!")

            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()