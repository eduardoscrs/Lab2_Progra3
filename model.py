from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base

class VueloORM(Base):
    __tablename__ = "vuelos"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, index=True)
    origen = Column(String)
    destino = Column(String)
    prioridad = Column(String)

class Vuelo(BaseModel):
    codigo: str
    origen: str
    destino: str
    prioridad: str = "normal"

    class Config:
        orm_mode = True

class ReordenarRequest(BaseModel):
    nueva_lista: list[Vuelo]


### model.py (Estructura de datos)
class DoublyLinkedList:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def insertar_al_frente(self, vuelo):
        self._insert_between(vuelo, self._header, self._header._next)

    def insertar_al_final(self, vuelo):
        self._insert_between(vuelo, self._trailer._prev, self._trailer)

    def obtener_primero(self):
        if self.is_empty():
            raise Exception('La lista está vacía')
        return self._header._next._element

    def obtener_ultimo(self):
        if self.is_empty():
            raise Exception('La lista está vacía')
        return self._trailer._prev._element

    def longitud(self):
        return self._size

    def insertar_en_posicion(self, vuelo, posicion):
        if posicion < 0 or posicion > self._size:
            raise IndexError('Posición fuera de rango')
        current = self._header
        for _ in range(posicion):
            current = current._next
        self._insert_between(vuelo, current, current._next)

    def extraer_de_posicion(self, posicion):
        if posicion < 0 or posicion >= self._size:
            raise IndexError('Posición fuera de rango')
        current = self._header._next
        for _ in range(posicion):
            current = current._next
        return self._delete_node(current)

    def listar_vuelos(self):
        vuelos = []
        current = self._header._next
        while current != self._trailer:
            vuelos.append(current._element)
            current = current._next
        return vuelos

    def reordenar(self, nueva_lista):
        self.__init__()
        for vuelo in nueva_lista:
            self.insertar_al_final(vuelo)
