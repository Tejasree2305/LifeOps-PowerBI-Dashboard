import csv
import random
from datetime import date, timedelta

random.seed(300)

NUM_USERS = 200
NUM_TRANSACTIONS = 20000

START_DATE = date(2025, 1, 1)

expense_categories = {
    "Food": [
        "Groceries",
        "Restaurants",
        "Food Delivery"
    ],
    "Transport": [
        "Fuel",
        "Public Transport",
        "Taxi"
    ],
    "Housing": [
        "Rent",
        "Maintenance"
    ],
    "Utilities": [
        "Electricity",
        "Internet",
        "Mobile"
    ],
    "Shopping": [
        "Clothing",
        "Electronics",
        "Personal Care"
    ],
    "Entertainment": [
        "Movies",
        "Gaming",
        "Streaming"
    ],
    "Healthcare": [
        "Medicine",
        "Doctor",
        "Health Checkup"
    ],
    "Education": [
        "Courses",
        "Books",
        "Certifications"
    ],
    "Travel": [
        "Hotels",
        "Flights",
        "Travel"
    ]
}

income_categories = {
    "Salary": [
        "Monthly Salary"
    ],
    "Freelance": [
        "Freelance Income"
    ],
    "Investment": [
        "Investment Return"
    ]
}

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Bank Transfer"
]

with open("Expenses.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "TransactionID",
        "UserID",
        "TransactionDate",
        "TransactionType",
        "Category",
        "SubCategory",
        "Amount",
        "PaymentMethod",
        "IsRecurring",
        "IsEssential"
    ])

    for i in range(1, NUM_TRANSACTIONS + 1):

        transaction_id = f"E{i:06d}"

        user_number = random.randint(1, NUM_USERS)

        user_id = f"U{user_number:03d}"

        transaction_date = START_DATE + timedelta(
            days=random.randint(0, 364)
        )

        # Decide whether transaction is income or expense
        transaction_type = random.choices(
            ["Income", "Expense"],
            weights=[15, 85]
        )[0]

        if transaction_type == "Income":

            category = random.choice(
                list(income_categories.keys())
            )

            subcategory = random.choice(
                income_categories[category]
            )

            if category == "Salary":
                amount = round(
                    random.uniform(25000, 90000),
                    2
                )

                is_recurring = "Yes"

            elif category == "Freelance":
                amount = round(
                    random.uniform(3000, 30000),
                    2
                )

                is_recurring = random.choice(
                    ["Yes", "No"]
                )

            else:
                amount = round(
                    random.uniform(1000, 15000),
                    2
                )

                is_recurring = "No"

            payment_method = "Bank Transfer"

            is_essential = "Yes"

        else:

            category = random.choice(
                list(expense_categories.keys())
            )

            subcategory = random.choice(
                expense_categories[category]
            )

            # Different categories have different spending ranges

            if category == "Housing":

                amount = round(
                    random.uniform(5000, 30000),
                    2
                )

                is_recurring = "Yes"

                is_essential = "Yes"

            elif category == "Utilities":

                amount = round(
                    random.uniform(500, 5000),
                    2
                )

                is_recurring = random.choice(
                    ["Yes", "No"]
                )

                is_essential = "Yes"

            elif category == "Healthcare":

                amount = round(
                    random.uniform(300, 8000),
                    2
                )

                is_recurring = "No"

                is_essential = "Yes"

            elif category == "Education":

                amount = round(
                    random.uniform(500, 15000),
                    2
                )

                is_recurring = "No"

                is_essential = "Yes"

            elif category == "Food":

                amount = round(
                    random.uniform(100, 3000),
                    2
                )

                is_recurring = "No"

                if subcategory == "Groceries":
                    is_essential = "Yes"
                else:
                    is_essential = "No"

            elif category == "Transport":

                amount = round(
                    random.uniform(100, 5000),
                    2
                )

                is_recurring = "No"

                is_essential = "Yes"

            elif category == "Shopping":

                amount = round(
                    random.uniform(300, 10000),
                    2
                )

                is_recurring = "No"

                is_essential = "No"

            elif category == "Entertainment":

                amount = round(
                    random.uniform(200, 5000),
                    2
                )

                is_recurring = random.choice(
                    ["Yes", "No"]
                )

                is_essential = "No"

            else:

                amount = round(
                    random.uniform(1000, 30000),
                    2
                )

                is_recurring = "No"

                is_essential = "No"

            payment_method = random.choice(
                payment_methods
            )

        writer.writerow([
            transaction_id,
            user_id,
            transaction_date,
            transaction_type,
            category,
            subcategory,
            amount,
            payment_method,
            is_recurring,
            is_essential
        ])

print("Expenses.csv created successfully!")
print("Total transactions:", NUM_TRANSACTIONS)