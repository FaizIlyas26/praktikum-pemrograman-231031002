print('tugas2 genap.py')
print()

print('nomor 1')
try:
     waktu_awal = input("Masukkan waktu awal (Contoh : 01:00): ")
     jam, menit = map(int, waktu_awal.split(':'))

     jam_tambah = int(input("Masukkan jumlah jam yang akan ditambahkan (Contoh: 2): "))
     menit_tambah = int(input("Masukkan jumlah menit yang akan ditambahkan: "))

     jam_akhir = (jam + jam_tambah + (menit + menit_tambah) // 60) % 24
     menit_akhir = (menit + menit_tambah) % 60

     waktu_akhir = f'{jam_akhir:02d}:{menit_akhir:02d}'

     print(f'Waktu sekarang menunjukkan Pukul {waktu_akhir}')
except ValueError:
     print('Format yang anda masukkan harus lengkap (contoh 12:00)')
    
print('-----------------------------')  
    
print('nomor 2')

jam = int(input("Masukkan jam Pertama"))
menit = int(input("masukkan Menit Pertama"))
detik = int(input("Masukkan detik Pertama"))

jam1 = int(input("Masukkan jam Kedua"))
menit1 = int(input("Masukkan Menit Kedua"))
detik1 = int(input("Masukkan detik kedua"))

t_detik1 = (jam * 3600) + (menit * 60) + detik
t_detik2 =(jam1 * 3600) + (menit1 * 60) + detik1

Sel_detik = abs(t_detik1 - t_detik2)

sel_jam = Sel_detik // 3600
S_detik = Sel_detik % 3600
sel_menit = S_detik // 60
Sel_detik = S_detik % 60

print(f"Selisih Waktu: {sel_jam} jam, {sel_menit} menit,{Sel_detik} detik")




