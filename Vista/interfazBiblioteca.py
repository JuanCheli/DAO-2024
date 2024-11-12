import os
import sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Controlador.gestorBiblioteca import BibliotecaGestor

class InterfazBiblioteca:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Biblioteca")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")

        # Cargar icono de la ventana
        icon_path = os.path.join(this_file_path, "resources", "icon.png")
        self.icono_ventana = PhotoImage(file=icon_path)
        self.root.iconphoto(False, self.icono_ventana)

        # Cargar imagen de fondo
        self.background_image = Image.open(os.path.join(this_file_path, "resources", "wallpaper.jpg"))
        self.background_image = self.background_image.resize(
            (self.root.winfo_screenwidth(), self.root.winfo_screenheight()),
            Image.Resampling.LANCZOS
        )
        self.bg_photo = ImageTk.PhotoImage(self.background_image)

        # Crear el canvas para el fondo
        self.canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Crear el gestor de biblioteca
        self.biblioteca_gestor = BibliotecaGestor()

        # Contenedor principal y widget de menú
        self.main_frame = Frame(self.root, bg="white", bd=5, relief=SOLID)
        self.main_frame.place(relx=0.5, rely=0.3, anchor="center", width=400, height=550)
        
        # Inicializar los diferentes frames de pantalla
        self.menu_principal()
        
    def menu_principal(self):
        # Limpiar frame principal
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Botones de menú principal
        Label(self.main_frame, text="Sistema de Gestión de Biblioteca", font=("Verdana", 16, "bold"), bg="white").grid(row=0, column=0, pady=10)

        Button(self.main_frame, text="Registrar Autor", font=("Arial", 14, "bold"), command=self.pantalla_registrar_autor, width=20, bg="#3498db", fg="white").grid(row=1, column=0, pady=10)
        Button(self.main_frame, text="Registrar Libro", font=("Arial", 14, "bold"), command=self.pantalla_registrar_libro, width=20, bg="#3498db", fg="white").grid(row=2, column=0, pady=10)
        Button(self.main_frame, text="Registrar Usuario", font=("Arial", 14, "bold"), command=self.pantalla_registrar_usuario, width=20, bg="#3498db", fg="white").grid(row=3, column=0, pady=10)
        Button(self.main_frame, text="Prestar Libro", font=("Arial", 14, "bold"), command=self.pantalla_prestar_libro, width=20, bg="#3498db", fg="white").grid(row=4, column=0, pady=10)
        Button(self.main_frame, text="Devolver Libro", font=("Arial", 14, "bold"), command=self.pantalla_devolver_libro, width=20, bg="#3498db", fg="white").grid(row=5, column=0, pady=10)
        Button(self.main_frame, text="Consultar Disponibilidad", font=("Arial", 14, "bold"), command=self.pantalla_consultar_disponibilidad, width=20, bg="#3498db", fg="white").grid(row=6, column=0, pady=10)

    def pantalla_registrar_autor(self):
        self._crear_pantalla_formulario("Registrar Autor", ["Nombre", "Apellido", "Nacionalidad"], self.guardar_autor)

    def pantalla_registrar_libro(self):
        self._crear_pantalla_formulario("Registrar Libro", ["ISBN", "Título", "Autor", "Género", "Año", "Cantidad"], self.guardar_libro)

    def pantalla_registrar_usuario(self):
        self._crear_pantalla_formulario("Registrar Usuario", ["Nombre", "Apellido", "Tipo de usuario", "Dirección", "Teléfono"], self.guardar_usuario)

    def pantalla_prestar_libro(self):
        self._crear_pantalla_formulario("Prestar Libro", ["Nombre Usuario", "Apellido Usuario", "ISBN"], self.prestar_libro)

    def pantalla_devolver_libro(self):
        self._crear_pantalla_formulario("Devolver Libro", ["ID Préstamo"], self.devolver_libro)

    def pantalla_consultar_disponibilidad(self):
        self._crear_pantalla_formulario("Consultar Disponibilidad", ["ISBN"], self.consultar_disponibilidad)

    def _crear_pantalla_formulario(self, titulo, campos, funcion_guardar):
        # Limpiar el frame principal
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Título
        Label(self.main_frame, text=titulo, font=("Arial", 16, "bold"), bg="white").grid(row=0, column=0, pady=10, columnspan=2)

        # Campos de entrada dinámicos
        entradas = {}
        for i, campo in enumerate(campos, start=1):
            Label(self.main_frame, text=f"{campo}:", bg="white").grid(row=i, column=0, sticky=W, padx=10)
            entradas[campo] = Entry(self.main_frame)
            entradas[campo].grid(row=i, column=1, pady=5, padx=10)

        # Botón de guardar
        Button(self.main_frame, text="Guardar", command=lambda: funcion_guardar(entradas), bg="#3498db", fg="white").grid(row=len(campos) + 1, column=0, columnspan=2, pady=15)
        Button(self.main_frame, text="Volver al Menú", command=self.menu_principal, bg="#e74c3c", fg="white").grid(row=len(campos) + 2, column=0, columnspan=2, pady=5)

    # Funciones para cada acción
    def guardar_autor(self, entradas):
        resultado = self.biblioteca_gestor.registrar_autor(
            entradas["Nombre"].get(),
            entradas["Apellido"].get(),
            entradas["Nacionalidad"].get()
        )
        self._mostrar_resultado(resultado, "Autor registrado correctamente.", "El autor ya se encuentra registrado.")

    def guardar_libro(self, entradas):
        resultado = self.biblioteca_gestor.registrar_libro(
            entradas["ISBN"].get(),
            entradas["Título"].get(),
            entradas["Autor"].get(),
            entradas["Género"].get(),
            entradas["Año"].get(),
            entradas["Cantidad"].get()
        )
        self._mostrar_resultado(resultado, "Libro registrado correctamente.", "El libro ya se encuentra registrado.")

    def guardar_usuario(self, entradas):
        resultado = self.biblioteca_gestor.registrar_usuario(
            entradas["Nombre"].get(),
            entradas["Apellido"].get(),
            entradas["Tipo de usuario"].get(),
            entradas["Dirección"].get(),
            entradas["Teléfono"].get()
        )
        self._mostrar_resultado(resultado, "Usuario registrado correctamente.", "El usuario ya se encuentra registrado.")

    def prestar_libro(self, entradas):
        resultado = self.biblioteca_gestor.prestar_libro(
            entradas["Nombre Usuario"].get(),
            entradas["Apellido Usuario"].get(),
            entradas["ISBN"].get()
        )
        self._mostrar_resultado(resultado, "Préstamo realizado correctamente.", "No se pudo realizar el préstamo.")

    def devolver_libro(self, entradas):
        resultado = self.biblioteca_gestor.devolver_libro(entradas["ID Préstamo"].get())
        self._mostrar_resultado(resultado, "Libro devuelto correctamente.", "No se pudo devolver el libro.")

    def consultar_disponibilidad(self, entradas):
        cantidad = self.biblioteca_gestor.consultar_disponibilidad(entradas["ISBN"].get())
        if cantidad is not None:
            messagebox.showinfo("Disponibilidad", f"Cantidad disponible: {cantidad}")
        else:
            messagebox.showerror("Error", "Libro no encontrado.")
        self.menu_principal()

    def _mostrar_resultado(self, resultado, mensaje_exito, mensaje_error):
        if resultado:
            messagebox.showinfo("Éxito", mensaje_exito)
        else:
            messagebox.showerror("Error", mensaje_error)
        self.menu_principal()


if __name__ == "__main__":
    root = Tk()
    app = InterfazBiblioteca(root)
    root.mainloop()
