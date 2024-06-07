import time
import matplotlib.pyplot as plt

# Algoritmos
def constant_algo(n):
    arr = list(range(n))
    return arr[0]

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def logarithmic_algo(n):
    arr = list(range(n))
    return binary_search(arr, n-1)

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def linear_algo(n):
    arr = list(range(n))
    return linear_search(arr, n-1)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def n_log_n_algo(n):
    arr = list(range(n, 0, -1))
    merge_sort(arr)
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quadratic_algo(n):
    arr = list(range(n, 0, -1))
    bubble_sort(arr)
    return arr

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def exponential_algo(n):
    return fibonacci(n)

# Medir tiempos de ejecución
sizes = [10, 50, 100, 200, 300, 400, 500]
times_constant = []
times_logarithmic = []
times_linear = []
times_n_log_n = []
times_quadratic = []
times_exponential = []

for n in sizes:
    start = time.time()
    constant_algo(n)
    times_constant.append(time.time() - start)

    start = time.time()
    logarithmic_algo(n)
    times_logarithmic.append(time.time() - start)

    start = time.time()
    linear_algo(n)
    times_linear.append(time.time() - start)

    start = time.time()
    n_log_n_algo(n)
    times_n_log_n.append(time.time() - start)

    start = time.time()
    quadratic_algo(n)
    times_quadratic.append(time.time() - start)

    if n <= 30:  # Limitar el cálculo para O(2^n) debido a la alta complejidad
        start = time.time()
        exponential_algo(n)
        times_exponential.append(time.time() - start)
    else:
        times_exponential.append(None)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(sizes, times_constant, label='O(1)')
plt.plot(sizes, times_logarithmic, label='O(log n)')
plt.plot(sizes, times_linear, label='O(n)')
plt.plot(sizes, times_n_log_n, label='O(n log n)')
plt.plot(sizes, times_quadratic, label='O(n^2)')
plt.plot(sizes[:len(times_exponential)], times_exponential, label='O(2^n)')

plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Comparación de Complejidades de Algoritmos')
plt.legend()
plt.grid(True)
plt.show()
