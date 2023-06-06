import tkinter as tk

def buscar_palabra():
    palabra = entry.get()
    if palabra in diccionario:
        result_text.set("La palabra '{}' se encontró en el diccionario.".format(palabra))
    else:
        result_text.set("La palabra '{}' no se encontró en el diccionario.".format(palabra))

# Crea el diccionario
diccionario = {'hola': 1, 'adios': 2, 'mundo': 3, 'chao': 4}

# Crear la ventana principal
window = tk.Tk()
window.title('Búsqueda de palabras')

# Crear la etiqueta y campo de entrada
label = tk.Label(window, text = 'Ingrese una palabra:')
label.pack()
entry = tk.Entry(window)
entry.pack()

# Crear botón de búsqueda
search_button = tk.Button(window, text = 'Buscar', command = buscar_palabra)
search_button.pack()

# Crear etiqueta de resultado
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable = result_text)
result_label.pack()

# Ejecutar la aplicación
window.mainloop()