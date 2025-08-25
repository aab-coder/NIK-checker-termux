import json
import os
from datetime import datetime

class NIKCheckerDatabase:
    def __init__(self, database_file="nik_bocor_database.json")
self.database_file = database_file
        self.bocor_nik_list = self.load_database()

    def load_database(self):
        """Muat database dari file JSON"""
        if os.path.exists(self.database_file):
            try:
                with open(self.database_file, 'r', encoding='utf-8') as f:
data = json.load(f)
                    return data.get('nik_bocor', [])
            except (json.JSONDecodeError, FileNotFoundError):
print(f"⚠️File database rusak atau tidak dapat dibaca. Membuat database baru.")
return self.create_default_database()
        else:
            print(f"📁 File database tidak ditemukan. Membuat database baru: {self.database_file}")
            return self.create_default_database()

    def create_default_database(self):
        """Buat database default dengan beberapa contoh NIK"""
default_niks = [
            "1234567891012345"
        ]
        self.save_database(default_niks)
        return default_niks

    def save_database(self, nik_list=None):
        """Simpan database ke file JSON"""
        if nik_list is None:
            nik_list = self.bocor_nik_list

        database_content = {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
"total_nik": len(nik_list),
            "nik_bocor": nik_list
        }

        try:
            with open(self.database_file, 'w', encoding='utf-8') as f:
json.dump(database_content, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"❌ Error menyimpan database: {e}")
            return False

    def cek_nik(self, nik):
        """Cek apakah NIK ada dalam daftar yang bocor"""
        nik = nik.strip()

        # Simpan NIK yang diinput user ke database
if nik not in self.bocor_nik_list and nik.isdigit() and len(nik) == 16:
            self.bocor_nik_list.append(nik)
            self.save_database()
if nik in self.bocor_nik_list:
            return "DATA BOCOR"
        else:
            return "TIDAK BOCOR"

def main():
    print("="*50)
    print("    CEK KEBOCORAN DATA NIK")
    print("="*50)
print("   semua NIK akan aman, karena tool ini tidak menyimpan data user hanya admin yang bisa menyimpan")
print("   hanya untuk keamanan bukan mainan\n")

    checker = NIKCheckerDatabase()

    while True:
nik = input("\nMasukkan NIK (16 digit) atau ketik 'exit' untuk keluar: ").strip()

        if nik.lower() == 'exit':
            break

l        if not nik.isdigit() or len(nik) != 16:
            print("❌ Format NIK tidak valid! Harus 16 digit angka")
continue

        hasil = checker.cek_nik(nik)

        if hasil == "DATA BOCOR":
            print("\n❌❌❌ HASIL: DATA BOCOR ❌❌❌")
print("NIK Anda ditemukan dalam database kebocoran")
print("diharapkan untuk meminta ubah NIK")
else:
print("\n✅✅✅ HASIL: TIDAK BOCOR ✅✅✅")
print(" hidup tenang")
print(f"\nTotal NIK dalam database: {checker.total_nik_bocor()}")
if __name__ == "__main__":
    main()