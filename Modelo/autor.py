class Autor:
    def __init__(self, id_autor, nombre, apellido, nacionalidad):
        self.id_autor = id_autor            # Identificador único del autor
        self.nombre = nombre                # Nombre del autor
        self.apellido = apellido            # Apellido del autor
        self.nacionalidad = nacionalidad    # Nacionalidad del autor

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.nacionalidad}"
