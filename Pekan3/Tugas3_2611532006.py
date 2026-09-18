# Program Sistem Simulasi Transaksi dan Validasi Akses Toko

print("=== SISTEM TRANSAKSI TOKO ===")
nama_2006 = input("Masukkan nama pelanggan:")
status_pelanggan_2006 = input("Masukkan status pelanggan (member/non-member):").strip().lower()
total_belanja_2006 = int(input("Masukkan total belanja:"))
jumlah_barang_2006 = int(input("Masukkan jumlah barang:"))
kode_promo_2006 = input("Masukkan kode promo:")

print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan :", nama_2006)
print("Total Belanja  : Rp", total_belanja_2006)
print("Jumlah Barang  :", jumlah_barang_2006)
print("Kode Promo     :", kode_promo_2006)

print("\n=== HASIL VALIDASI TRANSAKSI ===")
syarat_belanja_2006 = total_belanja_2006 >= 100000
syarat_barang_2006 = jumlah_barang_2006 >= 5
syarat_status_member_2006 = status_pelanggan_2006 == "member"
tersedia_promo_2006 = kode_promo_2006 != ""
syarat_diskon_2006 = syarat_status_member_2006 and syarat_belanja_2006
daftar_promo_2006 = ["SALE20", "PROMO20", "HEMAT20"]
syarat_promo_2006 = kode_promo_2006 in daftar_promo_2006
 
print("Belanja >= Rp100000 :", syarat_belanja_2006) 
print("Jumlah Barang >= 5  :", syarat_barang_2006)
print("Status Member       :", syarat_status_member_2006)
print("Kode Promo Tersedia :", tersedia_promo_2006)
print("Mendapatkan Diskon  :", syarat_diskon_2006)
print("Mendapatkan Promo   :", syarat_promo_2006)

print("\n=== HASIL PERHITUNGAN ===")
diskon_2006 = 0
if syarat_diskon_2006:
    diskon_2006 = total_belanja_2006 * 20 // 100
    print("Diskon 20%            :Rp", diskon_2006)
total_bayar_2006 = total_belanja_2006 - diskon_2006
rata_rata_barang_2006 = total_bayar_2006 // jumlah_barang_2006
print("Total Bayar            :Rp", total_bayar_2006)
print("Rata-rata Harga Barang :Rp", rata_rata_barang_2006)

print("\n=== HAK AKSES PELANGGAN ===")
member_akses_2006 = syarat_status_member_2006
promo_akses_2006 = syarat_promo_2006 and syarat_belanja_2006
free_shipping_akses_2006 = syarat_status_member_2006 and syarat_barang_2006
member_bit_2006 = 0b0001
belanja_bit_2006 = 0b0010
barang_bit_2006 = 0b0100
promo_bit_2006 = 0b1000
kode_hak_akses_2006 = 0
if syarat_status_member_2006:
    kode_hak_akses_2006 = kode_hak_akses_2006 | member_bit_2006
if syarat_belanja_2006 :
    kode_hak_akses_2006 = kode_hak_akses_2006 | belanja_bit_2006
if syarat_barang_2006 :
    kode_hak_akses_2006 = kode_hak_akses_2006 | barang_bit_2006
if syarat_promo_2006:
    kode_hak_akses_2006 = kode_hak_akses_2006 | promo_bit_2006
print("Kode Hak Akses       :", format(kode_hak_akses_2006,"04b"))
print("Member Access        :", member_akses_2006)
print("Promo Access         :", promo_akses_2006)
print("Free Shipping Access :", free_shipping_akses_2006)

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("Kode Biner   :", format(kode_hak_akses_2006, "04b"))
print("Kode Desimal :", kode_hak_akses_2006)

print("=== Pemeriksaan Status ===")
print("Cek Member")
print(format(kode_hak_akses_2006,"04b"), '&', "0001")
status_member_2006 = kode_hak_akses_2006 & member_bit_2006
print("Hasil Biner   :", format(status_member_2006,"04b"))
print("Hasil Desimal :", status_member_2006)
print("\nCek Promo")
print(format(kode_hak_akses_2006,"04b"), '&', "1000")
status_promo_2006 = kode_hak_akses_2006 & promo_bit_2006
print("Hasil Biner   :", format(status_promo_2006,"04b"))
print("Hasil Desimal :", status_promo_2006)
print("\nCek Belanja")
print(format(kode_hak_akses_2006,"04b"), '&', "0010")
status_belanja_2006 = kode_hak_akses_2006 & belanja_bit_2006
print("Hasil Biner   :", format(status_belanja_2006,"04b"))
print("Hasil Desimal :", status_belanja_2006)
print("\nCek Barang")
print(format(kode_hak_akses_2006,"04b"), '&', "0100")
status_barang_2006 = kode_hak_akses_2006 & barang_bit_2006
print("Hasil Biner   :", format(status_barang_2006,"04b"))
print("Hasil Desimal :", status_barang_2006)

print("\n=== Perbandingan Status ===")
kode_referensi_2006 = 0b1001
print("Kode Transaksi:", format(kode_hak_akses_2006,"04b"))
print("Kode Referensi:", format(kode_referensi_2006,"04b"))
print(format(kode_hak_akses_2006,"04b"), '^', "1001")
perbandingan_status_2006 = kode_hak_akses_2006 ^ kode_referensi_2006
print("Hasil Biner  :", format(perbandingan_status_2006,"04b"))
print("Hasil Desimal:", perbandingan_status_2006)

print("=== Shift ===")
#geser kiri
print(format(kode_hak_akses_2006,"04b"),'<<',"1")
hasil_shift_2006 = kode_hak_akses_2006 << 1
print("Hasil Biner:", format(hasil_shift_2006,"04b"))
print("Hasil Desimal:", hasil_shift_2006)
#geser kanan
print(format(kode_hak_akses_2006,"04b"),'>>',"1")
hasil_shift_2006 = kode_hak_akses_2006 >> 1
print("Hasil Biner:", format(hasil_shift_2006,"04b"))
print("Hasil Desimal:", hasil_shift_2006)




