# Representación del laberinto
laberinto = {
    'Entrada': ['A', 'B'],
    'A': ['Entrada'],
    'B': ['C', 'D','Entrada'],
    'C': ['B','E'],
    'D': ['B','E'],
    'E': ['C','D','Salida'],
    'Salida': []
}

posicion_actual = "Entrada"

# Iniciamos el bucle del laberinto
while posicion_actual != "Salida":
    print(f"Estás en {posicion_actual}. Puedes moverte a: {', '.join(laberinto[posicion_actual])}") #join para que no aparezca el nomnbre del diccionario delante
    proximo_paso = input("¿A dónde quieres ir? ").strip() #strip para recibir texto
    
    # Verificamos si el próximo paso es válido
    if proximo_paso in laberinto[posicion_actual]:
        posicion_actual = proximo_paso
        print(f"Te has movido a {posicion_actual}")
    else:
        print("Movimiento no válido. Intenta de nuevo.")

# Mensaje final al llegar a la salida
print("¡Felicidades! Has encontrado la salida del laberinto.")