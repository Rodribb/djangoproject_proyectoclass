import os

# 📁 Ruta absoluta a la carpeta templates
ruta = r"C:\Users\Laura\OneDrive\Documentos\Ambiente de Trabalho\djangoproject\myapp\templates"

# 🧩 Lista de nombres de archivos HTML
archivos = [
    "sq_visitor_satisfaction.html",
    "sq_crowding.html",
    "sq_market_segmentation.html",
    "sq_value_for_money.html",
    "sq_accessibility.html",
    "sq_content_quality.html",
    "sq_journey.html",
    "sq_benchmarking.html",
    "sq_communications.html",
    "sq_monitoring.html"
]

# 🧠 Generar cada archivo
for nombre in archivos:
    ruta_completa = os.path.join(ruta, nombre)
    titulo = nombre.replace(".html", "").replace("_", " ").title()

    contenido = (
        "{% extends 'base.html' %}\n"
        "{% block title %}" + titulo + "{% endblock %}\n"
        "{% block content %}\n"
        "  <h1>" + titulo + "</h1>\n"
        "  <p>This page will include details for this strategic question.</p>\n"
        "{% endblock %}\n"
    )

    with open(ruta_completa, "w", encoding="utf-8") as f:
        f.write(contenido)

print("✅ Archivos HTML creados correctamente.")



