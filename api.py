from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from model import Vuelo, VueloORM, ReordenarRequest
from model import DoublyLinkedList

# Crear tablas
from database import Base
Base.metadata.create_all(bind=engine)

app = FastAPI()
lista_vuelos = DoublyLinkedList()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/vuelos")
def agregar_vuelo(vuelo: Vuelo, emergencia: bool = False, db: Session = Depends(get_db)):
    vuelo_db = VueloORM(**vuelo.dict())
    db.add(vuelo_db)
    db.commit()
    db.refresh(vuelo_db)

    if emergencia:
        lista_vuelos.insertar_al_frente(vuelo.dict())
    else:
        lista_vuelos.insertar_al_final(vuelo.dict())

    return {"mensaje": "Vuelo agregado exitosamente", "vuelo": vuelo_db}

@app.post("/vuelos/insertar")
def insertar_vuelo(vuelo: Vuelo, posicion: int, db: Session = Depends(get_db)):
    try:
        lista_vuelos.insertar_en_posicion(vuelo.dict(), posicion)
        vuelo_db = VueloORM(**vuelo.dict())
        db.add(vuelo_db)
        db.commit()
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
    lista_vuelos.reordenar([vuelo.dict() for vuelo in request.nueva_lista])
    return {"mensaje": "Lista de vuelos reordenada exitosamente"}
