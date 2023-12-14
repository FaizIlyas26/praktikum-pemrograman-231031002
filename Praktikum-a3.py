print('praktikum-a3.py\n')

nama  = 'muhammad faiz ilyas'
nim   = '231031002'
meet  = 'praktikum 3'
prodi = 'sistem informasi'
email = 'muhammadfaizilyas750@gmail.com'
TTL   = 'parepare, 24 september 2005'
alamat= 'Jl. Jend. sudirman' 
asal  = 'parepare'
hobi  = 'badminton'
tinggi= '173cm' 

print('-------------------------------------------------')
print (nama.center(50).upper())
print (nim.center(50))
print('\n'*2)

print(meet.capitalize().rjust(50)) 
print(prodi.title().rjust(50))    
print(email.rjust(50)) 
print('-'*50)

Ttl = 'parepare'

print(f'''\thalo nama saya {nama} dengan nim {nim} dari prodi {prodi} ini adalah file {meet} Terima kasih\n''')



print(f'''Biodata saya
Nama\t :  {nama.title()}
nim\t : {nim}
prodi\t : {prodi.title()}
TTL\t : {TTL}
alamat\t : {alamat}
asal\t : {asal}
hobi\t : {hobi}
tinggi\t : {tinggi}cm
''')

stat = 'sir issac nevton'
up = stat.upper()
print(up)
up = up.split() #up menjadi list n item
print(up)
print(up[-1][0].join (up[0][-1])) #N SIR ISSAC
print('N SIR ISSAC')
print('F SIR ISSAC NEWTON')

print(up[2][0], up[0], up[1][2])
print('NEVTON S I')

print ()


stat2 = '&sir$ @issac# *nevton.'
up2 = stat2.upper()
print(up2)
up2 = up2.split()
print (up2)
print(up2[0][1:-1], up2[1][1:-1], up2[2][1:-1])
print(up2[0].strip('&$'), up2[1].strip('@#'), up2[2].strip('*.'))


print ('SIR ISSAC NEVTON')

# Tugas Praktikum 3

print('Tugas praktikum 3'. center (40))
nama = 'M. Faiz Ilyas'
nim = ' 231031002'
prodi = 'Sistem Informasi'
print (f'''biodata saya
nama\t = {nama.title ()}
nim\t = {nim}
prodi\t = {prodi.title()}\n\n ''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


str1 = 'duFort Frankel Von Neumann'
up = str1.upper().split(" ")
print(up[-1]," ".join(up[0:3]))
#output: NEUMANN DUFORT FRANKEL VON

str2 = 'duFort Frankel Von Neumann'
up2 = str2.upper().split(" ")
print(f'{up2[0][0]}{up2[1][0]}{up2[2][0]} {up2[3]}')
#output: DFV NEUMANN

str3 = 'duFort Frankel Von Neumann'
up3 = str3.upper().split(" ")
print(f'{up3[0]} {up3[1][0]}{up3[2][0]}{up3[3][0]}')
#output: DUFORT FVN

str4 = 'duFort Frankel Von Neumann'
up4 = str4.upper().split(" ")
print(f'{up4[3][0]} {str4[0:6]} {up4[1][0]}{up4[2][0]}')
#output: N duFort FV

str5 = 'duFort Frankel Von Neumann'
up5 = str5.lower().split(" ")
print(f'{up5[-1].upper()} {up5[0][0]} {up5[1][0]} {up5[2][0]}')
#output: NEUMANN d f v
str6 = 'duFort Frankel Von Neumann'
up5 = str6.upper().split(" ")
print(f'{up5[-1]} {up5[0][0]}{up5[1][0]}{up5[2][0]}')
#output: NEUMANN DFV

str7 = '@duFort Frankel Von Neumann$'
up7 = str7.split(" ")
print(f'{up7[0].strip("@")} {up7[1]} {up7[2]} {up7[3].upper().strip("$")}')
#output: duFort Frankel Von NEUMANN

str8 = '#duFort4Frankel4Von4Neumann$'
up8 = str8.split("4")
print(f'{up8[0].strip("#")} {up8[1]} {up8[2]} {up8[3].strip("$")}')
#output: duFort Frankel Von Neumann

str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
up9 = str9.split("@")
up92= up9[2].split("-") 
print(f'{up9[1]} {up92[1].strip("^*")} {up92[2].strip("(")} {up92[3].strip("($")}')
#output: duFort Frankel Von Neumann

str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
up10 = str10.split("1")
print(up10[0][1:-1].lower().replace('f','F'), up10[1][1:-1].title(), up10[2][1:-1].title(), up10[3][1:-1].title())
#output: duFort Frankel Von Neumann