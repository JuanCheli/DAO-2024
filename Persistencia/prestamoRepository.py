from Persistencia.databaseSingleton import DatabaseSingleton
import datetime

class PrestamoRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def agregar_prestamo(self, id_usuario, isbn, fecha_prestamo, fecha_devolucion):
        # Verificar si ya existe un préstamo activo para el mismo usuario y libro
        if self.existe_prestamo(id_usuario, isbn):
            print(f"El préstamo para el usuario {id_usuario} con ISBN {isbn} ya existe.")
            return False

        query = """
        INSERT INTO prestamos (id_usuario, isbn, fecha_prestamo, fecha_devolucion)
        VALUES (?, ?, ?, ?, ?)
        """
        parameters = (id_usuario, isbn, fecha_prestamo, fecha_devolucion)
        self.db.execute_query(query, parameters)
        return True

    def existe_prestamo(self, id_usuario, isbn):
        """Verifica si existe un préstamo activo para el mismo usuario y libro."""
        query = """
        SELECT 1 FROM prestamos 
        WHERE id_usuario = ? AND isbn = ? AND fecha_devolucion >= ?
        """
        # Se verifica que la fecha de devolución no haya pasado (es decir, que esté activo)
        fecha_actual = datetime.now().date()
        result = self.db.fetch_query(query, (id_usuario, isbn, fecha_actual))
        return bool(result)
    
    def contar_prestamos_activos(self, id_usuario):
        """Cuenta cuántos préstamos activos tiene un usuario."""
        query = """
        SELECT COUNT(*) FROM prestamos 
        WHERE id_usuario = ? AND fecha_devolucion >= ?
        """
        fecha_actual = datetime.now().date()
        result = self.db.fetch_query(query, (id_usuario, fecha_actual))
        return result[0][0] if result else 0

    def obtener_prestamo_por_id(self, id_prestamo):
        query = "SELECT * FROM prestamos WHERE id_prestamo = ?"
        result = self.db.fetch_query(query, (id_prestamo,))
        return result

    def listar_prestamos(self):
        query = "SELECT * FROM prestamos"
        result = self.db.fetch_query(query)
        return result
    
    def eliminar_prestamo(self, id_prestamo):
        query = "DELETE FROM prestamos WHERE id_prestamo = ?"
        parameter = (id_prestamo,)
        self.db.execute_query(query, parameter)
