class Usuario:
    def __init__(self, nombre, apellido, tipo_usuario, direccion, telefono):
        self.nombre = nombre                # Nombre del usuario
        self.apellido = apellido            # Apellido del usuario
        self.tipo_usuario = tipo_usuario    # Tipo de usuario (estudiante o profesor)
        self.direccion = direccion          # Dirección del usuario
        self.telefono = telefono            # Teléfono del usuario

    # Getters

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_tipo_usuario(self):
        return self.tipo_usuario

    def get_direccion(self):
        return self.direccion

    def get_telefono(self):
        return self.telefono

    # Setters

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_tipo_usuario(self, tipo_usuario):
        self.tipo_usuario = tipo_usuario

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_telefono(self, telefono):
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Tipo: {self.tipo_usuario}, Teléfono: {self.telefono}, Dirección: {self.direccion}"
