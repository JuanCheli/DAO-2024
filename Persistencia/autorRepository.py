from databaseSingleton import DatabaseSingleton

class AutorRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def agregar_autor(self, id_autor, nombre, apellido, nacionalidad):
        query = """
        INSERT INTO autores (id_autor, nombre, apellido, nacionalidad)
        VALUES (?, ?, ?, ?)
        """
        parameters = (id_autor, nombre, apellido, nacionalidad)
        self.db.execute_query(query, parameters)

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
