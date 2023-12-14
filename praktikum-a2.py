print('praktikum-a2\n')

print("Nama  : M. Faiz Ilyas")
print("NIM   : 231031002")
print("Prodi : sistem informasi-A\n")

# INI OPERATOR ASSIGMENT
a = 19
print('Nilai a adalah',a)
a += 3
print('Nilai a+= sekarang adalah',a,'\n')

a = 19
print('Nilai a adalah',a)
a -= 3
print('Nilai a-= sekarang adalah',a,'\n')

a = 19
print('Nilai a adalah',a)
a *= 2
print('Nilai a*= sekarang adalah',a,'\n')

a = 19
print('Nilai a adalah',a)
a /= 2
print('Nilai a/= sekarang adalah',a,'\n')

a = 3
print('Nilai a adalah',a)
a **= 2
print('Nilai a**= sekarang adalah',a,'\n')

a = 35
print('Nilai a adalah',a)
a //= 32
print('Nilai a%= sekarang adalah',a,'\n')

# TUGAS MELANJUTKAN UNTUK OPERATOR SELANJUTNYA LINE 25-LINE 59

# Shifting
c= 0b0100
print("nilai c =",format(c, "04b"))
c >>= 1
print('nilai c>>=1 akan menjadi', format (c, '04b'))
c = 0b0100
c <<=1
print('nilai c<<=1 akan menjadi', format (c, '04b'))

# OPERATOR PERBANDINGAN
a = 9
b = 13
print('\n---------Besar dari 13')
hasil = a > 13
print(a, '>13 adalah hasil',hasil,'\n')

print('\n---------Besar dari 13')
hasil = a < 13
print(a, '<13 adalah hasil',hasil,'\n')


hasil = b > 13
print(b, '>13 adalah hasil',hasil,'\n')

hasil = a < 2
print(a,'<13 adalah hasil', hasil,'\n' )

print('\n---------Besar atau sama dari 13 ujung NIM')
# Hasil = a >= 13
print('\n---------Besar dari 13')
hasil = a < 13
print(a,'<2 adalah hasil', hasil,'\n' )

# Hasil = b >= 13
print('\n---------Besar dari 13')
hasil = b > 13
print(b, '>2 adalah hasil',hasil,'\n')

print('\n-------------Kecil atau sama dari 13 ujung NIM')
# Hasil = a <=13
print('\n---------kecil dari 13')
hasil = a < 13
print(a, '<2 adalah hasil',hasil,'\n')

# Hasil = b <=13
print('\n---------kecil dari 13')
hasil = b < 13
print(b, '<2 adalah hasil',hasil,'\n')

print('\n---------- sama dari 13 ujung NIM')
# Hasil = a == 13
print('\n---------sama dari 13')
hasil = a == 13
print(a, '==2 adalah hasil',hasil,'\n')

# Hasil = b == 13
print('\n---------sama dari 13')
hasil = b == 13
print(b, '==2 adalah hasil',hasil,'\n')


print('\n---------- tidak sama dari 13 ujung NIM')
# Hasil = a !=13
print('\n--------- tidak sama dari 13')
hasil = a != 13
print(a, '!=2 adalah hasil',hasil,'\n')

# Hasil = a !=13
print('\n--------- tidak sama dari 13')
hasil = b != 13
print(b, '!=2 adalah hasil',hasil,'\n')

# Operator Logika
a = True
b = False
print('\n=======ANd=======')
hasil = a and a
print(a,'and',a,'hasilnya =',hasil)

hasil = a and b
print(a,'and',b,'hasilnya =',hasil)

hasil = b and a
print(b,'and',a,'hasilnya =',hasil)

hasil = b and b
print(b,'and',b,'hasilnya =',hasil)

print('\n=======OR=======')
# Tugas hasil = a or a
hasil = a or a
print(a, 'OR',a,'hasilnya=', hasil)

# Tugas hasil = a or b
hasil = a or b
print(a, 'OR',b,'hasilnya=', hasil)

# Tugas hasil = b or a
hasil = b or a
print(b, 'OR',a,'hasilnya=', hasil)

# Tugas hasil = b or b
hasil = b or b
print(b, 'OR',b,'hasilnya=', hasil)

print('\n=======XOR=======')

hasil = a ^ a
print(a, 'XOR',a,'hasilnya=', hasil)

hasil = a ^ b
print(a, 'XOR',b,'hasilnya=', hasil)

hasil = b ^ a
print(b, 'XOR',a,'hasilnya=', hasil)

hasil = b ^ b
print(b, 'XOR',b,'hasilnya=', hasil)


print('\n=======NOT=======')
hasil = not a
print('not',a,'hasilnya=',hasil)

hasil = not b
print('not',b,'hasilnya=',hasil)

# OPERATOR MEMBERSHIP
print('\n===========IN')
nama = 'M. Faiz Ilyas'
test = 'iz'
cek = test in nama
print(test, 'terdapat di', nama,' adalah', cek)

test = 'zi'
cek = test in nama
print(test, 'terdapat di', nama,' adalah', cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama 
print(test1,'terdapat di',nama,'adalah',cek)

cek = test2 in nama 
print(test2,'terdapat di',nama,'adalah',cek)

cek = test3 in nama 
print(test3,'terdapat di',nama,'adalah',cek)

cek = test4 in nama 
print(test4,'terdapat di',nama,'adalah',cek)

cek = test5 in nama 
print(test5,'terdapat di',nama,'adalah',cek)

print('\n========== NOT IN')
# TUGAS LANJUTAN UNTUK NOT IN DENGAN CARA YANG SAMA

print('\n=========== NOT IN')
nama = 'M. Faiz Ilyas'
test = 'iz'
cek = test not in nama
print(test, 'terdapat di', nama,' adalah', cek)

test = 'zi'
cek = test not in nama
print(test, 'terdapat di', nama,' adalah', cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 not in nama 
print(test1,'terdapat di',nama,'adalah',cek)

cek = test2  not in nama 
print(test2,'terdapat di',nama,'adalah',cek)

cek = test3 not in nama 
print(test3,'terdapat di',nama,'adalah',cek)

cek = test4 not in nama 
print(test4,'terdapat di',nama,'adalah',cek)

cek = test5 not in nama 
print(test5,'terdapat di',nama,'adalah',cek)