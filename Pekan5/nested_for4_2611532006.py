# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2006 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2006 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2006 = tinggi_2006
    c_2006 = a_2006
    lebar_2006 = (2 * tinggi_2006) - 2

    for i_2006 in range(1, tinggi_2006 + 1):
        b_2006 = c_2006 + 1

        for j_2006 in range(1, lebar_2006 + 1):

            # Baris atas dan bawah
            if i_2006 == 1 or i_2006 == tinggi_2006:
                if j_2006 == 1 or j_2006 == lebar_2006:
                    print("#", end="")
                else:
                    print("=", end="")
                    # Baris isi
            else:
                if j_2006 == 1 or j_2006 == lebar_2006:
                    print("|", end="")
                else:
                    if j_2006 == c_2006:
                        print("<", end="")
                    elif j_2006 == b_2006:
                        print(">", end="")
                    elif j_2006 == (lebar_2006 - c_2006):
                        print("<", end="")
                    elif j_2006 == (lebar_2006 - c_2006 + 1):
                        print(">", end="")
                    elif j_2006 > b_2006 and j_2006 < (lebar_2006 - c_2006):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_2006 -= 2

        if a_2006 <= 0:
            c_2006 = (-a_2006) + 2
        else:
            c_2006 = a_2006