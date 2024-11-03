#Es un lugar donde solo entran hombres y caben 3 personas dentro, va gente poniendose a la cola y hay que ir quitándola 

from collections import deque #sin esto no funcionan las colas
import string
import random

def id_generator(size=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range (size))

cola = deque()
listagente = ["Mario", "Sergio", "Dani", "Carolina", "Hugo"]
aforo = 3
numerogentedentro = 0
gentedentro = deque()


for persona in listagente:
    if persona == "Carolina":
        print(f"{persona}, aqui solo entran hombres")
    else:
        cola.append(persona)
        print(cola)
    
#gente que va entrando
while numerogentedentro < aforo:
    entrando = cola.popleft()
    gentedentro.append(entrando)
    print ("Están dentro", " " .join(gentedentro), "están esperando" , " ".join(cola), f"están entrando {entrando}")
    numerogentedentro += 1

string_gentefuera = " , ".join(cola) # no funciona sin " " delante puede llevar lo que sea

print(f"Se ha quedado fuera {string_gentefuera}")

descuentopornoentrar = 10

descuentos = []

for personafuera in cola:
    codigodescuento = id_generator()
    descuento = {"nombre": personafuera, "código descuento": codigodescuento, "importe": descuentopornoentrar}
    descuentos.append(descuento)

print(descuentos)