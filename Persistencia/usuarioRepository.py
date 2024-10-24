from databaseSingleton import DatabaseSingleton

class UsuarioRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def agregar_usuario(self, id_usuario, nombre, apellido, tipo_usuario, direccion, telefono):
        query = """
        INSERT INTO usuarios (id_usuario, nombre, apellido, tipo_usuario, direccion, telefono)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        parameters = (id_usuario, nombre, apellido, tipo_usuario, direccion, telefono)
        self.db.execute_query(query, parameters)

    def obtener_usuario_por_id(self, id_usuario):
        query = "SELECT * FROM usuarios WHERE id_usuario = ?"
        result = self.db.fetch_query(query, (id_usuario,))
        return result

    def listar_usuarios(self):
        query = "SELECT * FROM usuarios"
        result = self.db.fetch_query(query)
        return result
    
    def eliminar_usuario(self, id_usuario):
        query = "DELETE FROM usuarios WHERE id_usuario = ?"
        parameter = (id_usuario,)
        self.db.execute_query(query, parameter)
