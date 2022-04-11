print("Ingrese un numero positivo")
num = int(input())
cad = ""
for i in range(0, num):
    if(i%2 == 1):
        print(i)
        cad + ","
print(cad)