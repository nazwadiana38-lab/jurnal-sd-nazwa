from views.dashboard_component import render_dashboard

app_state = {"items": [], "is_loading": True} 

def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False

if __name__ == "__main__":
    # KONDISI 1: Tampilan saat Data Sedang Loading
    print("[KONDISI 1: LOADING]")
    render_dashboard(app_state["items"], is_loading=app_state["is_loading"])
    print("\n" + "="*30 + "\n")

    # Simulasi Proses Data Masuk
    mock_data = [{"id": 101, "name": "Produk A"}, {"id": 102, "name": "Produk B"}] 
    update_state(mock_data)

    # KONDISI 2: Tampilan saat Data Sudah Tampil
    print("[KONDISI 2: DATA SUDAH TAMPIL]")
    render_dashboard(app_state["items"], is_loading=app_state["is_loading"])
