print('tugas-praktikum4.py')
print()

pendapatan=  int(input('masukkan pendapatan:' ))
if pendapatan <=1000: 
    presentase= 0
elif pendapatan <= 2000:
    presentase= 10
elif pendapatan <= 3000:
    presentase= 20
elif pendapatan <= 4000:
    presentase= 30
elif pendapatan <= 5000:
    presentase= 40
else:
    pendapatan = 50
    
bonus = pendapatan*(presentase/100)
total = pendapatan+bonus

print('pendapatan:',pendapatan)
print(f'presentase ,{float(presentase)}%')
print('bonus',bonus)
print('total',total)
    
    
