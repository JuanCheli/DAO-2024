class Libro:
    def __init__(self, isbn, titulo, id_autor, genero, anio, cantidad):
        self.isbn = isbn            # Código ISBN
        self.titulo = titulo        # Título del libro
        self.id_autor = id_autor    # ID del autor (clave foránea)
        self.genero = genero        # Género literario
        self.anio = anio            # Año de publicación
        self.cantidad = cantidad    # Cantidad disponible de este libro

    # Getters
    def get_isbn(self):
        return self.isbn

    def get_titulo(self):
        return self.titulo

    def get_id_autor(self):
        return self.id_autor

    def get_genero(self):
        return self.genero

    def get_anio(self):
        return self.anio

    def get_cantidad(self):
        return self.cantidad

    # Setters
    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_id_autor(self, id_autor):
        self.id_autor = id_autor

    def set_genero(self, genero):
        self.genero = genero

    def set_anio(self, anio):
        self.anio = anio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.titulo} (ISBN: {self.isbn}) - Autor ID: {self.id_autor} - Género: {self.genero}, Año: {self.anio}, Disponibles: {self.cantidad}"
