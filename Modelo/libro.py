class Libro:
    def __init__(self, isbn, titulo, id_autor, genero, anio, cantidad):
        self.isbn = isbn            # Código ISBN
        self.titulo = titulo        # Título del libro
        self.id_autor = id_autor    # ID del autor (clave foránea)
        self.genero = genero        # Género literario
        self.anio = anio            # Año de publicación
        self.cantidad = cantidad    # Cantidad disponible de este libro

    def __str__(self):
        return f"{self.titulo} (ISBN: {self.isbn}) - Autor ID: {self.id_autor} - Género: {self.genero}, Año: {self.anio}, Disponibles: {self.cantidad}"
