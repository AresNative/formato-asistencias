import re

# Ejemplo de datos
data = """
    Número    Nombre                     Tiempo                    Estado     Dispositivos   Tipo de Registro
14     Max 14                   14/12/2024 08:12:18 a. m.   Entrada   mayoreo      0               
123    Juan Perez               16/12/2024 08:06:17 a. m.   Entrada   mayoreo      0               
7      Empresa XYZ              16/12/2024 03:12:58 p. m.   Salida    mayoreo      0               
45678  Otro Nombre              17/12/2024 08:06:03 a. m.   Entrada   mayoreo      0               
9876   Mi Negocio               18/12/2024 07:56:05 a. m.   Entrada   mayoreo      0               
"""

# Expresión regular ajustada para capturar cuenta, hora y tipo dinámicamente
# Captura: número de cuenta, hora, minuto y tipo (Entrada/Salida)
pattern = r"^\s*(\d+)\s+.+?\s+\d{2}/\d{2}/\d{4}\s+(\d{2}):(\d{2}).*\s+(Entrada|Salida)"

# Buscar las coincidencias
matches = re.findall(pattern, data, re.MULTILINE)

# Acumular los resultados
result = []
for match in matches:
    cuenta, hora, minuto, tipo = match
    # Formatear la cuenta con ceros a la izquierda
    result.append(f"{cuenta.zfill(5)}\t{tipo}\t{hora}:{minuto}")

# Imprimir todo el resultado al final
print("\n".join(result))
