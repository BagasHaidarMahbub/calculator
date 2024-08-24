print("Calculator Python")
print("================")

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("=================")

#logic
def penjumlahan(x,y):
    return x+y

def pengurangan(x,y):
    return x-y

def perkalian(x,y):
    return x*y

def pembagian(x,y):
    return x/y
type = input("Silahkan Masukan Nomor Yang Kalian Pilih :")

if type in ('1', '2', '3', '4'):
    angka1 = float(input("angka pertama :"))
    angka2 = float(input("angka kedua :"))
    print("=================")
    if type == '1':
        print("jawabannya adalah :", penjumlahan(angka1, angka2))
    if type == '2':
        print("jawabannya adalah :", pengurangan(angka1, angka2))
    if type == '3':
        print("jawabannya adalah :", perkalian(angka1, angka2))
    if type == '4':
        print("jawabannya adalah :", pembagian(angka1, angka2))
    print("=================")