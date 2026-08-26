berat = int(input("masukan berat anda(kg):" ))
tinggi = int(input("masukan tinggi badan anda (m) :"))
bmi = berat/ tinggi ** 2

print ("Berat badan :", berat"kg")
print ("Tinggi badan : ", tinggi)

if bmi < 18,5:
    print("keterangan : berat badan kurang")
elif bmi <25:
    print("keterangan : berat badan normal")
elif bmi <30:
    priny("keterangan : berat badan berlebih")
else:
    print("keterangan : obesitas")
