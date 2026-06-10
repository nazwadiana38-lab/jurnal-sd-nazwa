import os

# Membaca variabel 'APP_USER', defaultnya adalah 'Guest'
user_name = os.getenv('APP_USER', 'Guest')

if __name__ == "__main__":
    print(f"Halo {user_name}! Aplikasi ini berjalan di dalam kontainer Docker.")
