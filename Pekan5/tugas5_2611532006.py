print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")

n_2006 = int(input("Masukkan ukuran skala jam pasir(N): "))

# Border Atas
print("#", end="")

for i_2006 in range(4 * n_2006 + 5):
    print("=", end="")

print("#")


# Fase 1 Jam Pasir Atas
for baris_2006 in range(n_2006,0,-1):

    print("| ", end="")

    for spasi_2006 in range(2 * (n_2006 - baris_2006)):
        print(" ", end="")

    for angka_2006 in range(baris_2006,0,-1):
        print(angka_2006, end=" ")

    print("<*>", end="")

    for angka_2006 in range(1,baris_2006 + 1):
        print(" ", end="")
        print(angka_2006, end="")   

    for spasi_2006 in range(2 * (n_2006 - baris_2006)):
        print(" ", end="")

    print(" |")



# Fase 2 Poros Tengah

print("|", end="")

for spasi_2006 in range(2 * n_2006 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_2006 in range(2 * n_2006 + 1):
    print(" ", end="")

print("|")

# Fase 3 Jam Pasir Bawah
for baris_2006 in range(1,n_2006 + 1):

    print("| ", end="")

    for spasi_2006 in range(2 * (n_2006 - baris_2006)):
        print(" ", end="")

    for angka_2006 in range(baris_2006,0,-1):
        print(angka_2006, end=" ")

    print("<*>", end="")

    for angka_2006 in range(1,baris_2006 + 1):
        print(" ", end="")
        print(angka_2006, end="")

    for spasi_2006 in range(2 * (n_2006 - baris_2006)):
        print(" ", end="")

    print(" |")

print("#", end="")

for i_2006 in range(4 * n_2006 + 5):
    print("=", end="")

print("#")