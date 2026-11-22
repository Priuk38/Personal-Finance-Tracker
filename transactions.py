from datetime import datetime

def input_transaction():
    """Meminta input dan membuat satu data transaksi."""

    #1 Input tanggal
    while True:
        tanggal = input("Tanggal (YYYY-MM-DD): ")
        try:
            datetime.strptime(tanggal, "%Y-%m-%d")
            break
        except ValueError:
            print("Format tanggal tidak valid. Contoh: 2026-11-22")

    #2 Input jenis transaksi
    while True:
        print("\nJenis Transaksi:")
        print("1. Pemasukan")
        print("2. Pengeluaran")

        pilihan = input("Pilih jenis transaksi (1/2): ")

        if pilihan == "1":
            jenis = "pemasukan"
            break
        elif pilihan == "2":
            jenis = "pengeluaran"
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

    #3 Input kategori dan keterangan
    while True:
        kategori = input("Kategori: ")
        if kategori:
            break
        print("Kategori tidak boleh kosong.")

    while True:
        keterangan = input("Keterangan: ")
        if keterangan:
            break
        print("Keterangan tidak boleh kosong.")

    #4 Input nominal
    while True:
        try:
            nominal = int(input("Nominal (Rp): "))
            if nominal > 0:
                break
            print("Nominal harus lebih besar dari 0.")
        except ValueError:
            print("Nominal harus berupa bilangan bulat.")

    #5 Mengembalikan data transaksi
    return {
        "tanggal": tanggal,
        "jenis": jenis,
        "kategori": kategori,
        "keterangan": keterangan,
        "nominal": nominal
    }

def filter_transactions(data, jenis=None):
    """Menyaring transaksi berdasarkan jenisnya."""
    if jenis is None or jenis == "semua":
        return data
    return [
        transaksi
        for transaksi in data
        if transaksi["jenis"] == jenis
    ]

def display_transactions(data):
    """Menampilkan daftar transaksi."""
    if not data:
        print("\nBelum ada transaksi.")
        return

    print("\n" + "-" * 75)
    print("Daftar Transaksi")
    print("-" * 75)

    for transaksi in data:
        print(f"Tanggal: {transaksi['tanggal']}")
        print(f"Jenis: {transaksi['jenis']}")
        print(f"Kategori: {transaksi['kategori']}")
        print(f"Keterangan: {transaksi['keterangan']}")
        print(f"Nominal: Rp {transaksi['nominal']:,}")
        print("-" * 75)

def get_recent_transactions(data, limit=5):
    return data[-limit:][::-1]
    """Mengambil beberapa transaksi terbaru."""
    sorted_data = sorted(
        data,
        key=lambda transaksi: transaksi["tanggal"],
        reverse=True
    )
    return sorted_data[:limit]
