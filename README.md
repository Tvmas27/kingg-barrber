# 💈 King Barber - Sistema de Reservas

Aplicación web moderna para la gestión de citas de una barbería, desarrollada con Django y Firebase. Este proyecto implementa una arquitectura segura y escalable, desplegada en producción.

## Demo en Vivo
**URL Pública:** https://kiing-barber-fa8e396666b6.herokuapp.com/
*(Ejemplo: https://sheltered-anchorage-42930-18a3a2c1d124.herokuapp.com/)*

## Características Principales
*   **Reserva de Horas:** Formulario público para clientes que consume la API interna.
*   **Panel de Administración (Dashboard):**
    *   Acceso seguro con autenticación.
    *   Visualización de métricas y gráficos (Chart.js).
    *   Tabla de reservas con opción de **Cancelar**.
    *   **Exportación de datos a CSV**.
*   **API RESTful:** Endpoints documentados y protegidos con **JWT (JSON Web Tokens)**.
*   **Cliente Híbrido:** Incluye un script `client.py` que funciona como cliente de consola (CLI) para reservar o administrar.
*   **Seguridad:** 
    *   Variables de entorno para credenciales sensibles.
    *   Reglas de seguridad en Firebase Firestore.
    *   Validación de disponibilidad de horarios en el backend.

## Tecnologías Utilizadas
*   **Backend:** Python 3.13, Django 5.2, Django REST Framework.
*   **Base de Datos:** Google Firebase Firestore (NoSQL).
*   **Frontend:** HTML5, Tailwind CSS (CDN), JavaScript Vanilla.
*   **Despliegue:** Heroku (Gunicorn + WhiteNoise).
*   **Librerías Clave:** `firebase-admin`, `djangorestframework-simplejwt`, `python-dotenv`, `gunicorn`.

## Configuración Local

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Tvmas27/King-Barber.git
    cd King-Barber
    ```

2.  **Crear entorno virtual e instalar dependencias:**
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

3.  **Configurar Variables de Entorno:**
    Crea un archivo `.env` en la carpeta `King_Barber/` (junto a `settings.py`) con:
    ```env
    DEBUG=True
    SECRET_KEY=tu_clave_secreta_local
    ALLOWED_HOSTS=127.0.0.1,localhost
    FIREBASE_CREDENTIALS=ruta/a/tu/serviceAccountKey.json
    ```

4.  **Ejecutar el servidor:**
    ```bash
    cd King_Barber
    python manage.py runserver
    ```

## 🔌 Documentación de la API

| Método | Endpoint | Descripción | Auth Requerida |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/token/` | Obtener Token de Acceso (Login) | ❌ No |
| `POST` | `/api/reservas/crear/` | Crear nueva reserva (Valida horario) | ❌ No |
| `GET` | `/api/reservas/` | Listar todas las reservas (JSON) | ✅ Sí (JWT) |
| `GET` | `/api/reservas/exportar/` | Descargar reporte en CSV | ✅ Sí (JWT) |
| `DELETE` | `/api/reservas/<id>/` | Cancelar/Eliminar una reserva | ✅ Sí (JWT) |

## Cliente Python (CLI)
El proyecto incluye un cliente de terminal para demostrar la versatilidad de la API.
```bash
python client.py
```
*   **Opción 1:** Simula ser un cliente reservando una hora.
*   **Opción 2:** Simula ser el administrador consultando datos.

## Despliegue (Heroku)
El proyecto está configurado para despliegue continuo.
*   **Procfile:** Define el servidor Gunicorn.
*   **Config Vars:** Las credenciales de Firebase se inyectan vía variable de entorno `FIREBASE_CREDENTIALS` (JSON string) para mayor seguridad.

---
**Evaluación 3 - Programación Backend**
**Desarrollado por:** [Tu Nombre]

