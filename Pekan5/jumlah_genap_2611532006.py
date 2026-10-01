# Buat file dengan nama jumlah_genap_2611532006.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_2006
# Program ini menggunakan fungsi input()

ulang_2006 = int(input("Masukkan nilai batas: "))

jumlah_2006 = 0
for i_2006 in range(1, ulang_2006 + 1):
    if i_2006 % 2 == 0:
        print(i_2006, end=" ")
        jumlah_2006 = jumlah_2006 + i_2006

        if i_2006 < ulang_2006   :
            print("+ ", end="")
        else:
            print("= ", jumlah_2006, end="")
print()
print("Jumlah =", jumlah_2006)