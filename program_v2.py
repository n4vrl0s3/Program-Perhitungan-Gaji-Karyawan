#Prosedur Pokok
def pokok(jam_kerja):
    gaji_pokok = 20000
    if jam_kerja > 7:
        gaji_lembur = (jam_kerja - 7) * gaji_pokok * 1.5
        gaji_pokok += gaji_lembur
    return gaji_pokok

#Prosedur Lembur
def lembur(jam_kerja):
    gaji_lembur = 0
    if jam_kerja > 7:
        gaji_lembur = (jam_kerja - 7) * 20000 * 1.5
    return gaji_lembur

#Prosedur Makan
def makan(jam_kerja):
    uang_makan = 0
    if jam_kerja >= 8:
        uang_makan = 5000
    return uang_makan

#Prosedur Jasa
def jasa(jam_kerja):
    uang_transport_lembur = 0
    if jam_kerja >= 9:
        uang_transport_lembur = 4000
    return uang_transport_lembur

#Masukkan data
NIP = "312310505"
Nama = "Muhammad Agisna Yudiansyah"
Jumlah_jam_kerja = 17

#Proses dan Cetak
gaji_pokok = pokok(Jumlah_jam_kerja)
gaji_lembur = lembur(Jumlah_jam_kerja)
uang_makan = makan(Jumlah_jam_kerja)
uang_transport_lembur = jasa(Jumlah_jam_kerja)

total_gaji = gaji_pokok + gaji_lembur + uang_makan + uang_transport_lembur

print("LAPORAN GAJI HARIAN KARYAWAN")
print("PT.XYZ")
print("Bulan : November 2023")
print()
print("====================================================================================================================")
print("|    NIP    |            Nama            | Jam Kerja |  Gaji Pokok  |    Lembur    | Uang Makan | Transport Lembur |")
print("====================================================================================================================")
print("|           |                            |           |              |              |            |                  |")
print(f"| {NIP} | {Nama} |   {Jumlah_jam_kerja} Jam  | Rp. {gaji_pokok} | Rp. {gaji_lembur} |  Rp. {uang_makan}  |     Rp. {uang_transport_lembur}     |")
print("|           |                            |           |              |              |            |                  |")
print("====================================================================================================================")
print()
print(f"Total Gaji : {total_gaji}")
print()
