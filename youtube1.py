# Dedi yanto
# Universitas Kristen Duta Wacana


'''Dedi sedang belanja di sebuah mall di jepang. dalam mall tersebut ternyata sedang ada
promo diskon diseluruh mall. Diskon tersebut berlaku pemotongan 10% untuk setiap pembelanjaan
diatas sama dengan 100rb dan 25% untuk setiap pembelanjaan diatas sama dengan 250000. buatlah
sebuah program yang dapat menampilkan harga barang serta diskon yang didapatkan, total semua diskon,
serta jumlah uang yang harus dibayarkan oleh Dedi.'''

'''
Input:1. barang apa saja yang ingin dibeli
      2. harga barang tersebut(perbarang)

Proses:1. mengubah barang yang telah di input menjadi sebuah list
       2. menghitung banyak barang yang akan dibeli
       3. menanyakan harga barang satu persatu sesuai inputan user
       4. mengukur apakah barang tersebut terkena diskon 10% atau 25% atau tidak ada diskon
       5. menjumlah seluruh total diskon yang didapatkan
       6. mencatat diskon yang didapatkan perbarang
       7. menjumlahkan harga/uang yang harus dibayarkan dedi

Output:1. diskon yang didapatkan (perbarang)
       2. total semua diskon
       3. jumlah uang yang harus dibayar oleh dedi

'''

barang = input("Masukkan barang apa saja yang ingin dibeli(pisahkan dengan koma): ")
lstbarang = barang.split(",")
bnykbarang = len(lstbarang)
totaldiskon = 0
jumlah = 0

for i in range(bnykbarang):
    harga = "Berapa harga barang "+lstbarang[i]+" ?:"
    barang1 = input(harga)
    jumlah += int(barang1)
    if int(barang1) >= 100000 and int(barang1)< 250000:
        diskon = float(float(barang1)*0.1)
        totaldiskon += diskon
        print("Harga",lstbarang[i],"\t Rp. ",barang1,"\t","Diskon Rp. ",diskon)
    elif int(barang1)>= 250000:
        diskon = float(float(barang1)*0.25)
        totaldiskon += diskon
        print("Harga",lstbarang[i],"\t Rp. ",barang1,"\t","Diskon Rp. ",diskon)
    else:
        print("Harga",lstbarang[i],"\t Rp. ",barang1,"\t","Diskon Rp. ",0)
    

jmlhtotal = jumlah - totaldiskon

print("Total diskon yang anda dapatkan adalah sebesar: Rp. ",totaldiskon)
print("Total uang yang harus anda bayarkan adalah: Rp. ",jmlhtotal)






    
    









