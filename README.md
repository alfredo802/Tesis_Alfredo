# Sistema de Pronóstico de Mareas con Deep Learning

Este proyecto implementa un sistema de pronóstico de mareas utilizando técnicas de deep learning, integrando datos históricos de mareas y presión atmosférica.

## Características

- Pronóstico de mareas usando deep learning
- Visualización de datos históricos y pronósticos
- Cálculo de errores y residuales
- Interfaz web interactiva
- Monitoreo de niveles críticos
- Actualización continua del modelo

## Requisitos

- Python 3.12.3
- Dependencias listadas en requirements.txt

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar la base de datos:
```bash
python manage.py migrate
```

4. Ejecutar el servidor:
```bash
python manage.py runserver
```

## Estructura del Proyecto

- `tide_forecast/`: Aplicación principal de Django
- `ml_model/`: Módulo de machine learning
- `data/`: Datos históricos de mareas y presión
- `templates/`: Plantillas HTML
- `static/`: Archivos estáticos (CSS, JS, imágenes)

## Uso

1. Acceder a http://localhost:8000
2. Ver pronósticos actuales
3. Consultar datos históricos
4. Monitorear niveles críticos 