# Tarea 3 - Taller de Redes: Cliente, Servidor y Fuzzing de Tráfico

Este proyecto demuestra cómo levantar dos contenedores Docker (cliente y servidor), permitir la comunicación entre ellos y realizar fuzzing o modificaciones al tráfico con herramientas personalizadas.

---

## 📦 Estructura del Repositorio

├── Dockerfile-c # Dockerfile del cliente
├── Dockerfile-s # Dockerfile del servidor
├── default.conf # Configuración del servidor (Nginx)
├── index.html # Página HTML servida
├── fuzzing_injection.py # Script de fuzzing/inyección
├── modificacion.py # Script de modificación de tráfico
├── README.md # Este archivo

---

## 🐳 Paso 1: Crear los contenedores Docker

### 1.1. Construir la imagen del servidor

```bash
docker build -t servidor-img -f Dockerfile-s .

1.2. Construir la imagen del cliente
docker build -t cliente-img -f Dockerfile-c .

🔗 Paso 2: Crear red Docker para conectar los contenedores
docker network create red-local

🚀 Paso 3: Levantar los contenedores
3.1. Contenedor del servidor
docker run -d --name servidor --network red-local servidor-img

3.2. Contenedor del cliente
docker run -it --name cliente --network red-local cliente-img

🧪 Paso 4: Realizar fuzzing o modificar el tráfico
Opción 1: Fuzzing con fuzzing_injection.py
Este script permite realizar pruebas de fuzzing simulando ataques o entradas maliciosas:
python3 fuzzing_injection.py

Opción 2: Modificar tráfico con modificacion.py
Este script puede interceptar y alterar el tráfico antes de enviarlo al servidor (por ejemplo, para simular manipulaciones del cliente):
python3 modificacion.py

Nota: Asegúrate de que los scripts estén configurados para apuntar al nombre de host servidor dentro de la red Docker (red-local).


