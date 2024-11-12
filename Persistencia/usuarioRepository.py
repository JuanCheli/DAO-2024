from Persistencia.databaseSingleton import DatabaseSingleton

class UsuarioRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def agregar_usuario(self, nombre, apellido, tipo_usuario, direccion, telefono):
        # Verificar si el usuario ya existe basándose en nombre, apellido y teléfono
        if self.existe_usuario(nombre, apellido, telefono):
            print(f"El usuario {nombre} {apellido} con teléfono {telefono} ya existe en la base de datos.")
            return False

        query = """
        INSERT INTO usuarios (nombre, apellido, tipo_usuario, direccion, telefono)
        VALUES (?, ?, ?, ?, ?)
        """
        parameters = (nombre, apellido, tipo_usuario, direccion, telefono)
        self.db.execute_query(query, parameters)
        return True
        

    def existe_usuario(self, nombre, apellido, telefono):
        """Verifica si un usuario con nombre, apellido y teléfono ya existe en la base de datos."""
        query = """
        SELECT 1 FROM usuarios 
        WHERE nombre = ? AND apellido = ? AND telefono = ?
        """
        result = self.db.fetch_query(query, (nombre, apellido, telefono))
        return bool(result)



    def obtener_usuario_por_id(self, id_usuario):
        query = "SELECT * FROM usuarios WHERE id_usuario = ?"
        result = self.db.fetch_query(query, (id_usuario,))
        return result
    
    def obtener_usuario_por_nombre_apellido(self, nombre, apellido):
        """Obtiene un usuario por nombre y apellido."""
        query = """
        SELECT id_usuario, nombre, apellido, tipo_usuario FROM usuarios 
        WHERE nombre = ? AND apellido = ?
        """
        result = self.db.fetch_query(query, (nombre, apellido))
        if result:
            # Retornar el primer usuario encontrado (en este caso se supone que no hay duplicados)
            return result[0]
        return None

    def listar_usuarios(self):
        query = "SELECT * FROM usuarios"
        result = self.db.fetch_query(query)
        return result
    
    def eliminar_usuario(self, id_usuario):
        query = "DELETE FROM usuarios WHERE id_usuario = ?"
        parameter = (id_usuario,)
        self.db.execute_query(query, parameter)
