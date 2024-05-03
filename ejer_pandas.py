import pandas as pd
import matplotlib.pyplot as plt

productos = [
    {"nombre": "Camiseta", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
    {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
    {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
    {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
    {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
    {"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
    {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
    {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
    {"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible": 25},
    {"nombre": "Calcetines", "precio": 10, "cantidad_disponible": 150},
    {"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
    {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
    {"nombre": "Pendientes", "precio": 15, "cantidad_disponible": 180},
    {"nombre": "Cinturón", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
    {"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
    {"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
    {"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
    {"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]


df = pd.DataFrame(data=productos)
# print(df)

# Cálculo del valor total del inventario para cada producto
def calculo_valor_producto():
    df['valor total por producto'] = df['precio'] * df['cantidad_disponible'] # Multiplicamos precio por producto y lo definimos en una nueva columna del dataframe
    return df # Retorno del nuevo dataframe


valor_total_por_producto = calculo_valor_producto() # Almacenamos la funcion de calculo en una variable
# print(valor_total_por_producto)

# Cálculo del valor total del inventario sumando el valor total de cada producto
def calculo_valor_total():
    valor_total = df["valor total por producto"].sum() # Sumamos el valor total por producto y lo almacenamos en una variable
    return valor_total # Retornamos

valor_total = calculo_valor_total()
# print(valor_total)

# Simular algunas ventas y actualizar la cantidad disponible de productos vendidos


def simulacion_ventas():
    ventas_simuladas = [ # Creamos una nueva lista de diccionarios con simulaciones de ventas de algunos productos
        {"nombre": "Chaqueta", "cantidad_vendida": 9},
        {"nombre": "Pantalón", "cantidad_vendida": 6},
        {"nombre": "Bolso", "cantidad_vendida": 10},
        {"nombre": "Sombrero", "cantidad_vendida": 12},
    ]
    for venta in ventas_simuladas: # Iteramos sobre la lista
        nombre_prod = venta['nombre']
        cant_vendida = venta["cantidad_vendida"]
        df.loc[df['nombre'] == nombre_prod, 'cantidad_disponible'] -= cant_vendida
    return df

simulacion = simulacion_ventas()
# print(simulacion) #Mostramos la cantidad restante de cada producto despues de la simulacion de ventas


def new_data_drame(): #Creamos nuevo DataFrame
    df = pd.DataFrame(simulacion, columns=['nombre', 'cantidad_disponible']) #Asignamos columnas
    return df #Retornamos nuevo DataFrame


nuevo_df = new_data_drame()
print(nuevo_df)



# varible x: nombre de los productos
# variable y: cantidad disponible
def grafico():
    fig, ax = plt.subplots()
    ax.plot(nuevo_df['nombre'], nuevo_df['cantidad_disponible'])
    plt.title('Cantidad de Productos Disponibles') # Agrega un titulo
    plt.xlabel('Productos')
    plt.ylabel('Cantidad Disponible')
    plt.show()
    
grafico()
    
