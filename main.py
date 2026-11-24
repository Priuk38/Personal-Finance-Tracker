from storage import (
    load_transactions,
    save_transactions,
    export_transactions,
    export_monthly_report
)

from transactions import (
    input_transaction,
    filter_transactions,
    display_transactions,
    get_recent_transactions
)

from reports import (
    calculate_balance,
    generate_monthly_report
)

def format_rupiah(amount):
    """Mengubah angka menjadi format Rupiah."""
    return f"Rp {amount:,.0f}".replace(",", ".")

def show_dashboard(data):
    """Menampilkan saldo dan transaksi terbaru."""
    print("\n" + "=" * 45)
    print("         PERSONAL FINANCE TRACKER")
    print("=" * 45)

    balance = calculate_balance(data)
    print(f"\nSaldo saat ini: {format_rupiah(balance)}")
    print("\nTransaksi terbaru:")
    recent = get_recent_transactions(data, 5)

    if not recent:
        print("Belum ada transaksi.")
    else:
        for transaksi in recent:
            jenis = transaksi["jenis"].capitalize()
            print(
                f"- {transaksi['tanggal']} | "
                f"{jenis} | "
                f"{transaksi['kategori']} | "
                f"{format_rupiah(transaksi['nominal'])}"
            )
    print("=" * 45)

def show_transaction_menu(data):
    """Menampilkan transaksi berdasarkan filter."""
    while True:
        print("\n=== DAFTAR TRANSAKSI ===")
        print("1. Semua transaksi")
        print("2. Pemasukan saja")
        print("3. Pengeluaran saja")
        print("0. Kembali")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            display_transactions(filter_transactions(data, "semua"))
        elif pilihan == "2":
            display_transactions(filter_transactions(data, "pemasukan"))
        elif pilihan == "3":
            display_transactions(filter_transactions(data, "pengeluaran"))
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")

def show_monthly_report(data):
    """Meminta bulan dan tahun, lalu menampilkan laporan."""
    try:
        month = int(input("Masukkan bulan (1-12): "))
        year = int(input("Masukkan tahun (contoh: 2026): "))
        report = generate_monthly_report(data, month, year)

    except ValueError:
        print("Bulan atau tahun tidak valid.")
        return None

    print("\n" + "=" * 45)
    print(f" LAPORAN KEUANGAN {report['bulan']}")
    print("=" * 45)

    print(f"Total pemasukan     : {format_rupiah(report['total_pemasukan'])}")
    print(f"Total pengeluaran   : {format_rupiah(report['total_pengeluaran'])}")
    print(f"Saldo               : {format_rupiah(report['saldo'])}")

    if report["saving_rate"] is None:
        print("Saving rate          : Tidak dapat dihitung (pemasukan nol)")
    else:
        print(f"Saving rate         : {report['saving_rate']:.2f}%")
    
    print("\nRincian pengeluaran:")
    if report["expense_breakdown"]:
        for kategori, nominal in report["expense_breakdown"].items():
            print(f"- {kategori}: {format_rupiah(nominal)}")
    else:
        print("Tidak ada pengeluaran pada bulan ini.")

    print(f"\nKategori terbesar : {report['kategori_terbesar']}")
    print("=" * 45)

    return report

def main():
    """Menjalankan aplikasi Personal Finance Tracker."""
    data = load_transactions()

    while True:
        show_dashboard(data)

        print("\nMENU UTAMA")
        print("1. Tambah transaksi")
        print("2. Lihat transaksi")
        print("3. Laporan bulanan")
        print("4. Ekspor semua transaksi")
        print("5. Ekspor laporan bulanan")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            transaksi_baru = input_transaction()
            data.append(transaksi_baru)
            save_transactions(data)
            print("\nTransaksi berhasil disimpan.")
        elif pilihan == "2":
            show_transaction_menu(data)
        elif pilihan == "3":
            show_monthly_report(data)
        elif pilihan == "4":
            export_transactions(data)
        elif pilihan == "5":
            report = show_monthly_report(data)
            if report is not None:
                export_monthly_report(report)
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan Personal Finance Tracker!")
            break
        else:
            print("\nPilihan tidak valid. Silahkan coba lagi.")

if __name__ == "__main__":
    main()