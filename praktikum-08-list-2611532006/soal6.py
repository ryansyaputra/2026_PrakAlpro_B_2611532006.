LAST_DIGIT = 6  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for day in range(1, 8):
    value = int(input("Day " + str(day) + ": "))
    expenses.append(value)

total = 0
highest_value = expenses[0]
highest_day = 1
days_above = 0

for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest_value:
        highest_value = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
        days_above += 1

average = total / len(expenses)

print("Daily limit:", daily_limit)
print("Total:", total)
print("Average:", f"{average:.1f}")
print("Highest: day", highest_day, "(" + str(highest_value) + ")")
print("Days above limit:", days_above)  