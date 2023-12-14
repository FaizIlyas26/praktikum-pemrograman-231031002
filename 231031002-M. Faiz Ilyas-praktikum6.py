a = True

while a:
    pilih = input ('pilihan: ')
    if pilih == 'ya':
        print('selamat datang')
        break
    elif pilih == 'tidak':
        print('sampai jumpa:')
        break
    else:
        print('pilihan tidak valid, coba lagi')
        continue
    
    print()
    
   # a = True#: Variabel a diinisialisasi dengan nilai True. Variabel ini digunakan sebagai kondisi untuk loop while.

#while a:#: Memulai loop while yang akan terus berjalan selama kondisi a bernilai True.

#Di dalam loop while:

 #   pilih = input('pilihan: ')#: Menggunakan fungsi input untuk meminta input dari pengguna dan menyimpannya dalam variabel pilih.

  #  if pilih == 'ya':#: Mengecek apakah input pengguna adalah string 'ya'.

#Jika benar, mencetak 'selamat datang' dan keluar dari loop dengan menggunakan pernyataan break. Ini menghentikan eksekusi loop.
   # elif pilih == 'tidak':#: Mengecek apakah input pengguna adalah string 'tidak'.

#Jika benar, mencetak 'sampai jumpa' dan keluar dari loop dengan menggunakan pernyataan break.
    #else:#: Blok ini dijalankan jika input pengguna bukan 'ya' atau 'tidak'.

# Mencetak 'pilihan tidak valid, coba lagi'.
# Melanjutkan ke iterasi berikutnya dari loop menggunakan pernyataan continue. Ini menyebabkan program kembali ke awal loop dan meminta input pengguna lagi.