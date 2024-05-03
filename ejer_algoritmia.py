
palabra = str(input('Ingrese una plabra: '))

def capitalizar_palabra(palabra):
    if palabra == '':
         return 'Debe ingresar una palabra'
    else:
        return palabra.capitalize()
    
print(capitalizar_palabra(palabra))
       