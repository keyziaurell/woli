nama = input ("Masukkan nama : ")
saldo = int(input("Masukkan jumlah saldo anda : "))
print ("Hello,", nama)
print ("""Selamat datang di Wocker!
Woli Expense Tacker siap membantumu. Simpan dan atur keuanganmu!""")

menu = ["1. Pengeluaran", "2. Riwayat", "3. Atur keuangan", "4. Menabung", "5. Reminder", "6. Keluar"]

print (" ")
print ("====== MENU ======")
for item in menu :
    print (item)

pilih_menu = int(input(" Pilih menu (1/2/3/4/5/6):"))

if pilih_menu == 1:
    print (" ")
    print ("====== PENGELUARAN ======")
    print ("Saldo anda : ", saldo)

    tanggal = int (input("Tanggal : "))
    bulan = input ("Bulan : ")
    tahun = int(input ("Tahun : "))

    total_pengeluaran = 0
    ulang = "y" 

    while ulang == "y":
        jam = float(input("Jam: "))
        pengeluaran = int(input("Masukkan pengeluaran: "))
        kegunaan = input("Dipakai untuk apa?: ")

        total_pengeluaran = total_pengeluaran + pengeluaran

        print (" ")
        print ("====== PENGELUARAN HARI INI ======")
        print ("Tanggal : ", str(tanggal) + " " + bulan + " " + str(tahun))
        print ("Jam : ", jam)
        print("Pengeluaran:", pengeluaran)
        print("Kegunaan:", kegunaan)
        print("Total pengeluaran:", total_pengeluaran)

        ulang = input("Tambah pengeluaran lagi? (y/n): ").lower()

    saldo = saldo - total_pengeluaran
    print(" ")
    print("====== RINGKASAN AKHIR ======")
    print("Total pengeluaran hari ini:", total_pengeluaran)
    print("Sisa saldo:", saldo)

elif pilih_menu == 2 :
    print ("====== RIWAYAT ======")
