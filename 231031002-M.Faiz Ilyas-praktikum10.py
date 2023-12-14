#Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Program Utama
hasil = fibonacci(20)
print('Fibonacci(%d)=%d' % (20, hasil))

# Program Utama
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
hasil = fibonacci(20)
print('Fibonacci(%d)=%d' % (20, hasil))

# Program tugas

bilangan = int(input("Masukkan sebuah bilangan: "))
hasil_fibonacci = fibonacci(bilangan)

print(f"Fibonacci({bilangan}) = {hasil_fibonacci}")