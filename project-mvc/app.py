from controllers.api_handler import get_users
from views.dashboard_component import fetch_data_from_api, render_dashboard

# Inisialisasi State Awal
app_state = {"items": [], "is_loading": True} 

def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False

if __name__ == "__main__":
    print("[PROSES INTEGRASI LOKAL]\n")

    # ==========================================================
    # KONDISI 1: Tampilan saat Data Masih Memuat (Loading)
    # ==========================================================
    print("[KONDISI 1: LOADING]")
    render_dashboard(app_state["items"], is_loading=app_state["is_loading"])
    
    print("\n" + "="*40 + "\n")

    # ==========================================================
    # PROSES INTEGRASI: Memanggil Data dari API & Update State
    # ==========================================================
    print("[System] Memulai integrasi data...")
    data = fetch_data_from_api(get_users)
    
    if data:
        # Perbarui data state dengan data riil dari backend api_handler
        update_state(data)
    else:
        # Jika API gagal/error, gunakan mock_data sebagai fallback
        print("[System] API gagal dimuat, menggunakan mock data...")
        mock_data = [{"id": 101, "name": "Produk A"}, {"id": 102, "name": "Produk B"}] 
        update_state(mock_data)

    print("\n" + "="*40 + "\n")

    # ==========================================================
    # KONDISI 2: Tampilan saat Data Sudah Berhasil Tampil
    # ==========================================================
    print("[KONDISI 2: DATA SUDAH TAMPIL]")
    render_dashboard(app_state["items"], is_loading=app_state["is_loading"])
