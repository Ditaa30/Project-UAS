Menu = {
    "Ayam Bakar" : 15000,
    "Ayam Geprek": 17000,
    "Mie Nyemek" : 13000,
    "Jus Mangga" : 10000,
    "Nasi Goreng": 13000,
    "Es Teh"     : 5000,
}
print("=============================== Daftar Menu ===============================")
for i in Menu:
    print("Daftar Menu : ", i,"\t Harga : ",Menu[i])
print("Pembelian diatas Rp40.000,- mendapatkan diskon 20%")
print("=====================================================")
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * Menu[beli]
if bayar > 40000:
    diskon = bayar*20/100
    total = bayar - diskon
else:
    total = bayar
    
print("=========================== Struk Pembayaran ===========================")
print("Menu yang dipesan        : ",beli)
print("Jumlah yang dipesan      : ",jumlah)
print("Total Biaya              : ",bayar)
print("Total yang harus dibayar : ",total)
