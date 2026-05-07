#Database Schema (Draft Awal)
Aplikasi ini membutuhkan beberapa tabel utama untuk menyimpan data, antara lain:
1. **Tabel Users**
-id (pk,int)
-usn (var)
-email (var)
-pw_hash (var)
-role (var)
2. **Tabel Profiles**
-id (pk,int)
-user_id (fk,int)
-full_name (var)
-avatar_url (var)
-bio (text)
