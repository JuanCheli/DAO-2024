class Autor:
    def __init__(self, nombre, apellido, nacionalidad):           
        self.nombre = nombre                # Nombre del autor
        self.apellido = apellido            # Apellido del autor
        self.nacionalidad = nacionalidad    # Nacionalidad del autor

    # Getters
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido

    def get_nacionalidad(self):
        return self.nacionalidad
    
    # Setters

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad


    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.nacionalidad}"
