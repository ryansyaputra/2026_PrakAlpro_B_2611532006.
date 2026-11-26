schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

busiest_day = ""
max_courses = 0

for day, courses in schedule.items():
    if len(courses) > max_courses:
        busiest_day = day
        max_courses = len(courses)

print(f"Busiest day: {busiest_day} ({max_courses} courses)")

course = input()
days_count = 0

for day, courses in schedule.items():
    if course in courses:
        days_count += 1

print(f"{course}: {days_count} days")