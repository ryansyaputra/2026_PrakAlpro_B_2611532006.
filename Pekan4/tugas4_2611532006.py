print("\n=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_2006 = input("Masukkan Nama Pengunjung        :")
umur_2006 = int(input("Input Umur Anda                 :"))
sim_2006 = input("Apakah Anda Sudah Punya Sim(y/t):")[0].strip().lower()
jumlah_tiket_2006 = int(input("Masukkan Jumlah Tiket:"))

if jumlah_tiket_2006 <= 0:
    print("Peringatan:Kuota Tiket Tidak Valid")

print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")

nomor_paket_2006 = int(input("Masukkan Nomor Paket:"))
match nomor_paket_2006:
    case 1:
        nama_wahana_2006 = "Safari Rimba"
        harga_satuan_2006 = 50000
    case 2:
        nama_wahana_2006 = "Arung Jeram"
        harga_satuan_2006 = 75000
    case 3:
        nama_wahana_2006 = "Motor ATV Ekstrim"
        harga_satuan_2006 = 120000
    case 4:
        nama_wahana_2006 = "Roller Coaster kilat"
        harga_satuan_2006 = 100000
    case 5:
        nama_wahana_2006 = "All-Access VIP"
        harga_satuan_2006 = 220000
    case _: 
        print("Paket Wahana Tidak Valid")
        exit()


member_2006 = input("Apakah Anda member? (y/t):")[0].strip().lower()
kode_promo_2006 = input("Apakah Kode Promo Valid? (y/t):")[0].strip().lower()

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

# Khusus paket 3

if nomor_paket_2006 == 3 and umur_2006 >= 17 and sim_2006 == 'y':
    print("Status Akses : Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif nomor_paket_2006 == 3 and umur_2006 >= 17 and sim_2006 != 'y':
    print("Status Akses : Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif nomor_paket_2006 == 3 and umur_2006 < 17 and sim_2006 == 'y':
    print("Status Akses : Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif nomor_paket_2006 ==3:
    print("Status Akses : Anda Belum Cukup Umur dan Tidak Boleh Menaiki ATV")
# Paket selain 3
elif umur_2006 >= 10:
    print("Status Akses : Anda Memenuhi Syarat Bermain Wahana Ini")
else:
    print("Status Akses : Umur Anda Belum Memenuhi Syarat Minimal Wahana Ini")

print("\n--- Rincian Pembayaran ---")
subtotal_belanja_2006 = harga_satuan_2006 * jumlah_tiket_2006
total_diskon_persen_2006 = 0
if subtotal_belanja_2006 >=200000:
    total_diskon_persen_2006 += 10
if member_2006 in ["y","ya"]:
    total_diskon_persen_2006 += 5
if kode_promo_2006 in ["y","ya"]:
    total_diskon_persen_2006 += 15
if jumlah_tiket_2006 >= 5:
    total_diskon_persen_2006 += 5

nominal_diskon_2006 = subtotal_belanja_2006 * (total_diskon_persen_2006/100)
total_bayar_2006 = subtotal_belanja_2006 - nominal_diskon_2006

if total_bayar_2006 > 300000:
    catatan_layanan_2006 = "Selamat! Anda berhak mendapatkan Souvenir Gratis"
else:
    catatan_layanan_2006 = "Terimakasih Telah Berkunjung"
print(f"Subtotal Belanja : Rp {subtotal_belanja_2006:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_2006}% (Rp {nominal_diskon_2006:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_2006:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_2006}")
print("Program Selesai")
