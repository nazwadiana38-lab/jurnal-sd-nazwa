import os

# Mengambil DB_PASSWORD dari file .env (jika dijalankan lokal) atau env system
DB_PASSWORD = os.getenv("DB_PASSWORD")

def connect_database():
    if not DB_PASSWORD:
        return "Koneksi gagal: DB_PASSWORD tidak ditemukan!"
    return f"Koneksi sukses menggunakan password: {DB_PASSWORD}"
