# Sistem Pelaporan SIAGA Covid-19 

Program ini adalah aplikasi sistem terdistribusi yang dirancang untuk memfasilitasi pelaporan kasus Covid-19. Sistem ini bertujuan untuk mempermudah proses pelaporan, mengelola laporan secara otomatis, dan memungkinkan tim penjemputan untuk merespon dengan cepat dan tepat.

## Fitur

- Antarmuka berbasis console untuk pengguna melaporkan kasus Covid-19 dengan memasukkan Nomor Induk Kependudukan (NIK), nama pelapor, nama terduga Covid, alamat terduga Covid, dan gejala yang dirasakan.
- Memvalidasi laporan dengan membandingkan NIK pelapor dengan database (file teks). Jika valid, server akan memberikan estimasi waktu, nama petugas, dan jumlah anggota tim (ditetapkan 2 orang per permintaan) yang akan merespon.
- Memantau ketersediaan dan status (tersedia atau sedang menjemput) anggota tim. Menggunakan mutex untuk mengelola akses bersamaan ke sumber daya bersama dan mencegah race condition.
- Menggunakan RPC (Remote Procedure Call) untuk komunikasi antara klien dan server, serta thread untuk menangani beberapa permintaan secara bersamaan.

## Arsitektur Sistem

Sistem ini menggunakan arsitektur client-server, di mana server bertanggung jawab atas pengelolaan semua permintaan dari klien. Tim penjemput terdiri dari 6 anggota yang memiliki status ketersediaan (tersedia) dan status penjemputan (sedang menjemput). Ketika ada permintaan masuk dari klien, server akan menentukan waktu estimasi, anggota tim yang tersedia, dan jumlah orang yang akan melakukan penjemputan (ditetapkan menjadi 2 orang per permintaan).

## Cara Menjalankan 

1. Untuk Menjalankan server, masukkan perintah berikut:
   ```
   py server.py
   ```
   
2. Untuk menjalankan client, masukkan perintah berikut:
   ```
   py client.py
   ```

## Dokumentasi

- **Link Video Demo**: [Video TUBES SISTER Kelompok 4](https://drive.google.com/file/d/1nXh5z0QsBOexMOLnwMMDoKE84IWZMRrq/view?usp=sharing)

Program ini dibuat sebagai tugas besar Mata Kuliah Sistem Terdistribusi. 

### Kelompok 4 

Anggota : 
- Aini Nurul Azizah - 211524034
- Amelia Nathasa - 211524036
- Falia Davina Gustaman - 211524041
- Helsa Alika Femiani - 211524044

3B - D4 Teknik Informatika, 
Politeknik Negeri Bandung
  
