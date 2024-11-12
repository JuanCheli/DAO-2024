from Persistencia.databaseSingleton import DatabaseSingleton

class AutorRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def agregar_autor(self, nombre, apellido, nacionalidad):
        if self.existe_autor(nombre, apellido):
            print(f"El autor {nombre} {apellido} ya existe en la base de datos.")
            return False

        query = """
        INSERT INTO autores (nombre, apellido, nacionalidad)
        VALUES (?, ?, ?)
        """
        parameters = (nombre, apellido, nacionalidad)
        self.db.execute_query(query, parameters)
        return True

    def existe_autor(self, nombre, apellido):
        """Verifica si un autor con el nombre y apellido especificados ya existe en la base de datos."""
        query = "SELECT 1 FROM autores WHERE nombre = ? AND apellido = ?"
        result = self.db.fetch_query(query, (nombre, apellido))
        return bool(result)


    def obtener_autor_por_id(self, id_autor):
        query = "SELECT * FROM autores WHERE id_autor = ?"
        result = self.db.fetch_query(query, (id_autor,))
        return result

    def listar_autores(self):
        query = "SELECT * FROM autores"
        result = self.db.fetch_query(query)
        return result
    
    def eliminar_autor(self, id_autor):
        query = "DELETE FROM autores WHERE id_autor = ?"
        parameter = (id_autor,)
        self.db.execute_query(query, parameter)
