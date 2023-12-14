pw_benar = "faslah"
percobaan = 3 
a = True
while a:
    masukan = input('masukkan password: ')
    if masukan == pw_benar:
        print('selamat kamu berhasil')
        a = False
    else:
        if percobaan == 0:
            print ('cieee di banned')
            a = False
        else:
            print('password yang anda masukkan salah, coba lagi')
            percobaan -= 1
        
        
    