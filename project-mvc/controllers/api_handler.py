import random

# Simulasikan data dari database
users = [{"id": 1, "name": "Admin"}, {"id": 2, "name": "User"}]

def get_users():
    # Simulasi acak: Jika angka yang keluar adalah 1, simulasikan server error
    if random.choice([0, 1]) == 1:
        return {"status": "error", "message": "Server sedang sibuk. Silakan coba beberapa saat lagi."}

    return {"status": "success", "data": users}
