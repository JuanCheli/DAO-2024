class Prestamo:
    def __init__(self, usuario, isbn, fecha_prestamo, fecha_devolucion):
        self.usuario = usuario                    # Usuario que realizo el prestamo
        self.isbn = isbn                          # ISBN del libro prestado 
        self.fecha_prestamo = fecha_prestamo      # Fecha del préstamo
        self.fecha_devolucion = fecha_devolucion  # Fecha de devolución estimada

    # Getters

    def get_usuario(self):
        return self.usuario

    def get_isbn(self):
        return self.isbn

    def get_fecha_prestamo(self):
        return self.fecha_prestamo

    def get_fecha_devolucion(self):
        return self.fecha_devolucion

    # Setters

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_fecha_prestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo

    def set_fecha_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion

    def __str__(self):
        return (f"Préstamo ID: {self.id_prestamo}, Libro ISBN: {self.isbn}, "
                f"Usuario ID: {self.id_usuario}, Fecha Préstamo: {self.fecha_prestamo}, "
                f"Fecha Devolución: {self.fecha_devolucion}")
