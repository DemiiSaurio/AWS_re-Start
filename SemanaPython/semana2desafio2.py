print("digite una frase:")
frase = input()
print("digite una letra para buscarla en la frase:")
letra = input()
count = 0
for letter in frase:
    if letter == letra:
        count = count+1
    
print(f"la letra *{letra}* aparece {count} veces en la frase *{frase}*")
