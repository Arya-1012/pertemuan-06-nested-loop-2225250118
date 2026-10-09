# Pertemuan 06 - Nested Loop Python

## Identitas Mahasiswa

- Nama: Arya Kusmana Anas
- NIM: 2225250118
- Kelas: 3B
- Program Studi: Pendidikan Matematika
- Mata Kuliah: Algoritma dan Pemrograman
- Pertemuan: 06

---

## Deskripsi

Proyek ini merupakan tugas Pertemuan 6 mata kuliah Algoritma dan
Pemrograman yang membahas penggunaan nested loop dalam Python.

Materi yang dipelajari meliputi:
1. Nested loop dan pasangan indeks.
2. Pembentukan pola menggunakan perulangan.
3. Akumulasi jumlah per baris dan keseluruhan.
4. Pencacahan pasangan berdasarkan kondisi.
5. Pembuatan tabel perkalian dan statistik.
6. Pengujian program menggunakan Visual Studio Code.
7. Pengumpulan tugas melalui GitHub.

## Tujuan

- Memahami cara kerja nested loop.
- Membentuk pola menggunakan perulangan bersarang.
- Menghitung jumlah nilai menggunakan akumulator.
- Menghitung banyaknya kejadian menggunakan counter.
- Memahami penggunaan kondisi pada nested loop.
- Menguji dan memperbaiki kesalahan program Python.

## Cara Menjalankan Program

Pastikan Python 3 sudah terpasang di komputer dan folder proyek
sudah dibuka melalui Visual Studio Code.

Buka terminal di VS Code menggunakan menu Terminal > New Terminal.

1. Menjalankan Latihan 1
python latihan/01_pasangan_indeks.py

Program menampilkan seluruh pasangan indeks dan menghitung
banyaknya pasangan yang dihasilkan.

2. Menjalankan Latihan 2
python latihan/02_pola_segitiga.py

Program menerima input tinggi segitiga dan menampilkan pola
bintang menggunakan nested loop.

3. Menjalankan Latihan 3
python latihan/03_jumlah_per_baris.py

Program menghitung jumlah hasil perkalian pada setiap baris.

4. Menjalankan Latihan 4
python latihan/04_hitung_pasangan.py

Program menghitung banyaknya pasangan indeks yang memenuhi
kondisi tertentu.
 
5. Menjalankan Tugas
python tugas/tabel_perkalian_dan_statistik.py

Program membuat tabel perkalian, menghitung jumlah setiap baris,
menghitung total seluruh hasil perkalian, dan menghitung banyaknya hasil perkalian yang bernilai genap.

## Hasil Pengujian

Pengujian dilakukan menggunakan beberapa nilai input untuk
memastikan program menghasilkan keluaran yang benar.

Input n	Jumlah Pasangan	Total Keseluruhan	Banyak Hasil Genap
1	1	1	0
2	4	9	3
3	9	36	5
Test Case Tambahan
Input	Tujuan Pengujian
n = 0	Memastikan validasi input berjalan
n = -1	Memastikan input negatif ditolak
n = 1	Menguji ukuran tabel terkecil yang valid
n = 3	Menguji tabel dengan beberapa baris dan kolom

## Refleksi

Melalui tugas ini, saya mempelajari penggunaan nested loop untuk
mengolah data dalam bentuk baris dan kolom.

Saya memahami bahwa loop luar mengatur baris, sedangkan loop
dalam memproses kolom pada setiap baris.

Saya juga mempelajari perbedaan akumulasi dan pencacahan.
Akumulasi digunakan untuk menghitung jumlah nilai, sedangkan
pencacahan digunakan untuk menghitung banyaknya kejadian yang
memenuhi kondisi tertentu.

Salah satu hal penting dalam nested loop adalah menentukan
letak inisialisasi variabel. Variabel total_baris harus direset
pada setiap baris, sedangkan total_semua harus tetap terakumulasi
sampai seluruh perulangan selesai.

Pengujian program membantu memastikan bahwa hasil perhitungan
sesuai dengan hasil yang diharapkan.

