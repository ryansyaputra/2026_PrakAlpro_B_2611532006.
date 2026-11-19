menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []


for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        value = int(input("Day " + str(day) + ", " + menu + ": "))
        row.append(value)
    sales.append(row)


print("Total per day:")
for i in range(len(sales)):
    day_total = 0
    for value in sales[i]:
        day_total += value
    print("Day " + str(i + 1) + ": " + str(day_total))


menu_totals = []
for col in range(len(menus)):
    menu_total = 0
    for row in range(len(sales)):
        menu_total += sales[row][col]
    menu_totals.append((menus[col], menu_total))

print("Total per menu:", menu_totals)

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]
for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print("Best seller: " + best_name + " (" + str(best_total) + ")")