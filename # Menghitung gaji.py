# Menghitung gaji
def hitung_gaji(rate, total_jam_kerja):
    jam_normal = 40
    if total_jam_kerja > jam_normal:
        jam_lembur = total_jam_kerja - jam_normal
    else:
        jam_lembur = 0

    gaji_normal = rate * jam_normal
    gaji_lembur = (rate * 1.5) * jam_lembur
    total_gaji = gaji_normal + gaji_lembur
    return total_gaji

# Menghitung tabungan
def hitung_tabungan(total_gaji, pengeluaran):
    tabungan = total_gaji - pengeluaran
    if tabungan > 0:
        return f"Bisa menabung. Jumlah tabungan: Rp. {tabungan}"
    elif tabungan == 0:
        return "Tidak bisa menabung."
    else:
        return "Cari tambahan."

# Nilai-nilai variatif (bisa diganti sesuai kebutuhan)
rate = 15000
total_jam_kerja = 52
pengeluaran = 600000

# Menghitung gaji
total_gaji = hitung_gaji(rate, total_jam_kerja)

# Menghitung tabungan
hasil_tabungan = hitung_tabungan(total_gaji, pengeluaran)

# Output
print(f"Total Gaji Mr. John: Rp. {total_gaji}")
print(hasil_tabungan)
