# Personal Finance Tracker

Aplikasi pengelolaan keuangan pribadi berbasis Python yang berjalan melalui terminal/console. Proyek ini dikembangkan sebagai tugas akhir mata kuliah pemrograman.

Personal Finance Tracker membantu pengguna mencatat pemasukan dan pengeluaran, memantau saldo, serta melihat laporan keuangan bulanan dengan penyimpanan data menggunakan file CSV.

## Features

- **Transaction Management** — Mencatat pemasukan dan pengeluaran beserta kategori, keterangan, tanggal, dan nominal.
- **Transaction Filtering** — Menampilkan seluruh transaksi, pemasukan saja, atau pengeluaran saja.
- **Dashboard** — Menampilkan saldo saat ini dan lima transaksi terbaru.
- **Monthly Report** — Menampilkan total pemasukan, pengeluaran, saldo, rincian pengeluaran per kategori, dan kategori pengeluaran terbesar.
- **Saving Rate** — Menghitung persentase sisa pemasukan setelah dikurangi pengeluaran.
- **CSV Storage** — Menyimpan transaksi agar tetap tersedia ketika program dijalankan kembali.
- **CSV Export** — Mengekspor seluruh transaksi dan laporan bulanan ke file CSV.

## Requirements

Untuk menjalankan versi source code:

- Windows, Linux, atau macOS.
- Python 3.
- Terminal atau command prompt.

Tidak memerlukan library eksternal tambahan untuk menjalankan program utama.

## Project Structure

```text
Personal-Finance-Tracker/
│
├── main.py
├── transactions.py
├── reports.py
├── storage.py
├── run.bat
│
├── data/
│   └── transactions.csv
│
├── exports/
│
├── README.md
└── .gitignore
```

### Module Description

| File | Description |
|---|---|
| `main.py` | Menu utama dan integrasi seluruh modul. |
| `transactions.py` | Input, filter, dan tampilan transaksi. |
| `reports.py` | Perhitungan saldo dan laporan bulanan. |
| `storage.py` | Pengelolaan penyimpanan dan ekspor CSV. |
| `run.bat` | Menjalankan program melalui Windows batch file. |

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/Priuk38/Personal-Finance-Tracker.git
```

### 2. Open Project Directory

```bash
cd Personal-Finance-Tracker
```

### 3. Run the Program

Menggunakan Python:

```bash
python main.py
```

Atau melalui Windows:

```text
run.bat
```

## Executable Version

Aplikasi juga dapat dikemas menjadi executable Windows menggunakan PyInstaller.

Untuk menggunakan versi executable:

1. Unduh file ZIP aplikasi dari GitHub Releases.
2. Ekstrak seluruh isi ZIP.
3. Jalankan `PersonalFinanceTracker.exe`.

Pastikan file executable tetap berada bersama folder `_internal`, `data`, dan `exports`.

## Data Storage

Aplikasi menggunakan file CSV sebagai media penyimpanan transaksi.

### Transaction CSV

File: `data/transactions.csv`

| Column | Description |
|---|---|
| `tanggal` | Tanggal transaksi dengan format YYYY-MM-DD. |
| `jenis` | Jenis transaksi: pemasukan atau pengeluaran. |
| `kategori` | Kategori transaksi. |
| `keterangan` | Deskripsi singkat transaksi. |
| `nominal` | Jumlah uang dalam Rupiah. |

### Export Files

Hasil ekspor disimpan dalam folder `exports/`:

- `transactions_export.csv` — Seluruh data transaksi.
- `monthly_report.csv` — Ringkasan laporan keuangan bulanan.

## Saving Rate Formula

Saving rate dihitung menggunakan rumus:

```text
Saving Rate = ((Income - Expenses) / Income) × 100%
```

Apabila total pemasukan bernilai nol, saving rate tidak dihitung untuk menghindari pembagian dengan nol.

## Development Team

Developed as a group final project for a programming course.

| Role | Responsibility |
|---|---|
| Main Developer / Integrator | Main menu, dashboard, transaction flow, and module integration. |
| Report Developer | Monthly financial calculations and report generation. |
| Storage Developer | CSV data storage and export functionality. |

## License

This project was developed for educational purposes as part of a university programming course.