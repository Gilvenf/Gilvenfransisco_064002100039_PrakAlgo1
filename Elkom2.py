import math
a=input("masukan angka pertama: ")
p1 = a.split("#")
b=input("masukan angka kedua: ")
p2 = b.split("#") 
jarak = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1])**2) ) )
print("jarak antara", a,"dan", b,"adalah",jarak)
