def busqueda_binaria(animes, objetivo):
    primero = 0
    ultimo = len(animes) - 1
    
    while primero <= ultimo:
        medio = (primero + ultimo) // 2
        anime_actual = animes[medio][0]  # Extraemos el nombre del anime
        
        if anime_actual == objetivo:
            return animes[medio]
        elif anime_actual < objetivo:
            primero = medio + 1
        else:
            ultimo = medio - 1
    
    return None

# Ejemplo de uso
base_de_datos = [
    ("One Piece", "A"),
    ("Attack on Titan", "A+"),
    ("Naruto", "B"),
    ("My Hero Academia", "A"),
    ("Demon Slayer", "A+"),
    ("One Punch Man", "A-"),
    ("Fullmetal Alchemist", "A")
]

anime_buscado = "Naruto"
resultado = busqueda_binaria(base_de_datos, anime_buscado)

if resultado:
    nombre, clasificacion = resultado
    print(f"El anime '{nombre}' tiene clasificación '{clasificacion}'.")
else:
    print("El anime no fue encontrado en la base de datos.")
