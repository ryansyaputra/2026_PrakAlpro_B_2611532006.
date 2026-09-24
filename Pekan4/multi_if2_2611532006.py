# Buat file dengan nama multi_if2_2611532006.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_2006
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_2006 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2006 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member = input_member_2006 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2006 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2006 = input_promo_2006 in ["y", "ya"]

total_diskon_persen_2006 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2006 >= 1000000:
    total_diskon_persen_2006 += 10 # Diskon belanja besar

if is_member:
    total_diskon_persen_2006 += 5 # Diskon member

if kode_promo_valid_2006:
    total_diskon_persen_2006 += 15 # Diskon voucher

# Menghitung nomimal diskon dan total bayar
nominal_diskon_2006 = total_belanja_2006 * (total_diskon_persen_2006 / 100)
total_bayar_2006 = total_belanja_2006 - nominal_diskon_2006

#Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_2006}% (Rp {nominal_diskon_2006:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_2006:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_2006}%")
# Putput total diskon yang anda dapatkan: 30% jika belanja > 1juta, member, dan kode promo valid