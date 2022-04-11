
def swap_all_up(nom):
    result =""
    for letter in nom:
        if letter == letter.lower():
            result += letter.upper()
        else:
            result += letter.upper()
    print("Mayuscula")
    print(result) 
     
def swap_all_down(nom):
    result =""
    for letter in nom:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.lower()
    print("minuscula:")
    print(result) 
     
def swap_all_first(nom):
    print("Primera Mayuscula")
    print(nom.title())
     
     
print("Ingrese su nombre completo:")
nom = str(input())

swap_all_up(nom)
swap_all_down(nom)
swap_all_first(nom)

