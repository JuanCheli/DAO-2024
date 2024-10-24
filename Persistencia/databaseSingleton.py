import sqlite3
from sqlite3 import Error

class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        try:
            # Establecer conexión a la base de datos
            self.connection = sqlite3.connect("singleton_database.db")
            self.cursor = self.connection.cursor()
            print("Conexión a SQLite establecida")
            
            # Inicializar la base de datos si es necesario
            self._initialize_database()
            
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def _initialize_database(self):
        """Función que crea las tablas si no existen"""
        try:
            # Crear las tablas usando la instrucción CREATE TABLE IF NOT EXISTS
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS libros (
                    isbn TEXT PRIMARY KEY, 
                    titulo TEXT, 
                    autor TEXT, 
                    genero TEXT, 
                    anio INT, 
                    cantidad INT
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario INT PRIMARY KEY, 
                    nombre TEXT, 
                    apellido TEXT, 
                    tipo_usuario TEXT, 
                    direccion TEXT, 
                    telefono INT
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS autores (
                    id_autor INT PRIMARY KEY, 
                    nombre TEXT, 
                    apellido TEXT, 
                    nacionalidad TEXT
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS prestamos (
                    id_prestamo INT PRIMARY KEY, 
                    id_usuario INT, 
                    id_libro INT, 
                    fecha_prestamo TEXT, 
                    fecha_devolucion TEXT,
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
                    FOREIGN KEY(id_libro) REFERENCES libros(isbn)
                )
            """)
            # Confirmar los cambios
            self.connection.commit()
            print("Tablas creadas o verificadas correctamente")
        except Error as e:
            print(f"Error al crear/verificar las tablas: {e}")

    def execute_query(self, query, parameters=()):
        """Ejecutar una consulta (INSERT, UPDATE, DELETE)"""
        try:
            self.cursor.execute(query, parameters)
            self.connection.commit()
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def fetch_query(self, query, parameters=()):
        """Ejecutar una consulta SELECT"""
        try:
            self.cursor.execute(query, parameters)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error al obtener datos: {e}")
            return None

    def close_connection(self):
        """Cerrar la conexión"""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Conexión cerrada")
