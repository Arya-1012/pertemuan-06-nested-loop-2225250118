# Program Menampilkan Pasangan Indeks

n = int(input("Masukkan jumlah indeks: "))

for i in range(n):
    for j in range(n):
        print(f"({i}, {j})")