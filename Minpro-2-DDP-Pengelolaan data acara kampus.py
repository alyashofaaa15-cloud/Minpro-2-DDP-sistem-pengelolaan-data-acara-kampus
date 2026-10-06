import os
import pwinput
from prettytable import PrettyTable

USERS = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "nama": "Panitia BEM"
    },
    "mhs": {
        "password": "123",
        "role": "user",
        "nama": "Mahasiswa"
    }
}

KATEGORI_ACARA = {
    "1": "Seminar & Webinar",
    "2": "Kesenian & Budaya",
    "3": "Kompetisi & Olahraga",
    "4": "Organisasi & Pelatihan"
}

data_acara = [
    {
        "nama": "Seminar Nasional AI & Data",
        "kategori": "Seminar & Webinar",
        "tanggal": "15-11-2026",
        "lokasi": "Auditorium Utama",
        "kuota": 100,
        "pendaftar": ["mhs"]
    },
    {
        "nama": "Pentas Seni Dies Natalis",
        "kategori": "Kesenian & Budaya",
        "tanggal": "20-11-2026",
        "lokasi": "Lapangan Kampus",
        "kuota": 250,
        "pendaftar": []
    }
]

def hapus_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_teks_valid(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Input tidak boleh kosong!")
        else:
            return teks

def input_int_positif(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai <= 0:
                print("Angka harus lebih dari 0!")
            else:
                return nilai
        except ValueError:
            print("Input harus berupa angka bulat!")

def pilih_kategori_acara():
    print("\nPILIH KATEGORI ACARA")
    tabel_kat = PrettyTable()
    tabel_kat.field_names = ["Kode", "Kategori Acara"]
    for kode in KATEGORI_ACARA:
        tabel_kat.add_row([kode, KATEGORI_ACARA[kode]])
    print(tabel_kat)

    while True:
        pilihan = input("Pilih kode kategori (1-4): ").strip()
        if pilihan in KATEGORI_ACARA:
            return KATEGORI_ACARA[pilihan]
        print("Pilihan tidak valid, pilih 1-4!")

def tambah_acara():
    print("\nTAMBAH DATA ACARA KAMPUS")
    nama = input_teks_valid("Nama acara          : ")
    kategori = pilih_kategori_acara()
    tanggal = input_teks_valid("Tanggal pelaksanaan : ")
    lokasi = input_teks_valid("Lokasi kegiatan     : ")
    kuota = input_int_positif("Kuota peserta       : ")

    data_baru = {
        "nama": nama,
        "kategori": kategori,
        "tanggal": tanggal,
        "lokasi": lokasi,
        "kuota": kuota,
        "pendaftar": []
    }

    data_acara.append(data_baru)
    print("Data acara berhasil ditambahkan!")

def lihat_acara():
    print("\nDAFTAR ACARA KAMPUS")
    if len(data_acara) == 0:
        print("Belum ada data acara.")
        return False

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Acara", "Kategori", "Tanggal", "Lokasi", "Kuota", "Terdaftar"]

    nomor = 1
    for item in data_acara:
        terdaftar_str = f"{len(item['pendaftar'])}/{item['kuota']}"
        tabel.add_row([
            nomor,
            item["nama"],
            item["kategori"],
            item["tanggal"],
            item["lokasi"],
            item["kuota"],
            terdaftar_str
        ])
        nomor += 1

    print(tabel)
    print("Total Acara :", len(data_acara))
    return True

def ubah_acara():
    if not lihat_acara():
        return

    print("\nUBAH DATA ACARA")
    nomor = input_int_positif("Masukkan nomor acara yang ingin diubah: ")
    index = nomor - 1

    if 0 <= index < len(data_acara):
        item = data_acara[index]
        print("Mengubah data acara:", item["nama"])

        nama_baru = input("Nama acara baru (tekan Enter jika tidak diubah): ").strip()
        if nama_baru != "":
            item["nama"] = nama_baru

        pilih_kat = input("Ubah kategori acara? (y/n): ").strip().lower()
        if pilih_kat == "y":
            item["kategori"] = pilih_kategori_acara()

        tgl_baru = input("Tanggal baru (tekan Enter jika tidak diubah): ").strip()
        if tgl_baru != "":
            item["tanggal"] = tgl_baru

        lokasi_baru = input("Lokasi baru (tekan Enter jika tidak diubah): ").strip()
        if lokasi_baru != "":
            item["lokasi"] = lokasi_baru

        pilih_kuota = input("Ubah kuota peserta? (y/n): ").strip().lower()
        if pilih_kuota == "y":
            kuota_baru = input_int_positif("Masukkan kuota peserta baru: ")
            if kuota_baru < len(item["pendaftar"]):
                print(f"Kuota tidak boleh kurang dari jumlah pendaftar saat ini ({len(item['pendaftar'])} orang)!")
            else:
                item["kuota"] = kuota_baru

        print("Data acara berhasil diperbarui!")
    else:
        print("Nomor acara tidak ditemukan!")

def hapus_acara():
    if not lihat_acara():
        return

    print("\nHAPUS DATA ACARA")
    nomor = input_int_positif("Masukkan nomor acara yang ingin dihapus: ")
    index = nomor - 1

    if 0 <= index < len(data_acara):
        konfirmasi = input(f"Yakin ingin menghapus acara '{data_acara[index]['nama']}'? (y/n): ").strip().lower()
        if konfirmasi == "y":
            nama_terhapus = data_acara[index]["nama"]
            del data_acara[index]
            print(f"Data acara '{nama_terhapus}' berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Nomor acara tidak ditemukan!")

def daftar_acara_mhs(username):
    if not lihat_acara():
        return

    print("\nPENDAFTARAN ACARA KAMPUS")
    nomor = input_int_positif("Masukkan nomor acara yang ingin diikuti: ")
    index = nomor - 1

    if 0 <= index < len(data_acara):
        item = data_acara[index]
        if username in item["pendaftar"]:
            print("Anda sudah terdaftar di acara ini!")
            return

        if len(item["pendaftar"]) >= item["kuota"]:
            print("Kuota pendaftaran untuk acara ini sudah penuh!")
            return

        item["pendaftar"].append(username)
        print(f"Berhasil mendaftar pada acara '{item['nama']}'!")
    else:
        print("Nomor acara tidak ditemukan!")

def lihat_acara_saya(username):
    print("\nACARA YANG SAYA IKUTI")
    acara_saya = []
    for item in data_acara:
        if username in item["pendaftar"]:
            acara_saya.append(item)

    if len(acara_saya) == 0:
        print("Anda belum mendaftar di acara manapun.")
        return False

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Acara", "Kategori", "Tanggal", "Lokasi", "Status"]

    nomor = 1
    for item in acara_saya:
        tabel.add_row([
            nomor,
            item["nama"],
            item["kategori"],
            item["tanggal"],
            item["lokasi"],
            "Terdaftar"
        ])
        nomor += 1

    print(tabel)
    return True

def batalkan_acara_saya(username):
    if not lihat_acara_saya(username):
        return

    print("\nBATALKAN PENDAFTARAN ACARA")
    acara_saya = []
    for item in data_acara:
        if username in item["pendaftar"]:
            acara_saya.append(item)

    nomor = input_int_positif("Masukkan nomor acara yang ingin dibatalkan: ")
    index = nomor - 1

    if 0 <= index < len(acara_saya):
        target = acara_saya[index]
        konfirmasi = input(f"Yakin batal mengikuti '{target['nama']}'? (y/n): ").strip().lower()
        if konfirmasi == "y":
            target["pendaftar"].remove(username)
            print(f"Pendaftaran acara '{target['nama']}' berhasil dibatalkan!")
        else:
            print("Pembatalan dibatalkan.")
    else:
        print("Nomor acara tidak ditemukan!")

def login():
    hapus_layar()
    print("==============================")
    print("      LOGIN ACARA KAMPUS      ")
    print("==============================")
    username = input("Masukkan Username : ").strip()
    password = pwinput.pwinput("Masukkan Password : ")

    if username in USERS and USERS[username]["password"] == password:
        return username, USERS[username]["role"], USERS[username]["nama"]
    else:
        print("\nUsername atau Password salah!")
        input("Tekan Enter untuk mencoba lagi...")
        return None, None, None

def menu_admin(username, nama):
    while True:
        print("\n==============================")
        print("  MENU ADMIN PANITIA -", nama)
        print("==============================")
        print("1. Tambah Acara (Create)")
        print("2. Lihat Semua Acara (Read)")
        print("3. Ubah Data Acara (Update)")
        print("4. Hapus Acara (Delete)")
        print("5. Logout")

        pilihan = input("Pilih menu (1-5): ").strip()
        hapus_layar()

        if pilihan == "1":
            tambah_acara()
        elif pilihan == "2":
            lihat_acara()
        elif pilihan == "3":
            ubah_acara()
        elif pilihan == "4":
            hapus_acara()
        elif pilihan == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan menu tidak valid!")

def menu_user(username, nama):
    while True:
        print("\n==============================")
        print("     MENU MAHASISWA -", nama)
        print("==============================")
        print("1. Lihat Daftar Acara")
        print("2. Daftar Acara")
        print("3. Lihat Acara Saya")
        print("4. Batalkan Pendaftaran")
        print("5. Logout")

        pilihan = input("Pilih menu (1-5): ").strip()
        hapus_layar()

        if pilihan == "1":
            lihat_acara()
        elif pilihan == "2":
            daftar_acara_mhs(username)
        elif pilihan == "3":
            lihat_acara_saya(username)
        elif pilihan == "4":
            batalkan_acara_saya(username)
        elif pilihan == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan menu tidak valid!")

def main():
    while True:
        username, role, nama = login()
        if username is not None:
            hapus_layar()
            print("Selamat datang,", nama)
            if role == "admin":
                menu_admin(username, nama)
            elif role == "user":
                menu_user(username, nama)

main()