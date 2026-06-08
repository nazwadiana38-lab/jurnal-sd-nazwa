def render_dashboard(data_list, is_loading=False):
    print("--- DASHBOARD APLIKASI ---")

    # 1. Fitur Loading State
    if is_loading:
        print("Mohon Tunggu...") [cite: 124]
        return

    # 2. Validasi Data
    if not data_list: [cite: 92]
        print("[!] Data Kosong. Silakan sinkronisasi dengan Backend.") [cite: 94]
    else:
        for item in data_list: [cite: 95]
            print(f"- Item ID: {item['id']} | Nama: {item['name']}") [cite: 96]
