#!/usr/bin/env python3
"""
Script mejorado para buscar términos no encontrados del Tema 1
Utiliza búsquedas más flexibles y alternativas
"""

import os
import re
from pathlib import Path
from difflib import SequenceMatcher

def normalizar_texto(texto):
    """Normaliza texto para comparación"""
    # Eliminar acentos y caracteres especiales
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ñ': 'N'
    }
    texto_norm = texto.lower()
    for original, replacement in replacements.items():
        texto_norm = texto_norm.replace(original, replacement)
    return texto_norm

def similitud_cadenas(a, b):
    """Calcula similitud entre dos cadenas"""
    return SequenceMatcher(None, normalizar_texto(a), normalizar_texto(b)).ratio()

def generar_variaciones(termino):
    """Genera variaciones posibles de un término"""
    variaciones = [termino]
    
    # Variaciones básicas
    variaciones.extend([
        termino.lower(),
        termino.upper(),
        termino.capitalize(),
        termino.title(),
        termino.replace(' ', ''),
        termino.replace(' ', '_'),
        termino.replace(' ', '-'),
    ])
    
    # Variaciones específicas por término
    if termino == "capa D":
        variaciones.extend([
            "capa d", "Capa D\"", "capa D\"", "capa-D", "capaD",
            "D layer", "D\""
        ])
    elif termino == "ciencia del sistema Tierra":
        variaciones.extend([
            "ciencia del sistema terrestre", "sistema Tierra", "sistema terrestre",
            "Earth system science", "geociencias", "ciencias de la Tierra"
        ])
    elif termino == "cratón":
        variaciones.extend([
            "craton", "cratones", "cratónico", "cratonica"
        ])
    elif termino == "cuenca oceánica profunda":
        variaciones.extend([
            "cuenca oceanica profunda", "cuenca oceánica", "cuenca abismal",
            "cuenca marina profunda", "fosa oceánica"
        ])
    elif termino == "dorsal oceánica":
        variaciones.extend([
            "dorsal oceanica", "dorsal marina", "dorsal medio-oceánica",
            "dorsal mesoceánica", "cresta oceánica"
        ])
    elif termino == "escudo":
        variaciones.extend([
            "escudo continental", "escudo precámbrico", "escudo cratónico"
        ])
    elif termino == "fosa submarina":
        variaciones.extend([
            "fosa oceánica", "fosa marina", "zanja oceánica", "trinchera oceánica"
        ])
    elif termino == "interfaz":
        variaciones.extend([
            "interface", "límite", "frontera", "contacto"
        ])
    elif termino == "llanura abisal":
        variaciones.extend([
            "llanura abismal", "llanuras abisales", "planicie abisal"
        ])
    elif termino == "margen continental":
        variaciones.extend([
            "márgen continental", "borde continental", "límite continental"
        ])
    elif "mecanismo de realimentación" in termino:
        if "negativa" in termino:
            variaciones.extend([
                "retroalimentación negativa", "feedback negativo", "realimentacion negativa"
            ])
        elif "positiva" in termino:
            variaciones.extend([
                "retroalimentación positiva", "feedback positivo", "realimentacion positiva"
            ])
    elif termino == "monte submarino":
        variaciones.extend([
            "monte oceánico", "montaña submarina", "volcán submarino", "guyot"
        ])
    elif termino == "nebulosa solar":
        variaciones.extend([
            "nebulosa primitiva", "nebulosa protosolar", "disco protoplanetario"
        ])
    elif termino == "pie de talud":
        variaciones.extend([
            "pie del talud", "base del talud", "pie de talud continental"
        ])
    elif termino == "plataforma estable":
        variaciones.extend([
            "plataforma cratónica", "plataforma continental estable"
        ])
    elif termino in ["sistema", "sistema abierto", "sistema cerrado"]:
        variaciones.extend([
            "sistemas", "sistema terrestre", "sistemas terrestres"
        ])
    elif termino == "sucesión de fósiles":
        variaciones.extend([
            "sucesión fósil", "sucesión paleontológica", "secuencia fósil"
        ])
    elif termino == "teoría":
        variaciones.extend([
            "teorias", "teoría científica", "teorías científicas"
        ])
    elif termino == "teoría de la nebulosa primitiva":
        variaciones.extend([
            "hipótesis de la nebulosa", "teoría nebular", "nebulosa primitiva",
            "hipótesis nebular", "teoria de la nebulosa"
        ])
    
    return list(set(variaciones))

def buscar_en_contenido(termino, directorio_conceptos):
    """Busca término en el contenido de los archivos"""
    coincidencias = []
    termino_norm = normalizar_texto(termino)
    
    for ruta in Path(directorio_conceptos).rglob("*.md"):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
                contenido_norm = normalizar_texto(contenido)
                
                # Buscar coincidencias exactas
                if termino_norm in contenido_norm:
                    coincidencias.append((ruta, "contenido_exacto", 1.0))
                
                # Buscar palabras clave del término
                palabras_termino = termino_norm.split()
                if len(palabras_termino) > 1:
                    coincidencias_parciales = sum(1 for palabra in palabras_termino if palabra in contenido_norm)
                    if coincidencias_parciales >= len(palabras_termino) * 0.6:  # 60% de las palabras
                        ratio = coincidencias_parciales / len(palabras_termino)
                        coincidencias.append((ruta, "contenido_parcial", ratio))
        except:
            continue
    
    return sorted(coincidencias, key=lambda x: x[2], reverse=True)

def buscar_por_similitud(termino, directorio_conceptos, umbral=0.7):
    """Busca archivos con nombres similares al término"""
    coincidencias = []
    
    for ruta in Path(directorio_conceptos).rglob("*.md"):
        nombre_archivo = ruta.stem
        similitud = similitud_cadenas(termino, nombre_archivo)
        
        if similitud >= umbral:
            coincidencias.append((ruta, "nombre_similar", similitud))
    
    return sorted(coincidencias, key=lambda x: x[2], reverse=True)

def main():
    terminos_no_encontrados = [
        "capa D",
        "ciencia del sistema Tierra",
        "cratón",
        "cuenca oceánica profunda",
        "dorsal oceánica",
        "escudo",
        "fosa submarina",
        "interfaz",
        "llanura abisal",
        "margen continental",
        "mecanismo de realimentación negativa",
        "mecanismo de realimentación positiva",
        "monte submarino",
        "nebulosa solar",
        "pie de talud",
        "plataforma estable",
        "sistema",
        "sistema abierto",
        "sistema cerrado",
        "sucesión de fósiles",
        "teoría",
        "teoría de la nebulosa primitiva"
    ]
    
    directorio_conceptos = "Geología/Conceptos"
    
    print(f"🔍 Búsqueda mejorada de {len(terminos_no_encontrados)} términos no encontrados...")
    print()
    
    resultados_totales = {}
    
    for termino in terminos_no_encontrados:
        print(f"🔎 Buscando: **{termino}**")
        resultados_termino = []
        
        # Búsqueda 1: Por variaciones de nombre
        variaciones = generar_variaciones(termino)
        for variacion in variaciones[:5]:  # Limitar a las 5 primeras variaciones
            for ruta in Path(directorio_conceptos).rglob("*.md"):
                if normalizar_texto(ruta.stem) == normalizar_texto(variacion):
                    resultados_termino.append((ruta, "nombre_variacion", 1.0, variacion))
        
        # Búsqueda 2: Por similitud de nombres
        similitudes = buscar_por_similitud(termino, directorio_conceptos, 0.6)
        for ruta, tipo, score in similitudes[:3]:  # Top 3
            resultados_termino.append((ruta, tipo, score, ruta.stem))
        
        # Búsqueda 3: En contenido
        contenido = buscar_en_contenido(termino, directorio_conceptos)
        for ruta, tipo, score in contenido[:3]:  # Top 3
            resultados_termino.append((ruta, tipo, score, ruta.stem))
        
        # Eliminar duplicados y ordenar
        resultados_unicos = {}
        for ruta, tipo, score, nombre in resultados_termino:
            clave = str(ruta)
            if clave not in resultados_unicos or resultados_unicos[clave][2] < score:
                resultados_unicos[clave] = (ruta, tipo, score, nombre)
        
        resultados_ordenados = sorted(resultados_unicos.values(), key=lambda x: x[2], reverse=True)
        resultados_totales[termino] = resultados_ordenados[:3]  # Top 3 por término
        
        # Mostrar resultados para este término
        if resultados_ordenados:
            for i, (ruta, tipo, score, nombre) in enumerate(resultados_ordenados[:3]):
                score_pct = int(score * 100)
                tipo_emoji = {
                    "nombre_variacion": "✅",
                    "nombre_similar": "🔄",
                    "contenido_exacto": "📄",
                    "contenido_parcial": "📝"
                }.get(tipo, "❓")
                print(f"  {tipo_emoji} [{score_pct}%] {nombre} → {ruta.relative_to(Path(directorio_conceptos))}")
        else:
            print(f"  ❌ No se encontraron coincidencias")
        print()
    
    # Resumen final
    print("📊 **RESUMEN DE BÚSQUEDA MEJORADA:**")
    encontrados = sum(1 for resultados in resultados_totales.values() if resultados)
    print(f"  🔍 Términos con posibles coincidencias: {encontrados}/{len(terminos_no_encontrados)}")
    print(f"  ❌ Sin coincidencias: {len(terminos_no_encontrados) - encontrados}")
    
    print("\n🎯 **CANDIDATOS MÁS PROBABLES:**")
    for termino, resultados in resultados_totales.items():
        if resultados and resultados[0][2] >= 0.8:  # Score >= 80%
            ruta, tipo, score, nombre = resultados[0]
            score_pct = int(score * 100)
            print(f"  ✅ {termino} → {nombre} [{score_pct}%]")

if __name__ == "__main__":
    main()