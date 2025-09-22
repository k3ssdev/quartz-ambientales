#!/usr/bin/env python3
"""
Migrador de Tags de Asignatura
Añade tags de curso-cuatrimestre-asignatura a archivos existentes
"""

import os
import re
from pathlib import Path

def procesar_archivo(archivo_path, tag_asignatura):
    """Añade el tag de asignatura a un archivo si no lo tiene"""
    try:
        with open(archivo_path, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Verificar si ya tiene el tag de asignatura
        if tag_asignatura in contenido:
            return False, "Ya tiene el tag"
        
        # Buscar la última línea con tags
        lineas = contenido.split('\n')
        ultima_linea_tags = -1
        
        for i, linea in enumerate(lineas):
            if '#' in linea and any(tag in linea for tag in [
                'clima-', 'tectonica-', 'estructura-', 'historia-', 'organismos-', 
                'rocas-', 'recursos-', 'geomorfologia', 'conceptos-', 'importancia-', 
                'nivel-', 'concepto-', 'proceso-'
            ]):
                ultima_linea_tags = i
        
        # Añadir el tag de asignatura
        if ultima_linea_tags >= 0:
            # Añadir al final de la línea de tags existente
            lineas[ultima_linea_tags] += f' {tag_asignatura}'
        else:
            # Crear nueva línea de tags al final
            lineas.append('')
            lineas.append(tag_asignatura)
        
        # Escribir archivo actualizado
        nuevo_contenido = '\n'.join(lineas)
        with open(archivo_path, 'w', encoding='utf-8') as f:
            f.write(nuevo_contenido)
        
        return True, "Tag añadido"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Función principal"""
    print("=== MIGRADOR DE TAGS DE ASIGNATURA ===")
    
    # Configuración
    base_path = Path('../Geología')
    tag_asignatura = '#primero-1-geologia-1'
    
    print(f"Buscando archivos en: {base_path}")
    print(f"Tag a añadir: {tag_asignatura}")
    
    # Buscar todos los archivos markdown
    archivos_md = list(base_path.glob('**/*.md'))
    
    # Filtrar archivos que no sean índices
    archivos_contenido = [
        archivo for archivo in archivos_md 
        if not any(palabra in archivo.name.lower() for palabra in ['índice', 'index', 'home', 'readme'])
    ]
    
    print(f"Encontrados {len(archivos_contenido)} archivos de contenido")
    
    # Confirmar ejecución
    respuesta = input("¿Añadir tag de asignatura a todos los archivos? (s/N): ").strip().lower()
    if respuesta != 's':
        print("Migración cancelada")
        return
    
    # Procesar archivos
    archivos_modificados = 0
    archivos_sin_cambios = 0
    errores = 0
    
    print("\n=== PROCESANDO ARCHIVOS ===")
    
    for archivo in archivos_contenido:
        exito, mensaje = procesar_archivo(archivo, tag_asignatura)
        
        if exito:
            archivos_modificados += 1
            print(f"✅ {archivo.name} - {mensaje}")
        elif "Ya tiene el tag" in mensaje:
            archivos_sin_cambios += 1
            print(f"⏭️  {archivo.name} - {mensaje}")
        else:
            errores += 1
            print(f"❌ {archivo.name} - {mensaje}")
    
    print(f"\n=== RESUMEN ===")
    print(f"Archivos procesados: {len(archivos_contenido)}")
    print(f"Archivos modificados: {archivos_modificados}")
    print(f"Sin cambios: {archivos_sin_cambios}")
    print(f"Errores: {errores}")
    
    if archivos_modificados > 0:
        print(f"\n✅ Tag {tag_asignatura} añadido exitosamente!")

if __name__ == "__main__":
    main()