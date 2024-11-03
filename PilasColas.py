from collections import deque #sin esto no funcionan las colas

#ejercicio de listas

pila = []
pila.append ("Don Quijote")
pila.append ("EL Principito")
pila.append ("Dune")
print(pila)

pila.pop ()
pila.pop ()
print(pila)

#ejercicio de Colas

cola = deque()
cola.append("Mario")
print(cola)
cola.append("Sergio")
print(cola)
cola.append("Dani")
print(cola)
cola.append("Carolina")
print(cola)
cola.append("Hugo")
print(cola)

cola.popleft()
cola.popleft()
cola.popleft()
print(cola)


