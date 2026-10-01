# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2006 = int(input("Masukkan nilai batas: "))
for i_2006 in range(batas_2006+1):
    for j_2006 in range(batas_2006+1):
        print(i_2006+j_2006, end=" ")
    print()  # pindah ke baris berikutnya