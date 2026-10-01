import csv
import random
from datetime import date, timedelta

random.seed(100)

# Number of users
NUM_USERS = 200

# Start date
START_DATE = date(2025, 1, 1)

# Number of days
NUM_DAYS = 365

# Output file
OUTPUT_FILE = "DailyActivity.csv"


with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Column headers
    writer.writerow([
        "ActivityID",
        "UserID",
        "ActivityDate",
        "StudyHours",
        "WorkHours",
        "DeepWorkHours",
        "MeetingHours",
        "ExerciseHours",
        "LeisureHours",
        "SleepHours",
        "ProductivityScore"
    ])

    activity_number = 1

    # Generate data for every user
    for user_number in range(1, NUM_USERS + 1):

        user_id = f"U{user_number:03d}"

        # Generate data for every day
        for day_number in range(NUM_DAYS):

            activity_date = START_DATE + timedelta(days=day_number)

            # Weekend check
            is_weekend = activity_date.weekday() >= 5

            if is_weekend:

                study_hours = round(random.uniform(0.5, 4.0), 1)
                work_hours = round(random.uniform(0.0, 3.0), 1)
                meeting_hours = round(random.uniform(0.0, 1.5), 1)

            else:

                study_hours = round(random.uniform(1.0, 5.0), 1)
                work_hours = round(random.uniform(4.0, 9.0), 1)
                meeting_hours = round(random.uniform(0.5, 3.0), 1)

            # Deep work should normally be lower than total work/study
            deep_work_hours = round(
                random.uniform(
                    0.5,
                    min(4.0, study_hours + work_hours)
                ),
                1
            )

            exercise_hours = round(random.uniform(0.0, 1.5), 1)

            leisure_hours = round(random.uniform(1.0, 5.0), 1)

            sleep_hours = round(random.uniform(5.5, 9.0), 1)

            # Productivity calculation
            productivity = (
                deep_work_hours * 10
                + exercise_hours * 8
                + sleep_hours * 4
                - meeting_hours * 5
                - leisure_hours * 2
            )

            # Add a small random variation
            productivity += random.uniform(-5, 5)

            # Convert to 0-100 range
            productivity_score = max(
                0,
                min(100, round(productivity, 1))
            )

            activity_id = f"A{activity_number:06d}"

            writer.writerow([
                activity_id,
                user_id,
                activity_date,
                study_hours,
                work_hours,
                deep_work_hours,
                meeting_hours,
                exercise_hours,
                leisure_hours,
                sleep_hours,
                productivity_score
            ])

            activity_number += 1


print("DailyActivity.csv created successfully!")
print("Total records:", NUM_USERS * NUM_DAYS)