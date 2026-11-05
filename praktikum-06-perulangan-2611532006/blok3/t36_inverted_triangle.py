tinggi = int(input("Masukkan tinggi: "))

for row in range(tinggi, 0, -1):
    for column in range(1, row + 1):
        print("*", end=" ")
    print()