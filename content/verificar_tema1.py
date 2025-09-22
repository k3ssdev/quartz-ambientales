#!/usr/bin/env python3
"""
Script para verificar qué términos del Tema 1 ya tienen la etiqueta #geologia1-tema-01
y cuáles necesitan que se les agregue
"""

import os
from pathlib import Path

def normalizar_nombre(nombre):
    """Normaliza nombres para la búsqueda (sin tildes, espacios, etc.)"""
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ñ': 'n', ' ': ' ', '-': ' ', '_': ' '
    }
    nombre_norm = nombre.lower()
    for original, replacement in replacements.items():
        nombre_norm = nombre_norm.replace(original, replacement)
    return nombre_norm

def buscar_archivo_concepto(termino, directorio_conceptos):
    """Busca el archivo correspondiente a un término"""
    # Lista de posibles nombres para buscar
    posibles_nombres = [
        termino,
        termino.capitalize(),
        termino.title(),
        termino.lower(),
        termino.upper(),
        # Variaciones específicas
        termino.replace('«', '').replace('»', ''),  # Para "capa D"
        termino.replace(' oceánica', ' oceánicas') if 'oceánica' in termino else termino,
        termino.replace('s, principio de', '') if ', principio de' in termino else termino,
        termino.replace(', ley de', '') if ', ley de' in termino else termino,
    ]
    
    # Buscar en todos los archivos
    for ruta in Path(directorio_conceptos).rglob("*.md"):
        nombre_archivo = ruta.stem
        for posible in posibles_nombres:
            if normalizar_nombre(nombre_archivo) == normalizar_nombre(posible):
                return ruta
    
    return None

def verificar_etiqueta_tema01(archivo):
    """Verifica si un archivo tiene la etiqueta #geologia1-tema-01"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        return "#geologia1-tema-01" in contenido
    except:
        return False

def main():
    # Lista de términos del Tema 1
    terminos_tema1 = [
        "astenosfera",
        "atmósfera", 
        "biosfera",
        "capa D",
        "catastrofismo",
        "ciencia del sistema Tierra",
        "ciclo de las rocas",
        "corteza",
        "cratón",
        "cuenca oceánica profunda",
        "datación relativa",
        "dorsal oceánica",
        "escudo",
        "fosa submarina",
        "Geología",
        "Geología física",
        "Geología histórica", 
        "geosfera",
        "hidrosfera",
        "hipótesis",
        "interfaz",
        "litosfera",
        "llanura abisal",
        "manto",
        "manto inferior",
        "margen continental",
        "mecanismo de realimentación negativa",
        "mecanismo de realimentación positiva",
        "monte submarino",
        "nebulosa solar",
        "núcleo",
        "núcleo externo", 
        "núcleo interno",
        "pie de talud",
        "plataforma continental",
        "plataforma estable",
        "roca ígnea",
        "roca metamórfica",
        "roca sedimentaria",
        "sistema",
        "sistema abierto",
        "sistema cerrado",
        "sucesión de fósiles",
        "superposición",
        "talud continental",
        "teoría",
        "teoría de la nebulosa primitiva",
        "uniformismo",
        "zona de transición"
    ]
    
    directorio_conceptos = "Geología/Conceptos"
    
    print(f"🔍 Verificando estado de {len(terminos_tema1)} términos del Tema 1...")
    print()
    
    encontrados_con_etiqueta = []
    encontrados_sin_etiqueta = []
    no_encontrados = []
    
    for termino in terminos_tema1:
        archivo = buscar_archivo_concepto(termino, directorio_conceptos)
        
        if archivo:
            if verificar_etiqueta_tema01(archivo):
                encontrados_con_etiqueta.append((termino, archivo.name))
            else:
                encontrados_sin_etiqueta.append((termino, archivo.name))
        else:
            no_encontrados.append(termino)
    
    # Mostrar resultados
    print(f"✅ **TÉRMINOS CON ETIQUETA #geologia1-tema-01** ({len(encontrados_con_etiqueta)}):")
    for termino, archivo in sorted(encontrados_con_etiqueta):
        print(f"  ✅ {termino} → {archivo}")
    
    print(f"\n⚠️  **TÉRMINOS SIN ETIQUETA** ({len(encontrados_sin_etiqueta)}):")
    for termino, archivo in sorted(encontrados_sin_etiqueta):
        print(f"  📝 {termino} → {archivo}")
    
    print(f"\n❌ **TÉRMINOS NO ENCONTRADOS** ({len(no_encontrados)}):")
    for termino in sorted(no_encontrados):
        print(f"  ❓ {termino}")
    
    print(f"\n📊 **RESUMEN:**")
    print(f"  ✅ Con etiqueta: {len(encontrados_con_etiqueta)}")
    print(f"  ⚠️  Sin etiqueta: {len(encontrados_sin_etiqueta)}")
    print(f"  ❌ No encontrados: {len(no_encontrados)}")
    print(f"  📝 Total términos: {len(terminos_tema1)}")
    
    if encontrados_sin_etiqueta:
        print(f"\n🔧 Necesitan agregarse la etiqueta #geologia1-tema-01:")
        for termino, archivo in sorted(encontrados_sin_etiqueta):
            print(f"  - {archivo}")

if __name__ == "__main__":
    main()