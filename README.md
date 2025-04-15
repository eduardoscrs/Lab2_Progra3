#✈️🏢🏢 Lab 2 - Programación 3

## Gestión de Vuelos con Lista Doblemente-Enlazada, API REST y Base de Datos

### Contexto

Imagina que trabajas en la torre de control de un aeropuerto concurrido. Cada minuto llegan nuevos vuelos, algunos con emergencias médicas, otros con retrasos por el clima, y todos compitiendo por un espacio limitado en las pistas.

Los controladores aéreos necesitan:
1. Priorizar vuelos de emergencia (que deben saltar al frente de la lista).
2. Mantener el orden básico de los vuelos programados.
3. Organizar dinámicamente cuando hay retrasos o cancelaciones.
4. Consultar rápidamente qué vuelos están próximos a despegar.

> Las estructuras de datos simples como arrays o colas no son suficientes. Necesitamos algo más flexible: una **Lista Doblemente-Enlazada**.

---

### Objetivo General

Crear una **Lista Doblemente-Enlazada** para la gestión de vuelos con persistencia en base de datos (ORM con SQLAlchemy) y operaciones accesibles desde una **API REST** desarrollada con **FastAPI**.

---

### Objetivos de Aprendizaje

- Modelar un sistema de gestión de vuelos usando una estructura de datos avanzada.
- Integrar estructuras de datos con una base de datos relacional.
- Desarrollar una API REST con operaciones CRUD, incluyendo funcionalidades como **undo/redo**.

---

## Funcionalidades de la Lista Doblemente-Enlazada

Implementar los siguientes métodos:

- `insertar_al_frente(vuelo)` → Añade un vuelo al inicio de la lista (para emergencias).
- `insertar_al_final(vuelo)` → Añade un vuelo al final de la lista (vuelos regulares).
- `obtener_primero()` → Retorna (sin remover) el primer vuelo de la lista.
- `obtener_ultimo()` → Retorna (sin remover) el último vuelo de la lista.
- `longitud()` → Retorna el número total de vuelos en la lista.
- `insertar_en_posicion(vuelo, posicion)` → Inserta un vuelo en una posición específica.
- `extraer_de_posicion(posicion)` → Remueve y retorna el vuelo en la posición dada.

---

##  Endpoints Requeridos (API REST con FastAPI)

| Método | Ruta                    | Descripción                                                          |
|--------|-------------------------|----------------------------------------------------------------------|
| POST   | `/vuelos`               | Añade un vuelo al final (normal) o al frente (emergencia).          |
| POST   | `/vuelos/insertar`      | Inserta un vuelo en la posición específica.                         |
| GET    | `/vuelos/total`         | Retorna el total de los vuelos en cola.                             |
| GET    | `/vuelos/proximo`       | Retorna el primer vuelo sin remover.                                |
| GET    | `/vuelos/ultimo`        | Retorna el último vuelo sin remover.                                |
| GET    | `/vuelos/lista`         | Lista todos los vuelos en el orden actual.                          |
| DELETE | `/vuelos/extraer`       | Remueve un vuelo de la posición dada.                               |
| PATCH  | `/vuelos/reordenar`     | Reordena manualmente la cola (Ej: por retrasos, cambios de prioridad). |

---


### Ejecutar el Proyecto en Entorno Virtual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt