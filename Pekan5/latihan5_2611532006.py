tinggi_2006 = int(input("Masukkan tingi segitiga:"))

for i_2006 in range(1, tinggi_2006 + 1):
    print(" " * (tinggi_2006 - i_2006), end=" ")

    for j_2006 in range(i_2006):
        print("*", end=" ")
    print()  