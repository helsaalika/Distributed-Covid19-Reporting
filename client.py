import rpyc

conn = rpyc.connect("localhost", 12345) # Replace server_ip_address with the actual IP address of your server

# Input data dari cmd
print("\n======================================================================")
print(" Silakan Input Data Pelapor dan Pasien")
print("======================================================================\n")
nik = input(" Masukkan NIK pelapor: ")
nama_pelapor = input(" Masukkan Nama Pelapor: ")
nama_terduga = input(" Masukkan Nama Terduga Covid: ")
alamat_terduga = input(" Masukkan Alamat Terduga Covid: ")
gejala = input(" Masukkan Gejala: ")

# Submit laporan Covid
response = conn.root.exposed_submit_report(nik, nama_pelapor, nama_terduga, alamat_terduga, gejala)
print("\n======================================================================")
print(" Server Response")
print("======================================================================\n")
print(response)
print("======================================================================\n")