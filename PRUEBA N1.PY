"""
Acertijo del bote: persona, zorro, oveja y lechuga.

Problema de la vida cotidiana: una persona debe cruzar un rio con un zorro,
una oveja y una lechuga. El bote solo puede llevar a la persona y UN pasajero.

Reglas:
  - Si la persona no esta, el zorro se come a la oveja.
  - Si la persona no esta, la oveja se come la lechuga.

El programa usa BFS (busqueda en anchura) para encontrar la solucion
con el menor numero de viajes.
"""

from collections import deque

# Nombres de los elementos
PERSONA = "persona"
ZORRO = "zorro"
OVEJA = "oveja"
LECHUGA = "lechuga"

TODOS = {PERSONA, ZORRO, OVEJA, LECHUGA}


def es_seguro(orilla):
    """Devuelve True si en esa orilla no se come nadie."""
    if PERSONA in orilla:
        return True  # con la persona presente, todo esta seguro
    if ZORRO in orilla and OVEJA in orilla:
        return False  # el zorro se come a la oveja
    if OVEJA in orilla and LECHUGA in orilla:
        return False  # la oveja se come la lechuga
    return True


def estado_valido(izquierda):
    """Un estado es valido si ambas orillas son seguras."""
    derecha = TODOS - izquierda
    return es_seguro(izquierda) and es_seguro(derecha)


def vecinos(izquierda):
    """Genera los estados posibles tras un viaje del bote."""
    derecha = TODOS - izquierda
    # La persona rema desde la orilla donde se encuentra
    if PERSONA in izquierda:
        origen, direccion = izquierda, "derecha"
    else:
        origen, direccion = derecha, "izquierda"

    # Puede ir sola o con un pasajero que este en su misma orilla
    pasajeros = [None] + [x for x in origen if x != PERSONA]

    for pasajero in pasajeros:
        moviendo = {PERSONA} if pasajero is None else {PERSONA, pasajero}
        if direccion == "derecha":
            nueva_izq = izquierda - moviendo
        else:
            nueva_izq = izquierda | moviendo
        if estado_valido(nueva_izq):
            yield frozenset(nueva_izq), pasajero, direccion


def resolver():
    """BFS desde 'todos en la izquierda' hasta 'todos en la derecha'."""
    inicio = frozenset(TODOS)
    meta = frozenset()  # nadie queda en la izquierda
    cola = deque([(inicio, [])])
    visitados = {inicio}

    while cola:
        estado, camino = cola.popleft()
        if estado == meta:
            return camino
        for nuevo, pasajero, direccion in vecinos(estado):
            if nuevo not in visitados:
                visitados.add(nuevo)
                cola.append((nuevo, camino + [(pasajero, direccion, nuevo)]))
    return None


def mostrar_orillas(izquierda):
    derecha = TODOS - izquierda
    izq = ", ".join(sorted(izquierda)) or "(vacia)"
    der = ", ".join(sorted(derecha)) or "(vacia)"
    print(f"   Orilla izquierda: {izq}")
    print(f"   Orilla derecha  : {der}")


def main():
    print("=== ACERTIJO DEL BOTE ===")
    print("Estado inicial:")
    mostrar_orillas(frozenset(TODOS))
    print()

    solucion = resolver()
    if solucion is None:
        print("No hay solucion.")
        return

    for i, (pasajero, direccion, estado) in enumerate(solucion, start=1):
        if pasajero is None:
            print(f"Viaje {i}: la persona cruza sola hacia la {direccion}.")
        else:
            print(f"Viaje {i}: la persona lleva a '{pasajero}' hacia la {direccion}.")
        mostrar_orillas(estado)
        print()

    print(f"Resuelto en {len(solucion)} viajes.")


if __name__ == "__main__":
    main()