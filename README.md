# EVA2PCD
# Proyecto: Análisis de Impacto en Costos de Rutas Aéreas

Este proyecto tiene como objetivo analizar el impacto en los costos de las rutas aéreas utilizando técnicas de Machine Learning, incluyendo modelos supervisados y no supervisados.

## Estructura del proyecto
- `data/`: Dataset que se esta analizando.
- `notebooks/`: Notebooks con el análisis exploratorio, modelado, evaluación y optimización.
- `src/`: Código fuente modular con funciones de preprocesamiento, entrenamiento y evaluación.
- `models/`: Modelos entrenados serializados.
- `results/`: Métricas, gráficos y reportes.

## Configuración del Entorno (Dos opciones)

Requisito de sistema: Este proyecto requiere Python 3.10 o superior.
Elige **solo una** de las siguientes opciones para configurar tu entorno de trabajo:

### Opción A: Usando Conda (Recomendado para Ciencia de Datos)
Si tienes Anaconda o Miniconda instalado:
1. Crea el entorno: `conda create -n env_proy_ml python=3.10 -y`
2. Activa el entorno: `conda activate env_proy_ml`
3. Instala las dependencias: `pip install -r requirements.txt`

### Opción B: Usando Venv (Estándar de Python)
Si prefieres usar la herramienta nativa de Python:
1. Crea el entorno: `python -m venv venv`
2. Activa el entorno: 
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Instala las dependencias: `pip install -r requirements.txt`

---


