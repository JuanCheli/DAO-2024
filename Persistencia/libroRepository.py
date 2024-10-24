from databaseSingleton import DatabaseSingleton
class LibroRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def agregar_libro(self, isbn, titulo, id_autor, genero, anio, cantidad):
        query = """
        INSERT INTO libros (isbn, titulo, autor, genero, anio, cantidad)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        parameters = (isbn, titulo, id_autor, genero, anio, cantidad)
        self.db.execute_query(query, parameters)

    def obtener_libro_por_isbn(self, isbn):
        query = "SELECT * FROM libros WHERE isbn = ?"
        result = self.db.fetch_query(query, (isbn,))
        return result

    def listar_libros(self):
        query = "SELECT * FROM libros"
        result = self.db.fetch_query(query)
        return result
    
    def eliminar_libro(self, isbn):
        query = "DELETE from libros WHERE isbn = ?"
        parameter = isbn
        self.db.execute_query(query, parameter)