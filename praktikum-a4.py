print ('praktikum-a4.py,\n')
import os
os.system ('clear,\n')

nim = ['2','3','1','0','3','1','0','0','2']
# nim2 = '231031002'

print (nim)
 # print(nim2[1:3])
 
 # akses item 
print (f' item indeks 0: {nim[0]}')
print (f' item indeks 4: {nim[4]}')
print (f' item indeks terakhir: {nim[len(nim)-1]}')

# akses indeks negatif 
print (f' item indeks terakhir: {nim[-1]}')
print (f' item indeks pertama: {nim[-len(nim)]}')
print (f' item indeks 6 [-3]: {nim[-3]}')
print (f' item indeks 4 [-5]: {nim[-5]}')
print (f' item indeks 7 [-2]: {nim[-2]}')

# akses indeks batas

print (f'item indeks 1,2,.....: \n {nim[1:]}')
print (f'item indeks 3,4,.....: \n {nim[3:]}')
print (f'item indeks 0,1,2,.....: \n {nim[:3]}')
print (f'item indeks 0,1,2,3.....: \n {nim[:4]}')
print (f'item indeks semua: \n {nim[:]}')

print (f'item indeks [:8]: \n {nim[-1]}')
print (f'item indeks [:6]: \n {nim[-3]}')

# pengirisan 

print (f'item indeks 1,2: \n {nim[1:3]}')
print (f'item indeks 2,3,4 : \n {nim[2:5]}')
print (f'item indeks kosong : \n {nim[3:3]}')
print (f'item indeks [8:8] kosong : \n {nim[-1:-1]}')
print (f'item indeks [1:8] kosong : \n {nim[1:-1]}')
print (f'item indeks [2:7] kosong : \n {nim[2:-2]}')

# tugas list
data = ['M. Faiz ilyas',2023,'Aktif']
nilai= [90,89,93,97]

# status kuliah
print (f'{data[0]} status kuliah : {data[2]}')
# nilai terbesar
print (f'data terbesar nilai adalah : {max(nilai)}')
# nilai terkecil
print (f'data terkecil nilai adalah : {min(nilai)}')
#rata rata nilai
print (f'rata rata nilai adalah : {sum(nilai)/len(nilai)}')

#tugas tuple
data = ('Faiz',2023,'Aktif')
nilai= (90,89,93,97)

# jumlah nilai
print (f'jumlah nilai faiz adalah : {len(nilai)}')
# data terbesar
print (f'data terbesar nilai adalah : {max(nilai)}')
# data terkecil
print (f'data terkecil nilai adalah : {min(nilai)}')
# rata rata
print (f'rata rata nilai adalah : {sum(nilai)/len(nilai)}')

#nested list
data = [['Faiz',2023,'Aktif'],

[90,89,93,97],
[20,22],
['S1-Reguler','Ganjil']]

# program pendidikan 
print (f'program pendidikan {data[0][0]} : {data[3][0]}')
# angkatan
print (f' angkatan : {data[0][1]}-{data[3][1]}')
# jumlah nilai
print (f'jumlah nilai faiz adalah : {len(data[1])} ')
#nilai terbesar
print (f' jumlah nilai terbesar adalah : {max(data[1])} ')
# nilai terkecil
print (f' jumlah nilai terkecil adalah : {min(data[1])} ')
# rata rata nilai
print (f'rata rata nilai adalah : {sum(data[1])/len(data[1])}\n\n\n')

#tugas : tambahkan MATKUL dan SKS ke dalam data

matkul = ['pancasila','pendidikan agama islam','bahasa indonesia','kalkulus dasar']
sks    = [2,3,3,2]
data.append(matkul)
data.append(sks)

# mata kuliah 1 : matkul1 dengan jumlah 2 SKS
print(f'{data[4][0]} dengam jumlah {data[-1][0]} sks')

# mata kuliah 2 : matkul2 dengan jumlah 3 SKS
print(f'{data[4][1]} dengam jumlah {data[-1][1]} sks')

# mata kuliah 3 : matkul3 dengan jumlah 3 SKS
print(f'{data[4][2]} dengam jumlah {data[-1][2]} sks')

# mata kuliah 4 : matkul4 dengan jumlah 2 SKS
print(f'{data[4][3]} dengam jumlah {data[-1][3]} sks')

#Menambahkan matkul ke-5
data[4].append('Wawasan Cinta IPTEK dan IMTAQ')
data[5].append(2)
print(f'{data[4][4]} dengam jumlah {data[-1][4]} sks')
#print(data)

#Tambahkan 3 matkul dengan sks nya
#matkul 6 & sks nya
data[4].append('Pancasila')
data[5].append(2)
#matkul 7 & sks nya
data[4].append('pemrograman')
data[5].append(3)
#matkul 8 & sks nya
data[4].append('Sains Terpadu')
data[5].append(3)

# Mata kuliah 6: Matkul6 dengan jumlah 2 sks
print(f'{data[4][5]} dengam jumlah {data[-1][5]} sks')
# Mata kuliah 7: Matkul7 dengan jumlah 2 sks
print(f'{data[4][6]} dengam jumlah {data[-1][6]} sks')
# Mata kuliah 8: Matkul8 dengan jumlah 2 sks
print(f'{data[4][7]} dengam jumlah {data[-1][7]} sks')

#Tambahkan 8 nilai masing-masing
data[1].append(92)
data[1].append(94)
data[1].append(91)
data[1].append(92)

print(data[0][0])
print(data[3][0])
print(data[2][0:])








