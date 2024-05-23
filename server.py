import rpyc
import threading
import time
import random
from queue import Queue

# Struktur data untuk penjemput
penjemput = [
    {"nama": "Budi", "status": "available"},
    {"nama": "Bagus", "status": "available"},
    {"nama": "Andi", "status": "available"},
    {"nama": "Lina", "status": "available"},
    {"nama": "Toni", "status": "available"},
    {"nama": "Rara", "status": "available"},
]

# Buat lock untuk melindungi akses ke variabel penjemput
penjemput_lock = threading.Lock()

# Fungsi untuk mengganti status penjemput dan kembali ke "available" setelah waktu tertentu
def update_status(penjemput1, penjemput2, queue):
    time_to_pickup = random.randint(15, 60)  # Waktu random antara 15-60 detik
    queue.put(time_to_pickup)  # Simpan waktu penjemputan di queue
    time.sleep(time_to_pickup)
    with penjemput_lock:
        penjemput1["status"] = "available"
        penjemput2["status"] = "available"

# Fungsi untuk mencetak status semua penjemput
def print_status():
    while True:
        with penjemput_lock:
            print("Status Penjemput:")
            for p in penjemput:
                print(f"{p['nama']}: {p['status']}")
        print("--------------------------")
        time.sleep(10)  # Cetak status setiap 10 detik

class CovidReportService(rpyc.Service):
    def exposed_submit_report(self, nik, nama_pelapor, nama_terduga, alamat_terduga, gejala):
        # Validasi NIK
        with open("database.txt", "r") as file:
            valid_nik = False
            for line in file:
                if line.strip() == nik:  # Pencocokan string yang lengkap
                    valid_nik = True
                    break

            if not valid_nik:
                return " NIK tidak valid\n"

            with penjemput_lock:
                # Cari dua penjemput yang available
                available_penjemput = [p for p in penjemput if p["status"] == "available"]
                if len(available_penjemput) < 2:
                    return " Tidak ada penjemput yang tersedia saat ini.\n"

                # Ambil dua penjemput
                penjemput1, penjemput2 = available_penjemput[:2]
                penjemput1["status"] = "picking up"
                penjemput2["status"] = "picking up"

            # Queue untuk menerima waktu penjemputan dari thread
            queue = Queue()
            
            # Mulai thread untuk mengupdate status kembali ke available
            threading.Thread(target=update_status, args=(penjemput1, penjemput2, queue)).start()

            # Tunggu sampai thread memasukkan waktu penjemputan ke queue
            time_to_pickup = queue.get()

            # Respon dengan informasi penjemput
            return f"Estimasi Penjemputan: {time_to_pickup} detik\n Nama Penjemput: {penjemput1['nama']} dan {penjemput2['nama']}\n Jumlah Penjemput: 2 Orang\n"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    # Mulai thread untuk mencetak status penjemput
    threading.Thread(target=print_status, daemon=True).start()

    # Jalankan server
    server = ThreadedServer(CovidReportService, port=12345)
    server.start()
