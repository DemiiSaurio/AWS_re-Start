print("Cantidad iniciar a invertir:")
inic = int(input())
print("% Interes Anual:%")
inter = int(input())
print("a cuantos años es la inversion?:")
year = int(input())

result = inic
for i in range(0 , year):
   actual = result
   interes = (actual*inter)/100
   result = (actual + interes)
   
print(f"{result}")