#!/usr/bin/env python3
"""
Análisis de Contenido del Sistema de Etiquetado
Genera estadísticas para el índice general y analiza cumplimiento del sistema
"""

from analizador_obsidian import AnalizadorObsidian
from collections import Counter, defaultdict
import json
from datetime import datetime

def generar_estadisticas_indice():
    """Genera estadísticas específicas para el índice general"""
    analizador = AnalizadorObsidian('../Geología')
    analizador.procesar_directorio()
    
    # Obtener todos los tags usados
    todos_los_tags = []
    for tags_archivo in analizador.tags_por_archivo.values():
        todos_los_tags.extend(tags_archivo)
    
    counter_tags = Counter(todos_los_tags)
    
    # Calcular asignaturas activas
    asignaturas_activas = {}
    for tag, count in counter_tags.items():
        if tag in analizador.asignaturas_tags and count > 0:
            asignaturas_activas[analizador.asignaturas_tags[tag]] = count
    
    # Sistema de tags estándar
    tags_sistema = {
        'categorias': [
            'clima-oceanografia', 'geomorfologia', 'rocas-minerales', 'tectonica-placas',
            'historia-geologica', 'estructura-terrestre', 'procesos-geologicos', 
            'conceptos-fundamentales', 'recursos-riesgos'
        ],
        'importancia': ['importancia-1', 'importancia-2', 'importancia-3', 'importancia-4', 'importancia-5'],
        'tipos_proceso': ['proceso-fundamental', 'proceso-dinamico', 'proceso-estructural', 'proceso-historico'],
        'tipos_concepto': ['concepto-central', 'concepto-proceso', 'concepto-estructura', 'concepto-evento', 'concepto-personaje', 'concepto-herramienta'],
        'niveles': ['nivel-basico', 'nivel-intermedio', 'nivel-avanzado'],
        'rutas': ['ruta-fundamentos', 'ruta-procesos-dinamicos', 'ruta-materiales', 'ruta-tiempo-evolucion', 'ruta-estructura-terrestre']
    }
    
    # Calcular cumplimiento
    tags_estandar = set()
    for categoria in tags_sistema.values():
        tags_estandar.update(categoria)
    
    tags_sistema_usados = sum(1 for tag in tags_estandar if counter_tags.get(tag, 0) > 0)
    porcentaje_cumplimiento = (tags_sistema_usados / len(tags_estandar)) * 100
    
    # Generar estadísticas
    estadisticas = {
        'archivos_totales': len(analizador.archivos_procesados),
        'asignaturas_activas': len(asignaturas_activas),
        'asignaturas_detalle': asignaturas_activas,
        'tags_unicos': len(counter_tags),
        'cumplimiento_sistema': round(porcentaje_cumplimiento, 1),
        'fecha_actualizacion': datetime.now().strftime('%d/%m/%Y'),
        'tags_mas_usados': dict(counter_tags.most_common(10))
    }
    
    return estadisticas

def actualizar_indice_general():
    """Actualiza las estadísticas en el índice general automáticamente"""
    stats = generar_estadisticas_indice()
    
    # Construir texto de asignaturas
    num_asignaturas = stats['asignaturas_activas']
    if num_asignaturas == 1:
        texto_asignaturas = f"{num_asignaturas} (Geología)"
    else:
        asignaturas_nombres = list(stats['asignaturas_detalle'].keys())
        texto_asignaturas = f"{num_asignaturas} ({', '.join(asignaturas_nombres)})"
    
    # Nuevo bloque de estadísticas
    nuevo_bloque = f"""**📊 Estadísticas actuales:**
- **Archivos totales**: {stats['archivos_totales']}
- **Asignaturas activas**: {texto_asignaturas}
- **Tags únicos**: {stats['tags_unicos']}
- **Sistema de tags**: {stats['cumplimiento_sistema']}% cumplimiento

*Última actualización: {stats['fecha_actualizacion']}*"""
    
    return nuevo_bloque, stats

def analizar_cumplimiento():
    # Sistema de tags propuesto
    tags_sistema = {
        'categorias': [
            'clima-oceanografia', 'geomorfologia', 'rocas-minerales', 'tectonica-placas',
            'historia-geologica', 'estructura-terrestre', 'procesos-geologicos', 
            'conceptos-fundamentales', 'recursos-riesgos'
        ],
        'importancia': ['importancia-1', 'importancia-2', 'importancia-3', 'importancia-4', 'importancia-5'],
        'tipos_proceso': ['proceso-fundamental', 'proceso-dinamico', 'proceso-estructural', 'proceso-historico'],
        'tipos_concepto': ['concepto-central', 'concepto-proceso', 'concepto-estructura', 'concepto-evento', 'concepto-personaje', 'concepto-herramienta'],
        'niveles': ['nivel-basico', 'nivel-intermedio', 'nivel-avanzado'],
        'rutas': ['ruta-fundamentos', 'ruta-procesos-dinamicos', 'ruta-materiales', 'ruta-tiempo-evolucion', 'ruta-estructura-terrestre']
    }

    analizador = AnalizadorObsidian('../Geología')
    analizador.procesar_directorio()
    
    # Obtener todos los tags usados
    todos_los_tags = []
    for tags_archivo in analizador.tags_por_archivo.values():
        todos_los_tags.extend(tags_archivo)
    
    counter_tags = Counter(todos_los_tags)
    
    print("=" * 60)
    print("📊 ANÁLISIS DE CUMPLIMIENTO DEL SISTEMA DE ETIQUETADO")
    print("=" * 60)
    
    # 1. Análisis de categorías
    print("\n🏷️  CATEGORÍAS PRINCIPALES")
    print("-" * 40)
    
    archivos_por_categoria = defaultdict(int)
    for archivo, data in analizador.archivos_procesados.items():
        categoria = data['categoria']
        archivos_por_categoria[categoria] += 1
    
    for categoria in tags_sistema['categorias']:
        count = archivos_por_categoria[categoria]
        tag_count = counter_tags.get(categoria, 0)
        print(f"✅ #{categoria}: {count} archivos detectados, {tag_count} con tag")
    
    sin_categoria = archivos_por_categoria['sin-categoria']
    print(f"⚠️  sin-categoria: {sin_categoria} archivos")
    
    # 2. Análisis de importancia
    print("\n⭐ NIVELES DE IMPORTANCIA")
    print("-" * 40)
    
    for nivel in tags_sistema['importancia']:
        count = counter_tags.get(nivel, 0)
        status = "✅" if count > 0 else "❌"
        print(f"{status} #{nivel}: {count} archivos")
    
    # 3. Análisis de tipos de concepto
    print("\n🎯 TIPOS DE CONCEPTO")
    print("-" * 40)
    
    for tipo in tags_sistema['tipos_concepto']:
        count = counter_tags.get(tipo, 0)
        status = "✅" if count > 0 else "❌"
        print(f"{status} #{tipo}: {count} archivos")
    
    # 4. Análisis de tipos de proceso
    print("\n⚡ TIPOS DE PROCESO")
    print("-" * 40)
    
    for tipo in tags_sistema['tipos_proceso']:
        count = counter_tags.get(tipo, 0)
        status = "✅" if count > 0 else "❌"
        print(f"{status} #{tipo}: {count} archivos")
    
    # 5. Análisis de niveles de aprendizaje
    print("\n📚 NIVELES DE APRENDIZAJE")
    print("-" * 40)
    
    for nivel in tags_sistema['niveles']:
        count = counter_tags.get(nivel, 0)
        status = "✅" if count > 0 else "❌"
        print(f"{status} #{nivel}: {count} archivos")
    
    # 6. Tags populares que NO están en el sistema
    print("\n🔍 TAGS POPULARES NO ESTÁNDAR (≥5 usos)")
    print("-" * 40)
    
    tags_estandar = set()
    for categoria in tags_sistema.values():
        tags_estandar.update(categoria)
    
    tags_no_estandar = []
    for tag, count in counter_tags.most_common():
        if count >= 5 and tag not in tags_estandar:
            tags_no_estandar.append((tag, count))
    
    for tag, count in tags_no_estandar[:15]:
        print(f"🔸 #{tag}: {count} archivos")
    
    # 7. Mapeo de migración sugerido
    print("\n🔄 MIGRACIÓN SUGERIDA")
    print("-" * 40)
    
    mapeo_migracion = {
        'tectonica': 'tectonica-placas',
        'definicion': 'concepto-central',  # Muchos archivos con #definicion podrían ser centrales
        'proceso': 'proceso-dinamico',
        'vida': 'historia-geologica',  # Los archivos de vida suelen ser históricos
        'biosfera': 'estructura-terrestre',
        'astronomia': 'conceptos-fundamentales',
        'sistema-solar': 'conceptos-fundamentales',
        'formacion-geologica': 'historia-geologica',
        'geodinamica-externa': 'procesos-geologicos',
        'placas-tectonicas': 'tectonica-placas',
        'tierra': 'conceptos-fundamentales'
    }
    
    for tag_actual, tag_sugerido in mapeo_migracion.items():
        count = counter_tags.get(tag_actual, 0)
        if count > 0:
            print(f"📝 #{tag_actual} ({count}) → #{tag_sugerido}")
    
    # 8. Estadísticas finales
    print("\n📈 ESTADÍSTICAS GENERALES")
    print("-" * 40)
    print(f"Total archivos procesados: {len(analizador.archivos_procesados)}")
    print(f"Total tags únicos: {len(counter_tags)}")
    print(f"Tags del sistema en uso: {sum(1 for tag in tags_estandar if counter_tags.get(tag, 0) > 0)}")
    print(f"Tags del sistema total: {len(tags_estandar)}")
    
    # Porcentaje de cumplimiento
    tags_sistema_usados = sum(1 for tag in tags_estandar if counter_tags.get(tag, 0) > 0)
    porcentaje = (tags_sistema_usados / len(tags_estandar)) * 100
    print(f"Cumplimiento del sistema: {porcentaje:.1f}%")
    
    return {
        'counter_tags': counter_tags,
        'tags_sistema': tags_sistema,
        'mapeo_migracion': mapeo_migracion,
        'tags_no_estandar': tags_no_estandar
    }

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--actualizar-indice":
        # Modo automático: actualizar índice general
        print("🔄 Actualizando estadísticas del índice general...")
        nuevo_bloque, stats = actualizar_indice_general()
        
        # Leer archivo actual del índice
        indice_path = "../index.md"
        try:
            with open(indice_path, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            # Buscar y reemplazar bloque de estadísticas
            import re
            patron = r'\*\*📊 Estadísticas actuales:\*\*.*?\*Última actualización:.*?\*'
            if re.search(patron, contenido, re.DOTALL):
                contenido_actualizado = re.sub(patron, nuevo_bloque, contenido, flags=re.DOTALL)
                
                # Escribir archivo actualizado
                with open(indice_path, 'w', encoding='utf-8') as f:
                    f.write(contenido_actualizado)
                
                print("✅ Índice general actualizado exitosamente")
                print(f"📊 Nuevas estadísticas:")
                print(f"   - Archivos: {stats['archivos_totales']}")
                print(f"   - Asignaturas: {stats['asignaturas_activas']}")
                print(f"   - Tags: {stats['tags_unicos']}")
                print(f"   - Cumplimiento: {stats['cumplimiento_sistema']}%")
            else:
                print("❌ No se encontró el bloque de estadísticas en el índice")
                
        except Exception as e:
            print(f"❌ Error actualizando índice: {e}")
    
    elif len(sys.argv) > 1 and sys.argv[1] == "--solo-stats":
        # Modo solo estadísticas
        stats = generar_estadisticas_indice()
        print("📊 ESTADÍSTICAS PARA ÍNDICE GENERAL")
        print("=" * 50)
        print(f"Archivos totales: {stats['archivos_totales']}")
        print(f"Asignaturas activas: {stats['asignaturas_activas']}")
        print(f"Tags únicos: {stats['tags_unicos']}")
        print(f"Cumplimiento sistema: {stats['cumplimiento_sistema']}%")
        print(f"Fecha actualización: {stats['fecha_actualizacion']}")
    
    else:
        # Modo análisis completo (original)
        resultado = analizar_cumplimiento()