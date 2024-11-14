from Persistencia.databaseSingleton import DatabaseSingleton

class MultaRepository:
    def __init__(self):
        self.db = DatabaseSingleton()

    def registrar_multa(self, id_usuario, isbn, dias_retraso, monto):
        """
        Inserta una nueva multa en la base de datos.
        """
        query = """
        INSERT INTO multas (id_usuario, isbn, dias_retraso, monto)
        VALUES (?, ?, ?, ?)
        """
        parameters = (id_usuario, isbn, dias_retraso, monto)
        self.db.execute_query(query, parameters)
        print(f"Multa registrada para el usuario {id_usuario} con ISBN {isbn}.")

    def obtener_multas_por_usuario(self, id_usuario):
        """
        Obtiene todas las multas de un usuario específico.
        """
        query = """
        SELECT * FROM multas WHERE id_usuario = ?
        """
        result = self.db.fetch_query(query, (id_usuario,))
        return result if result else None

    def listar_multas(self):
        """
        Lista todas las multas en la base de datos.
        """
        query = "SELECT * FROM multas"
        result = self.db.fetch_query(query)
        return result

    def eliminar_multa(self, id_multa):
        """
        Elimina una multa específica en función de su ID.
        """
        query = "DELETE FROM multas WHERE id_multa = ?"
        self.db.execute_query(query, (id_multa,))
        print(f"Multa con ID {id_multa} eliminada.")
