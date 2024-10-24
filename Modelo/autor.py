class Autor:
    def __init__(self, id_autor, nombre, apellido, nacionalidad):
        self.id_autor = id_autor            # Identificador único del autor
        self.nombre = nombre                # Nombre del autor
        self.apellido = apellido            # Apellido del autor
        self.nacionalidad = nacionalidad    # Nacionalidad del autor

    # Setters
    def set_id_autor(self, id_autor):
        self.id_autor = id_autor

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    # Getters
    def get_id_autor(self):
        return self.id_autor

    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido

    def get_nacionalidad(self):
        return self.nacionalidad
    

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.nacionalidad}"
