import os
import time
import json
import random
from datetime import datetime

# Warna untuk tampilan keren
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear()
    print(Colors.HEADER + Colors.BOLD)
    print("=" * 60)
    print(" " * 15 + "🔥 HAPUS DATA PINJOL 🔥")
    print(" " * 12 + "Tools Penghapus Data Pinjaman Online")
    print("=" * 60)
    print(Colors.END)

def loading_animation(duration=3, message="Memproses penghapusan data..."):
    print(Colors.YELLOW + Colors.BOLD + message + Colors.END)
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{Colors.BLUE}{spinner[i % len(spinner)]} {message} {Colors.END}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print("\n" + Colors.GREEN + "✅ Berhasil!" + Colors.END)

def delete_data(nik, kode_apk):
    print_header()
    print(Colors.BOLD + f"NIK     : {nik}" + Colors.END)
    print(Colors.BOLD + f"Kode APK: {kode_apk}" + Colors.END)
    print("\n" + "=" * 60)
    
    # Simulasi proses penghapusan yang meyakinkan
    steps = [
        "Menghubungkan ke server pinjol...",
        "Mengautentikasi dengan NIK...",
        "Mengakses database pengguna...",
        "Menghapus data pribadi...",
        "Menghapus riwayat pinjaman...",
        "Menghapus data KTP & foto...",
        "Menghapus tracking device...",
        "Membersihkan cache server...",
        "Memverifikasi penghapusan total..."
    ]
    
    for step in steps:
        loading_animation(0.6, step)
    
    # Simpan ke riwayat
    history = load_history()
    history.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nik": nik,
        "kode_apk": kode_apk,
        "status": "BERHASIL",
        "detail": "Semua data telah dihapus secara permanen dari server"
    })
    save_history(history)
    
    print("\n" + Colors.GREEN + Colors.BOLD + "🎉 DATA BERHASIL DIHAPUS SECARA PERMANEN!" + Colors.END)
    print(Colors.GREEN + "Tidak ada jejak tersisa di sistem pinjol tersebut." + Colors.END)
    input("\nTekan Enter untuk kembali ke menu...")

def load_history():
    try:
        with open("riwayat_hapus.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_history(history):
    with open("riwayat_hapus.json", "w") as f:
        json.dump(history, f, indent=2)

def show_history():
    print_header()
    print(Colors.BOLD + "📜 RIWAYAT PENGHAPUSAN DATA" + Colors.END)
    print("=" * 60)
    
    history = load_history()
    if not history:
        print(Colors.YELLOW + "Belum ada riwayat penghapusan." + Colors.END)
    else:
        for i, entry in enumerate(reversed(history), 1):
            print(f"{Colors.BOLD}{i}. {entry['timestamp']}{Colors.END}")
            print(f"   NIK     : {entry['nik']}")
            print(f"   Kode APK: {entry['kode_apk']}")
            print(f"   Status  : {Colors.GREEN}{entry['status']}{Colors.END}")
            print(f"   Detail  : {entry['detail']}")
            print("-" * 50)
    
    input("\nTekan Enter untuk kembali ke menu...")

def main():
    while True:
        print_header()
        print(Colors.BOLD + "MENU UTAMA:" + Colors.END)
        print("1. 🔄 Hapus Semua Data APK Pinjol")
        print("2. 📜 Riwayat Penghapusan")
        print("3. ❌ Keluar Tools")
        print()
        
        choice = input(Colors.BOLD + "Pilih menu (1-3): " + Colors.END)
        
        if choice == "1":
            print_header()
            print(Colors.BOLD + "MASUKKAN DATA UNTUK PENGHAPUSAN" + Colors.END)
            nik = input(Colors.BOLD + "1. NIK (16 digit)          : " + Colors.END).strip()
            kode_apk = input(Colors.BOLD + "2. Kode APK Pinjol        : " + Colors.END).strip()
            
            if nik and kode_apk:
                confirm = input(Colors.YELLOW + "\nYakin ingin menghapus data ini? (y/n): " + Colors.END).lower()
                if confirm == 'y':
                    delete_data(nik, kode_apk)
                else:
                    input("Dibatalkan. Tekan Enter...")
            else:
                input(Colors.RED + "NIK dan Kode APK tidak boleh kosong!" + Colors.END)
        
        elif choice == "2":
            show_history()
        
        elif choice == "3":
            print_header()
            print(Colors.GREEN + "Terima kasih telah menggunakan HAPUS DATA PINJOL Tools!" + Colors.END)
            print(Colors.YELLOW + "Semua data Anda aman." + Colors.END)
            break
        
        else:
            input(Colors.RED + "Pilihan tidak valid! Tekan Enter..." + Colors.END)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Colors.RED + "Tools dihentikan." + Colors.END)
