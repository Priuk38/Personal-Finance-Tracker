import csv
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).resolve().parent
else: 
    BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
EXPORT_DIR = BASE_DIR / "exports"
TRANSACTIONS_FILE = DATA_DIR / "transactions.csv"

#Struktur kolom transaksi
TRANSACTION_FIELDS = [
    "tanggal",
    "jenis",
    "kategori",
    "keterangan",
    "nominal"
]

def load_transactions():
    """Membaca seluruh transaksi dari file CSV."""

    #Membuat folder data jika belum tersedai
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    #Jika file belum ada, buat file baru dengan header
    if not TRANSACTIONS_FILE.exists():
        save_transactions([])
        return []
    transactions = []
    with open(TRANSACTIONS_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row["nominal"] = int(row["nominal"])
                transactions.append(row)
            except (ValueError, KeyError, TypeError):
                print("Peringatan: Ada baris CSV yang tidak valid.")
    return transactions

def save_transactions(data):
    """Menyimpan seluruh transaksi ke file CSV."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(TRANSACTIONS_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=TRANSACTION_FIELDS
        )
        writer.writeheader()
        writer.writerows(data)

def export_transactions(data):
    """Mengekspor seluruh transaksi ke CSV."""
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    export_file = EXPORT_DIR / "transactions_export.csv"
    with open(export_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=TRANSACTION_FIELDS
        )
        writer.writeheader()
        writer.writerows(data)
    print(f"Ekspor transaksi berhasil: {export_file}")
    return export_file

def export_monthly_report(report):
    """Mengekspor Laporan Bulanan ke CSV."""
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    export_file = EXPORT_DIR / "monthly_report.csv"
    fields = [
        "bulan",
        "total_pemasukan",
        "total_pengeluaran",
        "saldo",
        "saving_rate",
        "kategori_pengeluaran",
        "nominal_per_kategori",
        "kategori_terbesar"
    ]

    #Mengambil rincian pengeluaran per kategori
    breakdown = report["expense_breakdown"]

    #Tetap buat satu baris jika belum ada pengeluaran
    if not breakdown:
        breakdown = {"Tidak ada": 0}
    with open(export_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for kategori, nominal in breakdown.items():
            writer.writerow({
                "bulan": report["bulan"],
                "total_pemasukan": report["total_pemasukan"],
                "total_pengeluaran": report["total_pengeluaran"],
                "saldo": report["saldo"],
                "saving_rate": f"{report['saving_rate']:.2f}%" if report["saving_rate"] is not None else "Tidak tersedia",
                "kategori_pengeluaran": kategori,
                "nominal_per_kategori": nominal,
                "kategori_terbesar": report["kategori_terbesar"],
            })
    print(f"Ekspor laporan bulanan berhasil: {export_file}")
    return export_file