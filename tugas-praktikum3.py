print('tugas-praktikum3.py','\n')

nama= input('masukkan nama karyawan: ')
pendapatan= int (input('masukkan pendapatan : '))
print()

print(f'masukkan nama {nama}')
print(f'masukkan pendapatan {pendapatan}')
if pendapatan > 1000: 
    print('status: berhak')
else:
    print('status: tidak berhak')