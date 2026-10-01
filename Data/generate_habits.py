import csv
import random
from datetime import date, timedelta

random.seed(600)

NUM_USERS = 200
NUM_RECORDS = 30000

START_DATE = date(2025, 1, 1)

habits = {
    "Health": [
        "Exercise",
        "Walking",
        "Water Intake",
        "Healthy Eating"
    ],
    "Learning": [
        "Reading",
        "Coding Practice",
        "Study",
        "Skill Practice"
    ],
    "Wellness": [
        "Meditation",
        "Journaling",
        "Digital Detox"
    ],
    "Productivity": [
        "Deep Work",
        "Screen Time Control",
        "Planning"
    ],
    "Lifestyle": [
        "Sleep",
        "Wake Up Early",
        "Outdoor Time"
    ]
}

with open("Habits.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "HabitID",
        "UserID",
        "HabitDate",
        "HabitName",
        "HabitCategory",
        "TargetValue",
        "ActualValue",
        "CompletionStatus",
        "StreakDays"
    ])

    streak_tracker = {}

    for i in range(1, NUM_RECORDS + 1):

        habit_id = f"H{i:06d}"

        user_number = random.randint(1, NUM_USERS)

        user_id = f"U{user_number:03d}"

        habit_date = START_DATE + timedelta(
            days=random.randint(0, 364)
        )

        category = random.choice(
            list(habits.keys())
        )

        habit_name = random.choice(
            habits[category]
        )

        # Different habits have different targets

        if habit_name == "Exercise":
            target_value = 60

        elif habit_name == "Walking":
            target_value = 30

        elif habit_name == "Water Intake":
            target_value = 8

        elif habit_name == "Healthy Eating":
            target_value = 3

        elif habit_name == "Reading":
            target_value = 30

        elif habit_name == "Coding Practice":
            target_value = 60

        elif habit_name == "Study":
            target_value = 120

        elif habit_name == "Skill Practice":
            target_value = 60

        elif habit_name == "Meditation":
            target_value = 15

        elif habit_name == "Journaling":
            target_value = 15

        elif habit_name == "Digital Detox":
            target_value = 60

        elif habit_name == "Deep Work":
            target_value = 120

        elif habit_name == "Screen Time Control":
            target_value = 180

        elif habit_name == "Planning":
            target_value = 15

        elif habit_name == "Sleep":
            target_value = 8

        elif habit_name == "Wake Up Early":
            target_value = 1

        else:
            target_value = 60

        # Generate completion status

        status = random.choices(
            [
                "Completed",
                "Partial",
                "Missed"
            ],
            weights=[
                55,
                30,
                15
            ]
        )[0]

        if status == "Completed":

            actual_value = round(
                target_value *
                random.uniform(1.0, 1.3),
                1
            )

        elif status == "Partial":

            actual_value = round(
                target_value *
                random.uniform(0.3, 0.9),
                1
            )

        else:

            actual_value = 0

        # Generate a realistic-looking streak

        if status == "Completed":

            streak_days = random.randint(
                1,
                30
            )

        elif status == "Partial":

            streak_days = random.randint(
                0,
                15
            )

        else:

            streak_days = 0

        writer.writerow([
            habit_id,
            user_id,
            habit_date,
            habit_name,
            category,
            target_value,
            actual_value,
            status,
            streak_days
        ])

print("Habits.csv created successfully!")
print("Total habit records:", NUM_RECORDS)