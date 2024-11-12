import random
from datetime import datetime
from databaseSingleton import DatabaseSingleton

class CargaDatos:
    def __init__(self):
        self.db = DatabaseSingleton()

    def cargar_usuarios(self):
        nombres = ["Juan", "Ana", "Luis", "Maria", "Carlos", "Sofia", "Pedro", "Laura", "Jose", "Lucia", 
                   "David", "Elena", "Fernando", "Raquel", "Miguel", "Carla", "Pablo", "Isabel", "Diego", "Marta"]
        apellidos = ["Gomez", "Perez", "Lopez", "Diaz", "Rodriguez", "Martinez", "Hernandez", "Gonzalez", 
                     "Sanchez", "Garcia", "Fernandez", "Ruiz", "Alvarez", "Ramirez", "Jimenez", "Vazquez", "Moreno", 
                     "Torres", "Cruz", "Reyes"]

        tipos_usuario = [1, 2]  # 1 = estudiante, 2 = profesor
        direcciones = ["Av. Libertad 1234","Calle de los Olivos 567","Paseo del Prado 890","Calle Mayor 135",
                       "Av. de la Constitución 2468","Callejón de las Flores 321","Calle San Juan 876","Av. de la Paz 1920",
                       "Calle La Esperanza 1357","Calle del Sol 468","Av. del Parque 234","Calle Primavera 905","Paseo de la Reforma 6789",
                       "Calle Nueva 4321","Av. Los Álamos 5678","Calle de la Fuente 300","Calle Real 789","Camino Viejo 450","Calle del Río 2100","Av. del Bosque 134"]

        

        for i in range(20):
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            tipo_usuario = random.choice(tipos_usuario)
            telefono = random.randint(3511114231, 3519999999)
            direccion = random.choice(direcciones)
            query = """
                INSERT INTO usuarios (nombre, apellido, tipo_usuario, direccion, telefono) 
                VALUES (?, ?, ?, ?, ?)
            """
            parameters = (nombre, apellido, tipo_usuario, direccion, telefono)
            self.db.execute_query(query, parameters)

    def cargar_autores(self):
        nombres_autores = ["Gabriel Garcia Marquez", "J.K. Rowling", "George Orwell", "Mario Vargas Llosa", 
                           "Isabel Allende", "Juan Rulfo", "Carlos Fuentes", "Octavio Paz", "Julia de Burgos", 
                           "Pablo Neruda", "Emilio Salgari", "Alejo Carpentier", "Virginia Woolf", "Mark Twain", 
                           "Albert Camus", "Ernest Hemingway", "F. Scott Fitzgerald", "Charles Dickens", 
                           "Leo Tolstoy", "Jane Austen"]

        nacionalidades = ["Colombiana", "Británica", "Estadounidense", "Peruana", "Chilena", "Mexicana", "Cubana", 
                          "Francesa", "Italiana", "Rusa", "Española", "Australiana"]

        for i in range(20):
            nombre_completo = random.choice(nombres_autores).split(" ")
            nombre = nombre_completo[0]
            apellido = " ".join(nombre_completo[1:])
            nacionalidad = random.choice(nacionalidades)
            query = """
                INSERT INTO autores (nombre, apellido, nacionalidad) 
                VALUES (?, ?, ?)
            """
            parameters = (nombre, apellido, nacionalidad)
            self.db.execute_query(query, parameters)

    def cargar_libros(self):
        titulos = ["Cien Años de Soledad", "Harry Potter y la Piedra Filosofal", "1984", "La Casa Verde", 
                   "La Casa de los Espíritus", "Pedro Páramo", "Terra Nostra", "El Laberinto de la Soledad", 
                   "Don Quijote de la Mancha", "El Gran Gatsby", "El Retrato de Dorian Gray", "Ulises", 
                   "Crimen y Castigo", "Orgullo y Prejuicio", "Matar a un Ruiseñor", "El Señor de los Anillos", 
                   "La Odisea", "Fahrenheit 451", "Los Miserables", "Moby Dick"]

        generos = ["Realismo mágico", "Fantasía", "Distopía", "Narrativa", "Drama", "Aventura", "Filosofía", "Épico"]
        anios = [random.randint(1949, 2022) for _ in range(20)]
        cantidades = [5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]

        for i in range(20):
            titulo = titulos[i]
            id_autor = random.randint(1, 20) 
            genero = random.choice(generos)
            anio = random.choice(anios)
            cantidad = random.choice(cantidades)
            query = """
                INSERT INTO libros (isbn, titulo, id_autor, genero, anio, cantidad) 
                VALUES (?, ?, ?, ?, ?, ?)
            """
            isbn = f"{random.randint(9780000000000, 9789999999999)}"  # Genera un ISBN aleatorio
            parameters = (isbn, titulo, id_autor, genero, anio, cantidad)
            self.db.execute_query(query, parameters)

    def cargar_datos(self):
        self.cargar_usuarios()
        self.cargar_autores()
        self.cargar_libros()

if __name__ == "__main__":
    carga = CargaDatos()
    carga.cargar_datos()
    print("Datos cargados exitosamente.")
