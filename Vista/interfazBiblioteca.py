import os
import sys


this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from Controlador.gestorBiblioteca import BibliotecaGestor

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class InterfazBiblioteca:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Bibliotecas - DAO 2024")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")

        # Cargar icono de la ventana
        icon_path = os.path.join(this_file_path, "resources", "icon.ico")
        icon_image = Image.open(icon_path)
        icon_image = ImageTk.PhotoImage(icon_image)
        self.root.iconbitmap(icon_path)

        # Cargar y registrar las fuentes personalizadas
        font_path = os.path.join(this_file_path, "resources", "fonts", "Kanit", "Kanit-ExtraBold.ttf")
        self.custom_font = ctk.CTkFont(family=font_path, size=50, weight="bold")  # Tamaño grande para el título
        self.button_font = ctk.CTkFont(family=font_path, size=20)  # Tamaño pequeño para los botones

        # Cargar imagen de fondo
        self.background_image = Image.open(os.path.join(this_file_path, "resources", "wallpaper.jpg"))
        self.background_image = self.background_image.resize(
            (self.root.winfo_screenwidth(), self.root.winfo_screenheight()),
            Image.Resampling.LANCZOS
        )
        self.bg_photo = ImageTk.PhotoImage(self.background_image)

        # Crear el canvas para el fondo
        self.canvas = ctk.CTkCanvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Crear el gestor de biblioteca
        self.biblioteca_gestor = BibliotecaGestor()

        # Inicializar el menú principal
        self.menu_principal()
        
    def menu_principal(self):
        # Limpiar canvas
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Título del menú principal
        self.canvas.create_text(self.root.winfo_screenwidth() // 2, 175, text="Sistema de Gestión de Biblioteca", font=self.custom_font, fill="white")

        # Botones del menú principal
        botones = [
            ("Registrar Autor", self.pantalla_registrar_autor),
            ("Registrar Libro", self.pantalla_registrar_libro),
            ("Registrar Usuario", self.pantalla_registrar_usuario),
            ("Prestar Libro", self.pantalla_prestar_libro),
            ("Devolver Libro", self.pantalla_devolver_libro),
            ("Consultar Disponibilidad", self.pantalla_consultar_disponibilidad),
            ("Generar Reporte", self.pantalla_generar_reporte)
        ]
        
        y_position = 375
        for texto, comando in botones:
            boton = ctk.CTkButton(self.root, text=texto, font=self.button_font, command=comando, width=350, height=55, fg_color="#ffffff", text_color="black", border_width=2)
            self.canvas.create_window(self.root.winfo_screenwidth() // 2, y_position, window=boton)
            y_position += 70



    def pantalla_registrar_autor(self):
        self._crear_pantalla_formulario("Registrar Autor", ["Nombre", "Apellido", "Nacionalidad"], self.guardar_autor)

    def pantalla_registrar_libro(self):
        self._crear_pantalla_formulario("Registrar Libro", ["ISBN", "Título", "Autor", "Género", "Año", "Cantidad"], self.guardar_libro)

    def pantalla_registrar_usuario(self):
        # Cambiar para usar un OptionMenu para el campo "Tipo de usuario"
        self._crear_pantalla_formulario("Registrar Usuario", ["Nombre", "Apellido", "Tipo de usuario", "Dirección", "Teléfono"], self.guardar_usuario)

    def pantalla_prestar_libro(self):
        self._crear_pantalla_formulario("Prestar Libro", ["Nombre Usuario", "Apellido Usuario", "ISBN del libro a Prestar"], self.prestar_libro)

    def pantalla_devolver_libro(self):
        self._crear_pantalla_formulario("Devolver Libro", ["ID Préstamo"], self.devolver_libro)

    def pantalla_consultar_disponibilidad(self):
        self._crear_pantalla_formulario("Consultar Disponibilidad", ["ISBN"], self.consultar_disponibilidad)

    def pantalla_generar_reporte(self):
        """Llama a la generación de reporte en BibliotecaGestor y muestra un mensaje de confirmación."""
        self.biblioteca_gestor.generar_reporte()
        messagebox.showinfo("Reporte", "Reporte generado con éxito en la carpeta 'Reportes'.")
        self.menu_principal()

    def _crear_pantalla_formulario(self, titulo, campos, funcion_guardar):
        # Limpiar el canvas
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Título del formulario
        self.canvas.create_text(self.root.winfo_screenwidth() // 2, 100, text=titulo, font=self.custom_font, fill="white")

        # Campos de entrada dinámicos
        y_position = 180
        entradas = {}
        for campo in campos:
            etiqueta = ctk.CTkLabel(self.root, text=f"{campo}:", font=self.button_font, text_color="white")
            
            if campo == "Tipo de usuario":
                # Aquí usamos un CTkOptionMenu para "Tipo de usuario"
                opciones = ["Estudiante", "Docente"]
                entrada = ctk.CTkOptionMenu(self.root, values=opciones, font=self.button_font, width=300)
            else:
                entrada = ctk.CTkEntry(self.root, font=self.button_font, width=300)

            self.canvas.create_window(self.root.winfo_screenwidth() // 2 - 150, y_position, window=etiqueta, anchor="e")
            self.canvas.create_window(self.root.winfo_screenwidth() // 2 + 150, y_position, window=entrada, anchor="w")

            entradas[campo] = entrada
            y_position += 50

        # Botones de guardar y volver al menú
        confirmar_boton = ctk.CTkButton(self.root, text="Confirmar", font=self.button_font, command=lambda: funcion_guardar(entradas), width=200)
        volver_boton = ctk.CTkButton(self.root, text="Volver al Menú", font=self.button_font, command=self.menu_principal, width=200)

        self.canvas.create_window(self.root.winfo_screenwidth() // 2, y_position + 30, window=confirmar_boton)
        self.canvas.create_window(self.root.winfo_screenwidth() // 2, y_position + 90, window=volver_boton)


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
        tipo_usuario = 0 if entradas["Tipo de usuario"].get() == "Estudiante" else 1
        resultado = self.biblioteca_gestor.registrar_usuario(
            entradas["Nombre"].get(),
            entradas["Apellido"].get(),
            tipo_usuario,  # Enviamos el valor numérico
            entradas["Dirección"].get(),
            entradas["Teléfono"].get()
        )
        self._mostrar_resultado(resultado, "Usuario registrado correctamente.", "El usuario ya se encuentra registrado.")


    def prestar_libro(self, entradas):
        nombre_usuario = entradas["Nombre Usuario"].get()
        apellido_usuario = entradas["Apellido Usuario"].get()
        isbn_libro = entradas["ISBN del libro a Prestar"].get()
        resultado = self.biblioteca_gestor.prestar_libro(nombre_usuario, apellido_usuario, isbn_libro)
        # Mostrar el resultado
        if resultado is True:
            self._mostrar_resultado(True, "Préstamo realizado correctamente.", None)
        else:
            self._mostrar_resultado(False, None, resultado)

    
    def devolver_libro(self, entradas):
        resultado = self.biblioteca_gestor.devolver_libro(entradas["ID Préstamo"].get())
        
        if resultado == True:
            self._mostrar_resultado(resultado, "Libro devuelto correctamente.", "")
        else:
            self._mostrar_resultado(False, "", resultado)  # Muestra el mensaje de error específico, en base a lo que pasó


    def consultar_disponibilidad(self, entradas):
        cantidad = self.biblioteca_gestor.consultar_disponibilidad(entradas["ISBN"].get())
        if cantidad is not False:
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
    root = ctk.CTk()
    app = InterfazBiblioteca(root)
    root.mainloop()
