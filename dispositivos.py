import re

# Ejemplo de datos
data = """ 
úmero	Nombre                  	Tiempo                   	Estado 	Dispositivos	Tipo de Registro
14    	Max 14                  	14/12/2024 08:12:18 a. m.	Entrada	mayoreo     	0               
14    	Max 14                  	14/12/2024 03:10:50 p. m.	Salida 	mayoreo     	0               
14    	Max 14                  	16/12/2024 08:06:17 a. m.	Entrada	mayoreo     	0               
14    	Max 14                  	16/12/2024 03:12:58 p. m.	Salida 	mayoreo     	0               
14    	Max 14                  	17/12/2024 08:06:03 a. m.	Entrada	mayoreo     	0               
14    	Max 14                  	17/12/2024 03:30:15 p. m.	Salida 	mayoreo     	0               
14    	Max 14                  	18/12/2024 07:56:05 a. m.	Entrada	mayoreo     	0               
14    	Max 14                  	18/12/2024 03:21:29 p. m.	Salida 	mayoreo     	0               
14    	Max 14                  	18/12/2024 03:43:59 p. m.	Entrada	mayoreo     	0   
"""

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

# Imprimir todo el resultado al final
print("\n".join(result))
