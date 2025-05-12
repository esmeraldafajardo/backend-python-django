## 🚀 Descripción General
 La aplicación está construida con **Django**, **SQLite**, **Django REST Framework** y utiliza una función adicional de **Inteligencia Artificial simulada**. Permite gestionar empresas, productos, inventario, usuarios con roles, generar archivos PDF y enviar correos.

---

## 📂 Tecnologías Usadas

- Python 3.6
- Django 3+
- Django REST Framework
- SQLite (como base de datos local)
- ReportLab (generación de PDF)
- Django email (consola como backend de pruebas)
- Postman (para testeo de endpoints)

---

## ⚖️ Requisitos de Instalación

1. Tener Python 3.6 instalado
2. Clonar el proyecto o copiar los archivos
3. Crear y activar un entorno virtual:

```bash
python3 -m venv env
source env/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

(Si no existe un `requirements.txt`, instalar manualmente):
```bash
pip install django djangorestframework reportlab
```

5. Migrar la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crear un superusuario:
```bash
python manage.py createsuperuser
```

7. Iniciar el servidor:
```bash
python manage.py runserver
```

---

## 👤 Autenticación y Usuarios

El sistema utiliza un modelo de usuario personalizado `CustomUser` con dos roles:
- `admin`: puede acceder al panel `/admin`, registrar y editar empresas, productos e inventario.
- `externo`: solo puede visualizar empresas y productos (vía API).

**Login API:**
```
POST /api/login/
```
Body:
```json
{
  "username": "usuario",
  "password": "contraseña"
}
```
Respuesta:
```json
{
  "message": "Bienvenido usuario",
  "rol": "admin"
}
```

---

## 📚 Funcionalidades por Módulo

### 1. Empresas
- URL admin: `/admin/empresas/`
- API: `GET /api/empresas/`

### 2. Productos
- Asociados a empresas
- API: `GET /api/productos/`

### 3. Inventario
- Asocia productos a empresas con cantidad.
- PDF: `GET /api/inventario/pdf/`
- Enviar correo: `GET /api/inventario/enviar/`

**Importante**: En `settings.py` debe estar:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
Esto imprime el correo en la consola.

### 4. IA: Generar descripción de producto
- API: `POST /api/generar-descripcion/`

Body:
```json
{
  "nombre": "Laptop Gamer",
  "caracteristicas": "Intel i9, 32GB RAM, RTX 4080"
}
```
Respuesta:
```json
{
  "descripcion_generada": "El producto 'Laptop Gamer' destaca por sus características..."
}
```

---

## ⚙️ Configuraciones Personalizadas

- `AUTH_USER_MODEL = 'users.CustomUser'` en `settings.py`
- Registro de modelos `Empresa`, `Producto`, `Inventario`, y `CustomUser` en `admin.py`
- Formulario personalizado para `CustomUser` para incluir campo `rol`
- Uso de SQLite para evitar problemas con PostgreSQL en desarrollo

---

## 🔧 Endpoints Importantes

| Recurso                | Método | Endpoint                          |
|------------------------|--------|-----------------------------------|
| Login                  | POST   | `/api/login/`                     |
| Empresas               | GET    | `/api/empresas/`                  |
| Productos              | GET    | `/api/productos/`                 |
| Generar descripción   | POST   | `/api/generar-descripcion/`       |
| PDF Inventario         | GET    | `/api/inventario/pdf/`            |
| Enviar PDF por correo  | GET    | `/api/inventario/enviar/`         |

---

## 🚫 Notas

- Este proyecto está desarrollado para propósitos de prueba. Algunas funcionalidades están simuladas (IA, correo).
- Para integración real de correo puedes usar SMTP real (ej. Gmail o SendGrid).
- IA puede integrarse con OpenAI si se dispone de clave de API.

---

## 🚀 Autora
**Dalia Diaz**  
Prueba Técnica Full Stack 2025 - Lite Thinking
# backend-python-django
# backend-python-django
