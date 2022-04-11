def swap_all_up(nom):
    result =""
    for letter in nom:
        if letter == letter.lower():
            result += letter.upper()
        else:
            result += letter.upper()
    
    print(result) 
     
def swap_all_down(nom):
    result =""
    for letter in nom:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.lower()
  
    print(result) 
     
def swap_all_first(nom):

    print(nom.title())
     
     
print("Ingrese una palabra:")
nom = str(input())
for i in range(0, 3):
    print(i+1)
    swap_all_up(nom)
    swap_all_down(nom)
    swap_all_first(nom)
