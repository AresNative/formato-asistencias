import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import re

def process_file(file_path):
    try:
        # Leer el contenido del archivo
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()

        # Expresión regular para capturar los datos relevantes
        pattern = r"^\s*(\d+)\s+.+?\s+\d{2}/\d{2}/\d{4}\s+(\d{2}):(\d{2}).*\s+(Entrada|Salida)"
        matches = re.findall(pattern, data, re.MULTILINE)

        # Formatear los resultados
        result = []
        for match in matches:
            cuenta, hora, minuto, tipo = match
            result.append(f"{cuenta.zfill(5)}\t{tipo}\t{hora}:{minuto}")

        return "\n".join(result)

    except Exception as e:
        return f"Error al procesar el archivo: {e}"

def open_file():
    # Seleccionar archivo usando el cuadro de diálogo
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if not file_path:
        return

    # Procesar el archivo
    processed_data = process_file(file_path)

    # Mostrar el resultado en la vista previa
    preview_text.delete("1.0", tk.END)
    preview_text.insert(tk.END, processed_data)

    # Guardar el archivo procesado
    save_path = filedialog.asksaveasfilename(
        title="Guardar archivo",
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if save_path:
        with open(save_path, "w", encoding="utf-8") as output_file:
            output_file.write(processed_data)
        messagebox.showinfo("Guardado", f"Archivo guardado en: {save_path}")

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Procesador de Archivos")
root.geometry("600x400")

# Etiqueta de instrucciones
instructions = tk.Label(root, text="Arrastra un archivo de texto o haz clic en el botón para abrirlo.", wraplength=580, justify="center")
instructions.pack(pady=10)

# Botón para abrir archivo
open_button = tk.Button(root, text="Abrir archivo", command=open_file)
open_button.pack(pady=5)

# Vista previa del contenido procesado
preview_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=70)
preview_text.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
