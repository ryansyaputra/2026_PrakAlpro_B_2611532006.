n = int(input("Jumlah perulangan: "))
cash = {}

for i in range(n):
    data = input().split()
    nama = data[0]
    nominal = int(data[1])
    if nama in cash:
        cash[nama] += nominal
    else:
        cash[nama] = nominal

total_cash = 0
top_nama = ""
top_cash = 0

for nama, kas in cash.items():
    print(f"{nama}: {kas}")
    total_cash += kas
    if kas > top_cash:
        top_cash = kas
        top_nama = nama

print(f"Total Cash: {total_cash}")
print(f"Top Contributor: {top_nama} ({top_cash})")

