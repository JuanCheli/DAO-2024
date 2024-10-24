class Usuario:
    def __init__(self, id_usuario, nombre, apellido, tipo_usuario, direccion, telefono):
        self.id_usuario = id_usuario        # Identificador único del usuario
        self.nombre = nombre                # Nombre del usuario
        self.apellido = apellido            # Apellido del usuario
        self.tipo_usuario = tipo_usuario    # Tipo de usuario (estudiante o profesor)
        self.direccion = direccion          # Dirección del usuario
        self.telefono = telefono            # Teléfono del usuario

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Tipo: {self.tipo_usuario}, Teléfono: {self.telefono}, Dirección: {self.direccion}"
