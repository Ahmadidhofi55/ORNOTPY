import random
welcome_message = 'WELCOME TO ORNOTPY GAMES!'
ornot_position = random.randint(1,4)

print('*******************************')
print('** '+ welcome_message + ' **')
print('*******************************')

nama = input('masukkan nama anda:')

print(f'''
Halo {nama}! coba perhatikan gambar dibawah ini
[-] [-] [-] [-]
''')
#input = string
#cek type data print(type(usia))
jawaban_user =  int(input("Menurut Kamu di goa nomor berapa ORNOTPY berada? [1 / 2 / 3 / 4] : "))
konfirmasi = input(f'Anda memasukkan {jawaban_user} Apakah anda yakin [y/n]')

if konfirmasi.lower() == 'y' :
   if jawaban_user == ornot_position:
    print(f'selamat {nama} kamu menang ornotpy di {ornot_position}')
   else:
    print(f'maaf anda kalah ornotpy di {ornot_position} pilihan kamu {jawaban_user}') 
else:
    jawaban_konfirmasi =  int(input("Masukkan Jawaban anda kembali! [1 / 2 / 3 / 4] : "))
    if jawaban_user == ornot_position:
     print(f'selamat {nama} kamu menang ornotpy di {ornot_position}')
    else:
     print(f'maaf anda kalah ornotpy di {ornot_position} pilihan kamu {jawaban_user}') 
#print(f"pilihan kamu adalah : {jawaban_user}")

   

