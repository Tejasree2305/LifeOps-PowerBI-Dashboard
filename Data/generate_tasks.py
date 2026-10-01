import csv
import random
from datetime import date, timedelta

random.seed(200)

NUM_USERS = 200
NUM_TASKS = 15000

START_DATE = date(2025, 1, 1)

categories = [
    "Work",
    "Learning",
    "Personal",
    "Health",
    "Finance",
    "Project"
]

priorities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

statuses = [
    "Completed",
    "Pending",
    "In Progress",
    "Cancelled",
    "Overdue"
]

with open("Tasks.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "TaskID",
        "UserID",
        "TaskDate",
        "TaskCategory",
        "Priority",
        "TaskStatus",
        "DueDate",
        "CompletionDate",
        "EstimatedHours",
        "ActualHours",
        "IsOverdue"
    ])

    for i in range(1, NUM_TASKS + 1):

        task_id = f"T{i:06d}"

        user_number = random.randint(1, NUM_USERS)

        user_id = f"U{user_number:03d}"

        task_date = START_DATE + timedelta(
            days=random.randint(0, 364)
        )

        category = random.choice(categories)

        priority = random.choices(
            priorities,
            weights=[20, 45, 30, 5]
        )[0]

        # Estimated time
        estimated_hours = round(
            random.uniform(0.5, 8.0),
            1
        )

        # Select task status
        status = random.choices(
            statuses,
            weights=[55, 15, 15, 5, 10]
        )[0]

        # Due date
        due_date = task_date + timedelta(
            days=random.randint(1, 14)
        )

        completion_date = ""

        if status == "Completed":

            completion_date = task_date + timedelta(
                days=random.randint(0, 14)
            )

            # Make sure completion date is not too far
            if completion_date > date(2025, 12, 31):
                completion_date = date(2025, 12, 31)

            actual_hours = round(
                estimated_hours *
                random.uniform(0.7, 1.5),
                1
            )

            # Completed tasks can still be late
            if completion_date > due_date:
                is_overdue = "Yes"
            else:
                is_overdue = "No"

        elif status == "Overdue":

            actual_hours = round(
                estimated_hours *
                random.uniform(0.8, 1.6),
                1
            )

            is_overdue = "Yes"

        else:

            actual_hours = 0

            is_overdue = "No"

        writer.writerow([
            task_id,
            user_id,
            task_date,
            category,
            priority,
            status,
            due_date,
            completion_date,
            estimated_hours,
            actual_hours,
            is_overdue
        ])

print("Tasks.csv created successfully!")
print("Total tasks:", NUM_TASKS)