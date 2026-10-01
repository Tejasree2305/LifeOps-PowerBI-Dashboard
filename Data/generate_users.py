import csv
import random

random.seed(42)

names = [
    "Aarav",
    "Aditi",
    "Arjun",
    "Ananya",
    "Rahul",
    "Priya",
    "Karthik",
    "Sneha",
    "Rohan",
    "Meera",
    "Vikram",
    "Pooja",
    "Sanjay",
    "Kavya",
    "Nikhil",
    "Divya",
    "Varun",
    "Ishita",
    "Aditya",
    "Neha"
]

cities = [
    "Hyderabad",
    "Bangalore",
    "Chennai",
    "Mumbai",
    "Delhi",
    "Pune",
    "Kolkata",
    "Kochi",
    "Ahmedabad",
    "Jaipur"
]

age_groups = [
    "18-25",
    "26-35",
    "36-45",
    "46-55"
]

occupations = [
    "Student",
    "Software Engineer",
    "Data Analyst",
    "Teacher",
    "Freelancer",
    "Business Owner",
    "Marketing Professional",
    "Finance Professional"
]

with open("Users.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "UserID",
        "UserName",
        "AgeGroup",
        "Occupation",
        "City"
    ])

    for i in range(1, 201):

        user_id = f"U{i:03d}"

        user_name = random.choice(names)

        age_group = random.choice(age_groups)

        occupation = random.choice(occupations)

        city = random.choice(cities)

        writer.writerow([
            user_id,
            user_name,
            age_group,
            occupation,
            city
        ])

print("Users.csv created successfully!")