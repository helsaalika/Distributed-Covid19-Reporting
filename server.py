import rpyc

class CovidReportService(rpyc.Service):
    def exposed_submit_report(self, nik, nama_pelapor, nama_terduga, alamat_terduga, gejala):
        # Check validity of NIK (Assuming database stored in a text file)
        with open("database.txt", "r") as file:
            for line in file:
                if nik in line:
                    # If NIK found in database, respond with pickup information
                    return "Waktu: 29 Maret 2024, Nama: Tim Penanganan Covid, Jumlah Orang: 2"
        return "NIK tidak valid"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(CovidReportService, port=12345)
    server.start()
