def swap_all_up(nom):
    result =""
    for letter in nom:
        if letter == letter.lower():
            result += letter.upper()
        else:
            result += letter.upper()
    
    lista.append(result) 
     
def swap_all_down(nom):
    result =""
    for letter in nom:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.lower()
  
    lista.append(result) 
     
def swap_all_first(nom):

    lista.append(nom.title())
     
     
print("Ingrese una palabra")
nom = str(input())
lista = [nom]
swap_all_up(nom)
swap_all_down(nom)
swap_all_first(nom)
lista.append(len(nom))
print(lista)
