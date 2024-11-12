from Persistencia.databaseSingleton import DatabaseSingleton

class LibroRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def agregar_libro(self, isbn, titulo, id_autor, genero, anio, cantidad):
        # Verificar si el libro ya existe
        if self.existe_libro(isbn):
            print(f"El libro con ISBN {isbn} ya existe en la base de datos.")
            return False

        query = """
        INSERT INTO libros (isbn, titulo, id_autor, genero, anio, cantidad)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        parameters = (isbn, titulo, id_autor, genero, anio, cantidad)
        self.db.execute_query(query, parameters)
        return True

    def existe_libro(self, isbn):
        """Verifica si un libro con el ISBN especificado ya existe en la base de datos."""
        query = "SELECT 1 FROM libros WHERE isbn = ?"
        result = self.db.fetch_query(query, (isbn,))
        return bool(result)

    def obtener_libro_por_isbn(self, isbn):
        """Obtiene un libro específico por su ISBN."""
        query = "SELECT * FROM libros WHERE isbn = ?"
        result = self.db.fetch_query(query, (isbn,))
        return result

    def listar_libros(self):
        """Lista todos los libros en la base de datos."""
        query = "SELECT * FROM libros"
        result = self.db.fetch_query(query)
        return result

    def eliminar_libro(self, isbn):
        """Elimina un libro por su ISBN."""
        query = "DELETE FROM libros WHERE isbn = ?"
        parameter = (isbn,)
        self.db.execute_query(query, parameter)

    def actualizar_cantidad(self, isbn, nueva_cantidad):
        """Actualiza la cantidad disponible de un libro por su ISBN."""
        query = "UPDATE libros SET cantidad = ? WHERE isbn = ?"
        parameters = (nueva_cantidad, isbn)
        self.db.execute_query(query, parameters)

    def verificar_disponibilidad(self, isbn):
        """Verifica la disponibilidad de un libro, retornando la cantidad disponible."""
        query = "SELECT cantidad FROM libros WHERE isbn = ?"
        result = self.db.fetch_query(query, (isbn,))
        if result:
            return result[0][0] > 0  # Retorna True si hay al menos un ejemplar disponible
        else:
            print("El libro no se encontró en la base de datos.")
            return False

