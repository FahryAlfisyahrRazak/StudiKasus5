def hitung_biaya_parkir(jenis_kendaraan, jam_masuk, jam_keluar):

    jenis = jenis_kendaraan
    
    if jenis == "Mobil":
        tarif_per_jam = 5000
    elif jenis == "Motor":
        tarif_per_jam = 3000
    else:
        tarif_per_jam = 0
        print("Jenis kendaraan tidak dikenali!")


    lama_parkir = jam_keluar - jam_masuk

    total_biaya = tarif_per_jam * lama_parkir

    return total_biaya, lama_parkir

jenis_kendaraan = input("Masukkan jenis kendaraan (Mobil/Motor): ")
jam_masuk = int(input("Masukkan jam masuk (format 24 jam): "))
jam_keluar = int(input("Masukkan jam keluar (format 24 jam): "))

total_biaya, lama_parkir = hitung_biaya_parkir(jenis_kendaraan, jam_masuk, jam_keluar)

print("Jenis kendaraan :", jenis_kendaraan)
print("Jam masuk :", jam_masuk)
print("Jam keluar :", jam_keluar)
print("Lama parkir :", lama_parkir)
print("Total biaya :", total_biaya)