print("Hello World")
print("My Name is Zainal Fattah")
print("Enjoy!, Happy running my code")

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y
    
def modulus(x, y):
    return x % y

print("Pilih Operasi.")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Modulus")

choice = input("Masukan Pilihanmu (1/2/3/4/5) : ")

num1 = int(input("Masukan angka pertama : "))
num2 = int(input("Masukan angka kedua : "))

if choice == '1':
    print("Hasil => ",num1," + ",num2," = ", tambah(num1, num2))

elif choice == '2':
    print("Hasil => ",num1," - ",num2," = ", kurang(num1, num2))

elif choice == '3':
    print("Hasil => ",num1," * ",num2," = ", kali(num1, num2))

elif choice == '4':
    print("Hasil => ",num1," / ",num2," = ", bagi(num1, num2))

elif choice =='5':
    print("Hasil => ",num1," % ",num2,"=",modulus(num1, num2))

else:
    print("Invalid input")
