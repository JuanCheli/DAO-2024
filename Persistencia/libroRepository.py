from Persistencia.databaseSingleton import DatabaseSingleton
from Persistencia.autorRepository import AutorRepository

class LibroRepository:
    def __init__(self):
        self.db = DatabaseSingleton()
        self.autor_repo = AutorRepository()

    def agregar_libro(self, isbn, titulo, nombre_autor, genero, anio, cantidad):
        # Verificar si el libro ya existe
        if self.existe_libro(isbn):
            print(f"El libro con ISBN {isbn} ya existe en la base de datos.")
            return False

        # Separar el nombre y el apellido del autor
        nombre_partes = nombre_autor.split()

        if len(nombre_partes) > 1:
            nombre = nombre_partes[0]  # Primer elemento como nombre
            apellido = " ".join(nombre_partes[1:])  # El resto como apellido
        else:
            print("Error: Se requiere al menos un nombre y un apellido para el autor.")
            return False
        
        id_autor = self.autor_repo.existe_autor(nombre, apellido)

        if not id_autor:
            # Crear nuevo autor y obtener su id_autor
            self.autor_repo.agregar_autor(nombre, apellido, "Desconocida")  # Nacionalidad por defecto
            id_autor = self.autor_repo.existe_autor(nombre, apellido)  # Obtener el id_autor recién creado

        # Agregar el libro con el id_autor obtenido o creado
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
        

    def obtener_libros_por_autor(self):
        """Obtiene un listado de libros agrupados por autor, incluyendo la cantidad disponible."""
        query = """
            SELECT a.nombre || ' ' || a.apellido AS autor, l.titulo, l.cantidad 
            FROM libros l 
            JOIN autores a ON l.id_autor = a.id_autor
            ORDER BY autor
        """
        result = self.db.fetch_query(query)
        return result

