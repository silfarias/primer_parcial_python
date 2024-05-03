
palabra = str(input('Ingrese una plabra: '))

def capitalizar_palabra(palabra):
    if palabra == '' or type(palabra) is not str :
         return 'Debe ingresar una palabra'
    else:
        return palabra.capitalize()
    
print(capitalizar_palabra(palabra))
       