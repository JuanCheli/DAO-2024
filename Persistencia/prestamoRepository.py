from databaseSingleton import DatabaseSingleton

class PrestamoRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def agregar_prestamo(self, id_prestamo, id_usuario, id_libro, fecha_prestamo, fecha_devolucion):
        query = """
        INSERT INTO prestamos (id_prestamo, id_usuario, id_libro, fecha_prestamo, fecha_devolucion)
        VALUES (?, ?, ?, ?, ?)
        """
        parameters = (id_prestamo, id_usuario, id_libro, fecha_prestamo, fecha_devolucion)
        self.db.execute_query(query, parameters)

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
