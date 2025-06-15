# Tarea 2 - Taller de Redes y Servicios

Este proyecto demuestra la creación de un entorno cliente-servidor utilizando **Docker** y **Nginx** para servir contenido web básico mediante el protocolo **HTTP**. La solución consiste en dos contenedores: uno que actúa como servidor web (usando Nginx) y otro que actúa como cliente (utilizando `curl` para hacer peticiones HTTP).

---

## 📁 Estructura del Proyecto

├── servidor/
│ ├── Dockerfile-s # Imagen del servidor Nginx
│ ├── default.conf # Configuración del servidor Nginx
│ └── index.html # Página HTML servida
├── cliente/
│ ├── Dockerfile-c # Imagen del cliente que realiza una petición HTTP

---

## 🚀 Instalación y Ejecución

### 1. Crear una red de Docker

```bash
sudo docker network create red-tarea

2. Construir imagen del servidor
cd servidor
sudo docker build -f Dockerfile-s -t servidor .

3. Ejecutar contenedor del servidor
sudo docker run -d --name servidorN --network red-tarea -p 8080:80 servidor

4. Construir imagen del cliente
cd cliente
sudo docker build -f Dockerfile-c -t cliente-img .

5. Ejecutar contenedor del cliente
sudo docker run --rm --network red-tarea cliente-img

🌐 ¿Qué hace cada componente?
Servidor: Utiliza Nginx para servir un archivo index.html desde la ruta /usr/share/nginx/html, con configuración personalizada en default.conf.

Cliente: Ejecuta un comando curl http://servidor:80 para realizar una petición HTTP al contenedor del servidor.
📦 Tecnologías utilizadas
Docker

Nginx

curl

🧪 Resultado Esperado
Al ejecutar el cliente, deberías ver en consola:
<h1>Hola desde el servidor Nginx</h1>
Y en herramientas de análisis como Wireshark, podrás observar paquetes con códigos de estado HTTP como 200 OK.

👨‍💻 Autores
Cristóbal Collado

Fernando Ortega

📄 Licencia
Este proyecto es solo con fines educativos y no incluye una licencia explícita.
