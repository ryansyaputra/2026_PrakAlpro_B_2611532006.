max_percobaan = 3
percobaan = 1
pin_benar = "1234"
pin = input("Masukkan PIN: ")

while pin != pin_benar and percobaan < max_percobaan:
    percobaan += 1
    print("coba lagi")
    pin = input("Masukkan PIN: ")
if pin == pin_benar:
    print("nice")
else:
    print("kamu di blok")