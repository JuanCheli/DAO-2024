from Persistencia.databaseSingleton import DatabaseSingleton
from datetime import datetime

class PrestamoRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def agregar_prestamo(self, id_usuario, isbn, fecha_prestamo, fecha_devolucion):
        # Verificar si ya existe un préstamo activo para el mismo usuario y libro
        if self.existe_prestamo(id_usuario, isbn):
            print(f"El préstamo para el usuario {id_usuario} con ISBN {isbn} ya existe.")
            return False

        query = """
        INSERT INTO prestamos (id_usuario, isbn, fecha_prestamo, fecha_devolucion, devuelto)
        VALUES (?, ?, ?, ?, ?)
        """
        # Por defecto, el préstamo se inserta con `devuelto = 0` (no devuelto)
        parameters = (id_usuario, isbn, fecha_prestamo, fecha_devolucion, 0)
        self.db.execute_query(query, parameters)
        return True

    def existe_prestamo(self, id_usuario, isbn):
        """Verifica si existe un préstamo activo para el mismo usuario y libro."""
        query = """
        SELECT 1 FROM prestamos 
        WHERE id_usuario = ? AND isbn = ? AND devuelto = 0
        """
        # Solo se consideran los préstamos no devueltos
        result = self.db.fetch_query(query, (id_usuario, isbn))
        return bool(result)

    def contar_prestamos_activos(self, id_usuario):
        """Cuenta cuántos préstamos activos tiene un usuario."""
        query = """
        SELECT COUNT(*) FROM prestamos 
        WHERE id_usuario = ? AND devuelto = 0
        """
        # Solo se cuentan los préstamos que aún no han sido devueltos
        result = self.db.fetch_query(query, (id_usuario,))
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

    def marcar_como_devuelto(self, id_prestamo):
        """Marca un préstamo como devuelto cambiando el valor del campo `devuelto` a 1."""
        query = "UPDATE prestamos SET devuelto = 1 WHERE id_prestamo = ?"
        parameter = (id_prestamo,)
        self.db.execute_query(query, parameter)
