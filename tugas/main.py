from module.penilaian import nilai_mahasiswa
from module.pembayaran import pembayaran
from module.kalkulator import kalkulator

import getpass
useername = 'ryanes'
pasword = 'ryanes07'

def menu():
    print("===================================================")
    print("\n\t---pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")
    print("\t3. kalkulator")
   
    pilih = input("\n\tsilakan pilih : ")
    if pilih == 1:
        print(nilai_mahasiswa())
    elif pilih == 2 :
        print(pembayaran())
    elif pilih == 3 :
        print(kalkulator())
    else:
        exit
    tanya()
    
def tanya():
    tanya = raw_input("\nKembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input...........!!!")

username = raw_input("\nUsername : ")
password = getpass._raw_input("\nPassword : ")

if username == "ryanes" and password == "ryanes07":
    menu()
    
else:
    print ("password atau username mu salah.........!!!")
