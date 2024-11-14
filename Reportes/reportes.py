from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from Reportes.generadorEstadisticas import (
    prestamos_vencidos, grafico_libros_mas_prestados, grafico_usuarios_mas_prestamos
)
from Persistencia.libroRepository import LibroRepository
import os


def crear_reporte():
    # Asegurarse de que el directorio de reportes existe
    if not os.path.exists("DAO-2024/Reportes/reportes"):
        os.makedirs("DAO-2024/Reportes/reportes")

    # Crear documento PDF
    doc = SimpleDocTemplate("DAO-2024/Reportes/reportes/reporte_biblioteca.pdf", pagesize=A4)
    Story = []
    styles = getSampleStyleSheet()
    
    # Título del reporte
    Story.append(Paragraph("Reporte de Biblioteca", styles["Title"]))
    Story.append(Spacer(1, 12))
    
    # 1. Reporte de préstamos vencidos
    Story.append(Paragraph("Préstamos Vencidos", styles["Heading2"]))
    prestamos = prestamos_vencidos()
    data = [["ID Préstamo", "Usuario", "Libro", "Fecha Préstamo", "Fecha Devolución"]]
    data.extend([[p[0], f"{p[1]} {p[2]}", p[3], p[4], p[5]] for p in prestamos])

    # Crear la tabla de préstamos vencidos con estilo
    table = Table(data, colWidths=[60, 120, 120, 80, 80])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige)
    ]))
    Story.append(table)
    Story.append(Spacer(1, 12))

    # Generar gráficos y agregar al reporte
    # 2. Gráfico de libros más prestados
    Story.append(PageBreak())
    Story.append(Paragraph("Libros Más Prestados en el Último Mes", styles["Heading2"]))
    grafico_libros_mas_prestados()
    img_libros_mas_prestados = Image("DAO-2024/Reportes/reportes/img/libros_mas_prestados.png", width=400, height=200)
    Story.append(img_libros_mas_prestados)
    Story.append(Spacer(1, 12))
    
    # 3. Gráfico de usuarios con más préstamos
    Story.append(PageBreak())
    Story.append(Paragraph("Usuarios con Más Préstamos", styles["Heading2"]))
    grafico_usuarios_mas_prestamos()
    img_usuarios_mas_prestamos = Image("DAO-2024/Reportes/reportes/img/usuarios_mas_prestamos.png", width=400, height=200)
    Story.append(img_usuarios_mas_prestamos)
    Story.append(Spacer(1, 12))


    # 4. Reporte de Libros por Autor
    Story.append(PageBreak())
    Story.append(Paragraph("Libros por Autor", styles["Heading2"]))
    
    # Obtener datos de libros por autor usando LibroRepository
    libro_repo = LibroRepository()
    libros_por_autor = libro_repo.obtener_libros_por_autor()
    
    # Crear estructura de datos para la tabla de libros por autor
    data_libros = [["Autor", "Título del Libro", "Cantidad Disponible"]]
    autor_totales = {}
    
    for libro in libros_por_autor:
        autor, titulo, cantidad = libro
        data_libros.append([autor, titulo, cantidad])
        
        # Sumarizar cantidad por autor
        if autor in autor_totales:
            autor_totales[autor] += cantidad
        else:
            autor_totales[autor] = cantidad
    
    # Crear la tabla de libros por autor con estilo
    table_libros = Table(data_libros, colWidths=[120, 200, 80])
    table_libros.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige)
    ]))
    Story.append(table_libros)
    Story.append(Spacer(1, 12))

    # Agregar resumen de total de libros por autor
    Story.append(Paragraph("Resumen de Cantidad de Libros por Autor", styles["Heading2"]))
    resumen_data = [["Autor", "Total de Libros Disponibles"]]
    resumen_data.extend([[autor, total] for autor, total in autor_totales.items()])
    
    resumen_table = Table(resumen_data, colWidths=[200, 120])
    resumen_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.lightgrey)
    ]))
    Story.append(resumen_table)


    # Generar el PDF
    doc.build(Story)

    print("Reporte generado en DAO-2024/Reportes/reportes/reporte_biblioteca.pdf")
