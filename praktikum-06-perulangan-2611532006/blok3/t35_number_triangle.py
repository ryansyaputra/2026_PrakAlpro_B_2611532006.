tinggi = int(input("Masukkan tinggi: "))

for row in range(1, tinggi + 1):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()