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
        self.root.title("Gestor de Bibliotecas - DAO 2024")
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
        self.main_frame = Frame(self.root, bd=5, relief=FLAT)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=int(self.root.winfo_screenwidth() * 0.6), height=int(self.root.winfo_screenheight() * 0.8))
        
        # Frame secundario para centrar contenido en main_frame
        self.center_frame = Frame(self.main_frame, bd=0)
        self.center_frame.pack(expand=True)

        # Inicializar los diferentes frames de pantalla
        self.menu_principal()
        
    def menu_principal(self):
        # Limpiar frame secundario
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Título del menú principal
        Label(self.center_frame, text="Sistema de Gestión de Biblioteca", font=("Verdana", 26, "bold"), fg="black").pack(pady=30)

        # Botones de menú principal
        Button(self.center_frame, text="Registrar Autor", font=("Arial", 20, "bold"), command=self.pantalla_registrar_autor, width=30, height=2, bg="#3498db", fg="white").pack(pady=15)
        Button(self.center_frame, text="Registrar Libro", font=("Arial", 20, "bold"), command=self.pantalla_registrar_libro, width=30, height=2, bg="#3498db", fg="white").pack(pady=15)
        Button(self.center_frame, text="Registrar Usuario", font=("Arial", 20, "bold"), command=self.pantalla_registrar_usuario, width=30, height=2, bg="#3498db", fg="white").pack(pady=15)
        Button(self.center_frame, text="Prestar Libro", font=("Arial", 20, "bold"), command=self.pantalla_prestar_libro, width=30, height=2, bg="#3498db", fg="white").pack(pady=15)
        Button(self.center_frame, text="Devolver Libro", font=("Arial", 20, "bold"), command=self.pantalla_devolver_libro, width=30, height=2, bg="#3498db", fg="white").pack(pady=15)
        Button(self.center_frame, text="Consultar Disponibilidad", font=("Arial", 20, "bold"), command=self.pantalla_consultar_disponibilidad, width=30, height=2, bg="#3498db", fg="white").pack(pady=15)


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
        # Limpiar el frame secundario
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Título del formulario
        Label(self.center_frame, text=titulo, font=("Arial", 24, "bold"), fg="black").pack(pady=20)

        # Campos de entrada dinámicos
        entradas = {}
        for campo in campos:
            frame_campo = Frame(self.center_frame, bd=0)
            frame_campo.pack(pady=5)

            Label(frame_campo, text=f"{campo}:", font=("Arial", 18)).pack(side=LEFT, padx=10)
            entradas[campo] = Entry(frame_campo, font=("Arial", 16), width=35)
            entradas[campo].pack(side=RIGHT, padx=10)

        # Botones de guardar y volver al menú
        Button(self.center_frame, text="Guardar", font=("Arial", 18, "bold"), command=lambda: funcion_guardar(entradas), bg="#3498db", fg="white").pack(pady=20)
        Button(self.center_frame, text="Volver al Menú", font=("Arial", 18, "bold"), command=self.menu_principal, bg="#e74c3c", fg="white").pack(pady=10)

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
