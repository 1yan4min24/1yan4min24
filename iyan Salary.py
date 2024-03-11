def hitung_gaji(jam_kerja, tarif_per_jam):
    if jam_kerja <= 40:
        gaji = jam_kerja * tarif_per_jam
    else:
        gaji = (40 * tarif_per_jam) + ((jam_kerja - 40) * tarif_per_jam * 1.5)
    return gaji

def main():
    jam_kerja = float(input("Masukkan jumlah jam kerja: "))
    tarif_per_jam = float(input("Masukkan tarif per jam: "))
    
    gaji = hitung_gaji(jam_kerja, tarif_per_jam)
    print("Gaji yang diterima adalah:", gaji)

if __name__ == "__main__":
    main()