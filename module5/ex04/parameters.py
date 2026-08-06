import sys

# Filtrar sys.argv para excluir el nombre del script (índice 0)
parametros = sys.argv[1:]
numero = len(parametros)

# Mostrar la lista de parámetros recibidos
print(f"Lista de parámetros recibidos: {parametros}")
print(f"Número de parámetros recibidos: {numero}")

# Salto de línea explícito (adicional al que ya incluye print)
print()