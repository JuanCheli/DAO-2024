class Prestamo:
    def __init__(self, id_prestamo, id_usuario, isbn, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo            # Identificador único del préstamo
        self.id_usuario = id_usuario              # ID del usuario (clave foránea)
        self.isbn = isbn                          # ISBN del libro prestado (clave foránea)
        self.fecha_prestamo = fecha_prestamo      # Fecha del préstamo
        self.fecha_devolucion = fecha_devolucion  # Fecha de devolución estimada

    def __str__(self):
        return (f"Préstamo ID: {self.id_prestamo}, Libro ISBN: {self.isbn}, "
                f"Usuario ID: {self.id_usuario}, Fecha Préstamo: {self.fecha_prestamo}, "
                f"Fecha Devolución: {self.fecha_devolucion}")
