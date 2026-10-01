import csv
import random
from datetime import date, timedelta

random.seed(500)

NUM_USERS = 200
NUM_RECORDS = 10000

START_DATE = date(2025, 1, 1)

skills = [
    "SQL",
    "Python",
    "Excel",
    "Power BI",
    "Data Analytics",
    "Machine Learning",
    "Communication",
    "Cloud",
    "ServiceNow",
    "Java"
]

course_types = [
    "Online Course",
    "Certification",
    "Project",
    "Workshop",
    "Self Learning"
]

difficulty_levels = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

statuses = [
    "Not Started",
    "In Progress",
    "Completed",
    "Dropped"
]

with open("Learning.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "LearningID",
        "UserID",
        "LearningDate",
        "Skill",
        "CourseType",
        "HoursSpent",
        "AssessmentScore",
        "CompletionPercent",
        "LearningStatus",
        "DifficultyLevel"
    ])

    for i in range(1, NUM_RECORDS + 1):

        learning_id = f"L{i:06d}"

        user_number = random.randint(1, NUM_USERS)

        user_id = f"U{user_number:03d}"

        learning_date = START_DATE + timedelta(
            days=random.randint(0, 364)
        )

        skill = random.choice(skills)

        course_type = random.choice(course_types)

        difficulty = random.choice(
            difficulty_levels
        )

        hours_spent = round(
            random.uniform(0.5, 6.0),
            1
        )

        assessment_score = round(
            random.uniform(40, 100),
            1
        )

        completion_percent = round(
            random.uniform(0, 100),
            1
        )

        status = random.choices(
            statuses,
            weights=[10, 50, 30, 10]
        )[0]

        # Make status and completion logically consistent

        if status == "Completed":

            completion_percent = 100

            assessment_score = round(
                random.uniform(65, 100),
                1
            )

        elif status == "Not Started":

            completion_percent = 0

            hours_spent = 0

            assessment_score = 0

        elif status == "Dropped":

            completion_percent = round(
                random.uniform(10, 70),
                1
            )

        writer.writerow([
            learning_id,
            user_id,
            learning_date,
            skill,
            course_type,
            hours_spent,
            assessment_score,
            completion_percent,
            status,
            difficulty
        ])

print("Learning.csv created successfully!")
print("Total learning records:", NUM_RECORDS)