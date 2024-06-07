# Visualización de Complejidad de Algoritmos

Este proyecto visualiza la complejidad temporal de varios algoritmos usando Python y Matplotlib.

## Algoritmos Implementados

- **O(1) - Constante**: Acceso a un elemento en una lista
- **O(log n) - Logarítmica**: Búsqueda binaria
- **O(n) - Lineal**: Búsqueda lineal
- **O(n log n) - Linealítmica**: Ordenamiento por mezcla (Merge sort)
- **O(n^2) - Cuadrática**: Ordenamiento de burbuja (Bubble sort)
- **O(2^n) - Exponencial**: Fibonacci recursivo

## Requisitos

- Python 3.x
- Matplotlib

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/Algorithm-Complexity-Visualization.git
    cd Algorithm-Complexity-Visualization
    ```

2. Crea y activa un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala el paquete requerido:

    ```bash
    pip install matplotlib
    ```

## Uso

Ejecuta el script para generar la gráfica de complejidad:

```bash
python complexity_graph.py
