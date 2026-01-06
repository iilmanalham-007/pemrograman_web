import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    print("--------- menu ---------")
    print("1. konversi nilai ke label")
    print("2. konversi label ke bobot")
    print("3. hitung total sks yang diambil")
    print("4. hitung total nilai")
    print("5. hitung IPS")
    print("6. exit")

def kembali_ke_menu():
    input("\nKlik Enter untuk kembali ke tampilan awal...")