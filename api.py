from fastapi import FastAPI, HTTPException
from model import DoublyLinkedList
from model import Vuelo, ReordenarRequest

app = FastAPI()
lista_vuelos = DoublyLinkedList()

@app.post("/vuelos")
def agregar_vuelo(vuelo: Vuelo, emergencia: bool = False):
    if emergencia:
        lista_vuelos.insertar_al_frente(vuelo)
    else:
        lista_vuelos.insertar_al_final(vuelo)
    return {"mensaje": "Vuelo agregado exitosamente"}

@app.post("/vuelos/insertar")
def insertar_vuelo(vuelo: Vuelo, posicion: int):
    try:
        lista_vuelos.insertar_en_posicion(vuelo, posicion)
        return {"mensaje": "Vuelo insertado exitosamente"}
    except IndexError:
        raise HTTPException(status_code=400, detail="Posición fuera de rango")

@app.get("/vuelos/total")
def total_vuelos():
    return {"total": lista_vuelos.longitud()}

@app.get("/vuelos/proximo")
def proximo_vuelo():
    try:
        return lista_vuelos.obtener_primero()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/vuelos/ultimo")
def ultimo_vuelo():
    try:
        return lista_vuelos.obtener_ultimo()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/vuelos/lista")
def listar_vuelos():
    return lista_vuelos.listar_vuelos()

@app.delete("/vuelos/extraer")
def extraer_vuelo(posicion: int):
    try:
        vuelo = lista_vuelos.extraer_de_posicion(posicion)
        return {"mensaje": "Vuelo extraído exitosamente", "vuelo": vuelo}
    except IndexError:
        raise HTTPException(status_code=400, detail="Posición fuera de rango")

@app.patch("/vuelos/reordenar")
def reordenar_vuelos(request: ReordenarRequest):
    lista_vuelos.reordenar(request.nueva_lista)
    return {"mensaje": "Lista de vuelos reordenada exitosamente"}