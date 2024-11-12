import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from Persistencia.libroRepository import LibroRepository
from Persistencia.autorRepository import AutorRepository
from Persistencia.usuarioRepository import UsuarioRepository
from Persistencia.prestamoRepository import PrestamoRepository

from Reportes.reportes import crear_reporte

from datetime import datetime, timedelta


class BibliotecaGestor:
    def __init__(self):
        self.libro_repo = LibroRepository()
        self.autor_repo = AutorRepository()
        self.usuario_repo = UsuarioRepository()
        self.prestamo_repo = PrestamoRepository()

    # 1. Registro de Autores
    def registrar_autor(self, nombre, apellido, nacionalidad):
        res = self.autor_repo.agregar_autor(nombre, apellido, nacionalidad)
        return res

    # 2. Registro de Libros
    def registrar_libro(self, isbn, titulo, autor, genero, anio, cantidad):
        res = self.libro_repo.agregar_libro(isbn, titulo, autor, genero, anio, cantidad)
        return res

    # 3. Registro de Usuarios
    def registrar_usuario(self, nombre, apellido, tipo_usuario, direccion, telefono):
        res = self.usuario_repo.agregar_usuario(nombre, apellido, tipo_usuario, direccion, telefono)
        return res

    # 4. Préstamo de Libros
    def prestar_libro(self, nombre, apellido, isbn):
        # Obtener usuario y verificar si existe
        usuario_existente = self.usuario_repo.obtener_usuario_por_nombre_apellido(nombre, apellido)
        if not usuario_existente:
            return "Usuario no encontrado."
        
        id_usuario = usuario_existente[0][0]  # Obtener el id_usuario del resultado

        tipo_usuario = usuario_existente[0][2]  # El tipo_usuario es el tercer campo
        max_libros = (3 if tipo_usuario == 0 else 5)
        prestamos_activos = self.prestamo_repo.contar_prestamos_activos(id_usuario)

        # Verificar límite de préstamos
        if prestamos_activos > max_libros:
            return f"El usuario ya tiene el máximo de libros permitidos en préstamo ({max_libros})."

        # Verificar disponibilidad del libro
        libro = self.libro_repo.obtener_libro_por_isbn(isbn)
        if not libro or libro[0][5] <= 0:
            return "El libro no existe o no está disponible para préstamo."

        # Realizar préstamo
        fecha_prestamo = datetime.now().date()
        fecha_devolucion = fecha_prestamo + timedelta(days=30)
        self.prestamo_repo.agregar_prestamo(id_usuario, isbn, fecha_prestamo, fecha_devolucion)

        # Actualizar cantidad disponible del libro
        nueva_cantidad = libro[0][5] - 1
        self.libro_repo.actualizar_cantidad(isbn, nueva_cantidad)
        return True

    # 5. Devolución de Libros
    def devolver_libro(self, prestamo):
        # Verificar si el préstamo existe
        prestamo_existente = self.prestamo_repo.obtener_prestamo_por_id(prestamo)
        if not prestamo_existente:
            return False
            

        # Verificar si el libro está dentro del plazo de devolución
        if datetime.strptime(prestamo_existente[0][4], "%Y-%m-%d").date() < datetime.now().date():  # Verificar si la fecha de devolución es pasada
            print(f"El préstamo está fuera del plazo.")
        
        # Marcar el préstamo como devuelto
        self.prestamo_repo.marcar_como_devuelto(prestamo)

        # Actualizar cantidad disponible del libro
        isbn = prestamo_existente[0][2]
        libro = self.libro_repo.obtener_libro_por_isbn(isbn)
        nueva_cantidad = libro[0][5] + 1
        self.libro_repo.actualizar_cantidad(isbn, nueva_cantidad)
        return True


    # 6. Consulta de Disponibilidad
    def consultar_disponibilidad(self, isbn):
        libro = self.libro_repo.obtener_libro_por_isbn(isbn)
        if libro:
            return libro[0][5]
        else:
            return False
        
    # 7. Generación de Reportes
    def generar_reporte(self):
        """Genera un reporte PDF de toda la información solicitada."""
        crear_reporte() 
        print("Reporte generado con éxito.")
