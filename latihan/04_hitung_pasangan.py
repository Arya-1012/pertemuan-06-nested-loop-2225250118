# Program Menghitung Pasangan Indeks

n = int(input("Masukkan jumlah elemen: "))
jumlah_pasangan = 0

for i in range(n):
    for j in range(n):
        jumlah_pasangan += 1

print("Jumlah pasangan indeks:", jumlah_pasangan)