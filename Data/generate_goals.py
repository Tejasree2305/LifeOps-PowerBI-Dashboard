import csv
import random
from datetime import date, timedelta

random.seed(400)

NUM_USERS = 200
NUM_GOALS = 3000

START_DATE = date(2025, 1, 1)
END_DATE = date(2025, 12, 31)

goal_types = [
    "Financial",
    "Health",
    "Learning",
    "Career",
    "Personal",
    "Productivity"
]

goal_names = {
    "Financial": [
        "Save Emergency Fund",
        "Reduce Monthly Expenses",
        "Increase Savings",
        "Build Investment Fund"
    ],
    "Health": [
        "Exercise Regularly",
        "Improve Sleep",
        "Walk Daily",
        "Improve Fitness"
    ],
    "Learning": [
        "Complete Python Course",
        "Learn SQL",
        "Learn Power BI",
        "Complete Certification"
    ],
    "Career": [
        "Build Portfolio",
        "Apply for Jobs",
        "Improve Resume",
        "Learn New Skill"
    ],
    "Personal": [
        "Read More Books",
        "Develop New Hobby",
        "Travel More",
        "Improve Work-Life Balance"
    ],
    "Productivity": [
        "Improve Productivity",
        "Increase Deep Work",
        "Reduce Screen Time",
        "Complete Tasks on Time"
    ]
}

priorities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

statuses = [
    "Not Started",
    "In Progress",
    "Completed",
    "Overdue",
    "Cancelled"
]

with open("Goals.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "GoalID",
        "UserID",
        "GoalDate",
        "GoalType",
        "GoalName",
        "Priority",
        "TargetValue",
        "CurrentValue",
        "Deadline",
        "GoalStatus"
    ])

    for i in range(1, NUM_GOALS + 1):

        goal_id = f"G{i:06d}"

        user_number = random.randint(1, NUM_USERS)

        user_id = f"U{user_number:03d}"

        goal_date = START_DATE + timedelta(
            days=random.randint(0, 250)
        )

        goal_type = random.choice(goal_types)

        goal_name = random.choice(
            goal_names[goal_type]
        )

        priority = random.choices(
            priorities,
            weights=[20, 45, 30, 5]
        )[0]

        # Target values based on goal type
        if goal_type == "Financial":

            target_value = random.choice([
                10000,
                25000,
                50000,
                100000,
                200000
            ])

        elif goal_type == "Health":

            target_value = random.choice([
                30,
                60,
                100,
                150,
                200
            ])

        elif goal_type == "Learning":

            target_value = random.choice([
                20,
                40,
                60,
                100,
                150
            ])

        elif goal_type == "Career":

            target_value = random.choice([
                5,
                10,
                20,
                30,
                50
            ])

        elif goal_type == "Personal":

            target_value = random.choice([
                5,
                10,
                20,
                30,
                50
            ])

        else:

            target_value = random.choice([
                20,
                40,
                60,
                80,
                100
            ])

        # Generate progress
        progress_percentage = random.uniform(
            0,
            1.2
        )

        current_value = round(
            target_value * progress_percentage,
            2
        )

        # Deadline
        deadline = goal_date + timedelta(
            days=random.randint(30, 180)
        )

        if deadline > END_DATE:
            deadline = END_DATE

        # Determine status
        if current_value >= target_value:

            goal_status = "Completed"

            current_value = target_value

        elif deadline < date(2025, 8, 30):

            goal_status = random.choice([
                "Overdue",
                "In Progress"
            ])

        else:

            goal_status = random.choices(
                [
                    "Not Started",
                    "In Progress",
                    "Cancelled"
                ],
                weights=[15, 75, 10]
            )[0]

        writer.writerow([
            goal_id,
            user_id,
            goal_date,
            goal_type,
            goal_name,
            priority,
            target_value,
            current_value,
            deadline,
            goal_status
        ])

print("Goals.csv created successfully!")
print("Total goals:", NUM_GOALS)