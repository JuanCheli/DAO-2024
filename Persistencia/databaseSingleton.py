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
            self.connection = sqlite3.connect("DAO-2024/biblioteca.db")
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
                    isbn INTEGER PRIMARY KEY NOT NULL, 
                    titulo TEXT NOT NULL, 
                    id_autor INT NOT NULL, 
                    genero TEXT NOT NULL, 
                    anio INT NOT NULL, 
                    cantidad INT NOT NULL,
                    FOREIGN KEY(id_autor) REFERENCES autores(id_autor)
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT NOT NULL, 
                    apellido TEXT NOT NULL, 
                    tipo_usuario INT NOT NULL, 
                    direccion TEXT NOT NULL, 
                    telefono INT NOT NULL
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS autores (
                    id_autor INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT NOT NULL, 
                    apellido TEXT NOT NULL, 
                    nacionalidad TEXT NOT NULL
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS prestamos (
                    id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,  
                    id_usuario INT NOT NULL, 
                    isbn TEXT NOT NULL, 
                    fecha_prestamo TEXT NOT NULL, 
                    fecha_devolucion TEXT NOT NULL,
                    devuelto BOOLEAN NOT NULL,
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
                    FOREIGN KEY(isbn) REFERENCES libros(isbn)
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


if __name__ == "__main__":
    # Crear una instancia de la clase DatabaseSingleton
    db = DatabaseSingleton()
