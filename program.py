print("NIM   : 312310505")
print("Nama  : Muhammad Agisna Yudiansyah")
print("Prodi : Teknik Informatika")
print("Kelas : TI.23.B.2")
print("==================================")
print("")

def THP(GP,JA,HK):
    TP = (0.1 * GP) 
    TA = (JA * (0.05 * GP)) 
    TTr = 20000 * HK
    BPJS = 75000
    PJK = (0.15 * (GP+TA+TP))
    GB = int (GP+TP+TA+TTr) - int (PJK+BPJS)
    Total = int (GP+TP+TA+TTr)
    Tunjangan = int (TP+TA+TTr)
    Potongan = int (PJK+BPJS)

    def total_tunjangan (Tunjangan):
        y = str (Tunjangan)
        if len (y) <= 3:
            return "Rp. "+ y
        else:
            p = y [:-3]
            l = y [-3:]
            return total_tunjangan(p)+ "." + l
    print ("Tujangan :",total_tunjangan(Tunjangan))

    
    def gaji_total (Total):
        x = str (Total)
        if len (x) <= 3:
            return "Rp. "+ x
        else:
            c = x [:-3]
            d = x [-3:]
            return gaji_total(c)+ "." + d
    print ("Gaji Total :", gaji_total(Total))

    def total_potongan (Potongan):
        h = str (Potongan)
        if len (h) <=3:
            return "Rp. "+ h
        else:
            v = h [:-3]
            w = h [-3:]
            return total_potongan(v)+ "." + w
    print ("Potongan Pajak 15% + BPJS :", total_potongan(Potongan))

    def gaji_bersih (GB):
        z = str (GB)
        if len (z) <= 3:
            return "Rp. "+ z
        else:
            a = z [:-3]
            b = z [-3:]
            return gaji_bersih (a)+ "." + b
    print ("Gaji Bersih : " , gaji_bersih(GB))
    
GP = int (input("Input Gaji Pokok : Rp. "))
JA = int (input("Input Jumlah Anak : "))
HK = int (input("Input Jumlah Hari Kerja : "))

THP(GP,JA,HK)
