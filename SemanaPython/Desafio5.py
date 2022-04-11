print("Ingrese numero su peso en KG:")
kg = int(input())
print("Ingrese su altura en metros:")
met = float(input())
res = (kg/met)*100 
print(f"Su IMC es :{round(res, 2)}%")