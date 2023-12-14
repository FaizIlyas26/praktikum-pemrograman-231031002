import os,time
masuk_brankas = True
percobaan = 3
pw_lapis1 = "kilo 2"
pw_lapis2 = "faslah"
pw_lapis3 = "badminton"
while masuk_brankas: 
    print("Selamat datang di brankas dengan 3 lapis keamanan!\nSisa percobaan anda:", percobaan)
    lapis1 = input("masukkan sandi pada lapisan ketiga: ")
    if lapis1 == pw_lapis1.lower(): 
        os.system('cls')
        print("Selamat datang di lapisan ke 2")
        lapis2 = input("masukkan sandi pada lapisan kedua: ")
        if lapis2 == pw_lapis2.lower():
            os.system('cls')
            print("Selamat datang di lapisan ke 1")
            lapis3 = input("masukkan sandi pada lapisan pertama: ")
            if lapis3 == pw_lapis3.lower():
                os.system('cls')
                print("silahkan mengakses brankas :)")
                break
            else:
                percobaan -= 1 
                print("sandi yang anda masukkan salah!")
                time.sleep(0.9)
                os.system('cls')
                if percobaan > 0:
                    print("clue: aku adalah olahraga yang banyak diminati banyak orang")
                    time.sleep(2)
                    os.system('cls')
                elif percobaan == 0: 
                    print("Anda gagal memasukkan sandi brangkas yang benar, kamu akan di tangkap")
                    time.sleep(0.9)   
                    break
        else:
            percobaan -= 1 
            print("sandi yang anda masukkan salah!")
            time.sleep(0.9)
            os.system('cls')
            if percobaan > 0:
                print("clue: aku adalah seseorang yang tinggal di parepare")
                time.sleep(2)
                os.system('cls')
            elif percobaan == 0: 
                print("Anda gagal memasukkan sandi brangkas yang benar, kamu akan di tangkap")
                time.sleep(0.9)   
                break
    else: 
        percobaan -= 1 
        print("sandi yang anda masukkan salah!")
        time.sleep(0.9)
        os.system('cls')
        if percobaan > 0:
            print("clue: di tempat ini ada masjid al ihsan")
            time.sleep(2)
            os.system('cls')
        elif percobaan == 0: 
            print("Anda gagal memasukkan sandi brangkas yang benar, kamu akan ditangkap")
            time.sleep(0.9)   
            break