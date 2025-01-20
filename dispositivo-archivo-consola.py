import re
import datetime

# Solicitar al usuario la ruta del archivo de entrada
archivo_entrada = input("Ingresa la ruta del archivo de entrada: ")

# Intentar leer el archivo de entrada
try:
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        data = f.read()
except FileNotFoundError:
    print(f"El archivo {archivo_entrada} no se encuentra. Asegúrate de que la ruta sea correcta.")
    exit(1)

# Expresión regular para extraer los datos
pattern = r"(\d+)\s+.*\s+(\d{2}/\d{2}/\d{4}) (\d{2}):(\d{2}):\d{2} (a\. m\.|p\. m\.)\s+(\w+)\s+.*"

# Buscar las coincidencias
matches = re.findall(pattern, data)

# Función para convertir hora en formato de 24 horas
def convertir_hora(hora, minuto, periodo):
    hora, minuto = int(hora), int(minuto)
    if periodo == "a. m." and hora == 12:
        hora = 0  # Convertir 12 a 00
    elif periodo == "p. m." and hora != 12:
        hora += 12  # Convertir la hora PM a formato de 24 horas
    return f"{hora:02}:{minuto:02}"

# Acumular los resultados
result = []
for match in matches:
    cuenta, fecha, hora, minuto, periodo, tipo = match
    hora_convertida = convertir_hora(hora, minuto, periodo)
    result.append(f"{cuenta.zfill(5)}\t{tipo}\t{hora_convertida}")

# Obtener la fecha y hora actual para nombrar el archivo de salida
fecha_hora_actual = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
archivo_salida = f"resultados_{fecha_hora_actual}.txt"

# Escribir los resultados en el archivo de salida
with open(archivo_salida, 'w', encoding='utf-8') as f:
    f.write("\n".join(result))

print(f"Los resultados se han guardado en el archivo: {archivo_salida}")
