from datetime import datetime

def calculate_balance(data):
    """Menghitung saldo keseluruhan dari semua transaksi."""
    total_income = sum(
        transaksi["nominal"]
        for transaksi in data
        if transaksi["jenis"].lower() == "pemasukan"
    )

    total_expense = sum(
        transaksi["nominal"]
        for transaksi in data
        if transaksi["jenis"].lower() == "pengeluaran"
    )
    return total_income - total_expense

def generate_monthly_report(data, month, year):
    """Menghasilkan laporan keuangan berdasarkan bulan dan tahun."""

    #Validasi bulan dan tahun
    datetime(year, month, 1)  # Akan memunculkan ValueError jika tidak valid
    monthly_data = []

    for transaksi in data:
        try:
            transaction_date = datetime.strptime(
                transaksi["tanggal"], "%Y-%m-%d"
            )
            if transaction_date.month == month and transaction_date.year == year:
                monthly_data.append(transaksi)
        except (ValueError, KeyError, TypeError):
            print("Peringatan: Ada transaksi dengan tanggal yang tidak valid.")

    total_income = sum(
        transaksi["nominal"]
        for transaksi in monthly_data
        if transaksi["jenis"].lower() == "pemasukan"
    )
    total_expense = sum(
        transaksi["nominal"]
        for transaksi in monthly_data
        if transaksi["jenis"].lower() == "pengeluaran"
    )

    #Mengelompokkan pengeluaran berdasarkan kategori
    expense_breakdown = {}

    for transaksi in monthly_data:
        if transaksi["jenis"].lower() == "pengeluaran":
            kategori = transaksi["kategori"]
            if kategori not in expense_breakdown:
                expense_breakdown[kategori] = 0
            expense_breakdown[kategori] += transaksi["nominal"]

    #Menentukan kategori pengeluaran terbesar
    if expense_breakdown:
        largest_category = max(
            expense_breakdown, 
            key=expense_breakdown.get
            )
    else:
        largest_category = "Tidak ada"

    #Menghitung saving rate
    if total_income > 0:
        saving_rate = round(((total_income - total_expense) / total_income) * 100, 2)
    else:
        saving_rate = None

    return {
        "bulan": f"{year}-{month:02d}",
        "total_pemasukan": total_income,
        "total_pengeluaran": total_expense,
        "saldo": total_income - total_expense,
        "saving_rate": saving_rate,
        "expense_breakdown": expense_breakdown,
        "kategori_terbesar": largest_category,
    }