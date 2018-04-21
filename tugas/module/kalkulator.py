def kalkulator():
    print "--"*10
    a = input("masukan nilai a:")
    b = input("\masukan nilai b:")
    print ("-----------------------")
    print ("\n\t1.perkalian ")
    print ("\n\t2.pembagian ")
    print ("\n\t3.penjumlahan ")
    print ("\n\t4.pengurangan ")
    pilih = input("pilih operasi = ")
    if pilih == 1:
        a=a*b
        print (a)
    elif pilih == 2:
        a=a/b
        print (a)
    elif pilih == 3:
        a=a+b
        print (a)
    elif pilih == 4:
        a=a-b
        print (a)
    else:
        print "salah input"

