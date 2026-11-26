students = input("Input students:").split()
submitted = set(input("Input yang submit:").split())

not_submitted = set(students) - (submitted) 

print("submitted:", len(submitted), "students")
print("not submitted:", len(not_submitted), "students")

for i in students:
    if i in not_submitted:
        print(i)


