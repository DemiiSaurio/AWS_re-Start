print("Cantidad de payasos:")
payasos = int(input())
print("Cantidad de muñecas:")
munnecas = int(input())

pesoPayaso = payasos * 112
pesoMunneca = munnecas * 75
print(f"el peso total de los payasos es :{pesoPayaso} gramos")
print(f"el peso total de las muñecas es :{pesoMunneca} gramos")
print(f"en total el pedido tiene un peso de {pesoMunneca + pesoPayaso} gramos")