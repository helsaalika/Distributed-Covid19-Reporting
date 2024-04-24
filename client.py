import rpyc

conn = rpyc.connect("192.168.13.90", 12345) # ip address

# Input data dari cmd
nik = input("Masukkan NIK pelapor: ")
nama_pelapor = input("Masukkan Nama Pelapor: ")
nama_terduga = input("Masukkan Nama Terduga Covid: ")
alamat_terduga = input("Masukkan Alamat Terduga Covid: ")
gejala = input("Masukkan Gejala: ")

# Submit laporan Covid
response = conn.root.exposed_submit_report(nik, nama_pelapor, nama_terduga, alamat_terduga, gejala)
print("Response dari server:", response)
