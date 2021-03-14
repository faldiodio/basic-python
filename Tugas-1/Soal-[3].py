nilai_praktek = int(input("masukan nilai praktek "))
nilai_teori =int(input("masukan nilai teori "))
if (nilai_praktek > 70) and (nilai_teori > 70):
    print("Selamat, Anda lulus!")
elif (nilai_praktek > 70) and (nilai_teori < 70):
    print("Anda harus mengulangi ujian teori")
elif (nilai_praktek < 70) and (nilai_teori > 70):
    print("Anda harus mengulangi ujian praktek ")
elif (nilai_praktek < 70) and (nilai_teori < 70):
    print("Anda harus mengulangi ujian teroi dan praktek")