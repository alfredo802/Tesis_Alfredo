# Sistema de Pronóstico de Mareas

Este sistema permite realizar pronósticos de mareas utilizando datos históricos y técnicas de aprendizaje automático.

## Requisitos

- Python 3.8 o superior
- Las dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio
2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar el sistema de pronóstico:

```bash
python tide_forecast.py
```

El sistema:
1. Generará datos de muestra para demostración
2. Entrenará un modelo con los datos históricos
3. Realizará un pronóstico para las próximas 24 horas
4. Mostrará una gráfica con los datos históricos y el pronóstico
5. Imprimirá una tabla con las predicciones

## Notas

- Este es un sistema de demostración que utiliza datos simulados
- Para uso en producción, se recomienda:
  - Integrar datos reales de mareas
  - Ajustar los parámetros del modelo según la ubicación
  - Considerar factores adicionales como la luna, el viento, etc. 