#!/usr/bin/env python3
"""
Generador de Índice Temático Compatible con Obsidian
Usa el sistema nativo de tags de Obsidian para generar el índice automáticamente
"""

import os
from datetime import datetime
from analizador_obsidian import AnalizadorObsidian

class GeneradorIndiceObsidian:
    def __init__(self, vault_path):
        self.vault_path = vault_path
        self.analizador = AnalizadorObsidian(vault_path)
        self.analizador.procesar_directorio()
        self.estadisticas = self.analizador.generar_estadisticas()
        
        # Mapeo de categorías a iconos y nombres amigables
        self.categoria_info = {
            'clima-oceanografia': {'icono': '🌊', 'nombre': 'Clima y Oceanografía'},
            'geomorfologia': {'icono': '🏔️', 'nombre': 'Geomorfología'},
            'rocas-minerales': {'icono': '🪨', 'nombre': 'Rocas y Minerales'},
            'tectonica-placas': {'icono': '🌍', 'nombre': 'Tectónica de Placas'},
            'historia-geologica': {'icono': '📚', 'nombre': 'Historia Geológica'},
            'estructura-terrestre': {'icono': '🏗️', 'nombre': 'Estructura Terrestre'},
            'procesos-geologicos': {'icono': '⚡', 'nombre': 'Procesos Geológicos'},
            'conceptos-fundamentales': {'icono': '🎯', 'nombre': 'Conceptos Fundamentales'},
            'recursos-riesgos': {'icono': '⚠️', 'nombre': 'Recursos y Riesgos'}
        }
        
        # Información de asignaturas por curso
        self.asignaturas_info = {
            'primero-1-geologia-1': {'curso': '1º', 'cuatrimestre': '1C', 'nombre': 'Geología I', 'icono': '🗿'},
            'primero-2-geologia-2': {'curso': '1º', 'cuatrimestre': '2C', 'nombre': 'Geología II', 'icono': '🌋'},
            'primero-1-biologia-1': {'curso': '1º', 'cuatrimestre': '1C', 'nombre': 'Biología I', 'icono': '🧬'},
            'primero-2-biologia-2': {'curso': '1º', 'cuatrimestre': '2C', 'nombre': 'Biología II', 'icono': '🦠'},
            'primero-1-matematicas-1': {'curso': '1º', 'cuatrimestre': '1C', 'nombre': 'Matemáticas I', 'icono': '🔢'},
            'primero-2-matematicas-2': {'curso': '1º', 'cuatrimestre': '2C', 'nombre': 'Matemáticas II', 'icono': '📐'},
            'primero-1-fisica-ambiental': {'curso': '1º', 'cuatrimestre': '1C', 'nombre': 'Bases Físicas del Medio Ambiente', 'icono': '⚛️'},
            'primero-2-quimica-ambiental': {'curso': '1º', 'cuatrimestre': '2C', 'nombre': 'Bases Químicas del Medio Ambiente', 'icono': '🧪'},
            'primero-2-sig': {'curso': '1º', 'cuatrimestre': '2C', 'nombre': 'Sistemas de Información Geográfica', 'icono': '🗺️'},
            'primero-1-sociedad': {'curso': '1º', 'cuatrimestre': '1C', 'nombre': 'Medio Ambiente y Sociedad', 'icono': '👥'}
        }
    
    def filtrar_enlaces_problematicos(self, archivo_nombre):
        """Filtra archivos que no deberían aparecer como enlaces en el índice"""
        # Lista de archivos a excluir
        archivos_excluir = [
            'Índice Temático',
            'índice temático', 
            'Home',
            'home',
            'README',
            'readme',
            'Planning',
            'planning',
            'General'
        ]
        
        return archivo_nombre not in archivos_excluir
    
    def generar_seccion_enlaces_importantes(self):
        """Genera la sección de enlaces más importantes"""
        contenido = "## 🔗 Enlaces Más Importantes\n\n"
        
        # Obtener los conceptos más enlazados globalmente
        conceptos_mas_enlazados = self.estadisticas['conceptos_mas_enlazados']
        
        if conceptos_mas_enlazados:
            contenido += "### Conceptos Centrales\n"
            for i, (concepto, enlaces) in enumerate(conceptos_mas_enlazados[:5]):
                if self.filtrar_enlaces_problematicos(concepto):
                    contenido += f"- [[{concepto}]] - Concepto más enlazado ({enlaces} enlaces entrantes)\n"
            contenido += "\n"
        
        # Procesos fundamentales (archivos con tags de importancia alta)
        procesos_importantes = []
        for archivo, data in self.analizador.archivos_procesados.items():
            tags = data['tags']
            enlaces_entrantes = self.analizador.enlaces_entrantes[archivo]
            
            # Buscar archivos con tags de proceso y alta importancia
            if ('proceso-dinamico' in tags or 'proceso-fundamental' in tags) and enlaces_entrantes >= 3:
                procesos_importantes.append((archivo, enlaces_entrantes))
        
        # Ordenar por enlaces entrantes
        procesos_importantes.sort(key=lambda x: x[1], reverse=True)
        
        if procesos_importantes:
            contenido += "### Procesos Fundamentales\n"
            for concepto, enlaces in procesos_importantes[:5]:
                if self.filtrar_enlaces_problematicos(concepto):
                    contenido += f"- [[{concepto}]] - Proceso dinámico central\n"
            contenido += "\n"
        
        # Estructura terrestre (archivos con tags de estructura)
        estructuras_importantes = []
        for archivo, data in self.analizador.archivos_procesados.items():
            tags = data['tags']
            enlaces_entrantes = self.analizador.enlaces_entrantes[archivo]
            
            if ('concepto-estructura' in tags or 'estructura-terrestre' in tags) and enlaces_entrantes >= 3:
                estructuras_importantes.append((archivo, enlaces_entrantes))
        
        estructuras_importantes.sort(key=lambda x: x[1], reverse=True)
        
        if estructuras_importantes:
            contenido += "### Estructura Terrestre\n"
            for concepto, enlaces in estructuras_importantes[:5]:
                if self.filtrar_enlaces_problematicos(concepto):
                    contenido += f"- [[{concepto}]] - Elemento estructural\n"
            contenido += "\n"
        
        return contenido
    
    def generar_seccion_navegacion_categorias(self):
        """Genera la sección de navegación por categorías"""
        contenido = "## 📁 Navegación por Categorías\n\n"
        
        # Filtrar categoría sin-categoria y ordenar por número de archivos
        categorias_validas = {k: v for k, v in self.estadisticas['categorias'].items() 
                            if k != 'sin-categoria' and len(v['archivos']) > 0}
        
        categorias_ordenadas = sorted(
            categorias_validas.items(),
            key=lambda x: len(x[1]['archivos']),
            reverse=True
        )
        
        for categoria, datos in categorias_ordenadas:
            info = self.categoria_info.get(categoria, {'icono': '📂', 'nombre': categoria.replace('-', ' ').title()})
            
            contenido += f"### {info['icono']} {info['nombre']} ({len(datos['archivos'])} archivos)\n"
            contenido += f"- Enlaces internos: {datos['enlaces_internos']} | Enlaces externos: {datos['enlaces_externos']}\n"
            
            # Conceptos clave de esta categoría usando el sistema de tags
            conceptos_categoria = []
            for archivo in datos['archivos']:
                data = self.analizador.archivos_procesados[archivo]
                enlaces_entrantes = self.analizador.enlaces_entrantes[archivo]
                tags = data['tags']
                
                # Incluir si tiene tag de concepto central, alta importancia o muchos enlaces
                if ('concepto-central' in tags or 
                    any(tag.startswith('importancia-') and int(tag.split('-')[1]) >= 4 for tag in tags if tag.startswith('importancia-')) or
                    enlaces_entrantes >= 5):
                    conceptos_categoria.append((archivo, enlaces_entrantes))
            
            # Ordenar por enlaces entrantes y tomar los top 3
            conceptos_categoria.sort(key=lambda x: x[1], reverse=True)
            
            if conceptos_categoria:
                conceptos_str = ", ".join([f"[[{nombre}]]" for nombre, _ in conceptos_categoria[:3]])
                contenido += f"- Conceptos clave: {conceptos_str}\n"
            
            contenido += "\n"
        
        return contenido
    
    def generar_seccion_asignaturas(self):
        """Genera la sección de organización por asignaturas"""
        contenido = "## 🎓 Organización por Asignaturas\n\n"
        
        # Contar archivos por asignatura
        asignaturas_archivos = {}
        
        for archivo, data in self.analizador.archivos_procesados.items():
            tags = data['tags']
            for tag in tags:
                if tag in self.asignaturas_info:
                    if tag not in asignaturas_archivos:
                        asignaturas_archivos[tag] = []
                    asignaturas_archivos[tag].append(archivo)
        
        # Organizar por curso y cuatrimestre
        cursos = {}
        for tag_asig, archivos in asignaturas_archivos.items():
            if tag_asig in self.asignaturas_info:
                info = self.asignaturas_info[tag_asig]
                curso = info['curso']
                cuatrimestre = info['cuatrimestre']
                
                if curso not in cursos:
                    cursos[curso] = {}
                if cuatrimestre not in cursos[curso]:
                    cursos[curso][cuatrimestre] = []
                
                cursos[curso][cuatrimestre].append({
                    'tag': tag_asig,
                    'info': info,
                    'archivos': archivos
                })
        
        # Generar contenido por curso
        for curso in sorted(cursos.keys()):
            contenido += f"### 📚 {curso} Curso\n\n"
            
            for cuatrimestre in sorted(cursos[curso].keys()):
                contenido += f"#### {cuatrimestre} - {cuatrimestre.replace('C', '° Cuatrimestre')}\n\n"
                
                for asignatura in cursos[curso][cuatrimestre]:
                    info = asignatura['info']
                    archivos = asignatura['archivos']
                    icono = info['icono']
                    nombre = info['nombre']
                    
                    # Calcular métricas
                    enlaces_totales = sum(self.analizador.enlaces_entrantes[arch] for arch in archivos)
                    conceptos_importantes = [arch for arch in archivos 
                                           if self.analizador.enlaces_entrantes[arch] >= 3]
                    
                    contenido += f"**{icono} {nombre}** ({len(archivos)} conceptos)\n"
                    contenido += f"- Enlaces entrantes: {enlaces_totales}\n"
                    contenido += f"- Conceptos destacados: {len(conceptos_importantes)}\n"
                    
                    if conceptos_importantes[:3]:
                        conceptos_str = ", ".join([f"[[{arch}]]" for arch in conceptos_importantes[:3]])
                        contenido += f"- Principales: {conceptos_str}\n"
                    
                    contenido += "\n"
        
        return contenido

    def generar_seccion_enlaces_bidireccionales(self):
        """Genera la sección de enlaces bidireccionales"""
        contenido = "## 🔄 Enlaces Bidireccionales Recomendados\n\n"
        
        # Agrupar por tipo de conexión usando categorías
        conexiones_tematicas = []
        conexiones_procesales = []
        
        enlaces_bi = self.estadisticas['enlaces_bidireccionales']
        
        for archivo1, archivo2 in enlaces_bi:
            if archivo1 in self.analizador.archivos_procesados and archivo2 in self.analizador.archivos_procesados:
                cat1 = self.analizador.archivos_procesados[archivo1]['categoria']
                cat2 = self.analizador.archivos_procesados[archivo2]['categoria']
                
                if cat1 == cat2:
                    conexiones_tematicas.append((archivo1, archivo2))
                else:
                    conexiones_procesales.append((archivo1, archivo2))
        
        if conexiones_tematicas:
            contenido += "### Conexiones Temáticas Fuertes\n"
            for arch1, arch2 in conexiones_tematicas[:5]:
                contenido += f"- [[{arch1}]] ↔ [[{arch2}]]\n"
            contenido += "\n"
        
        if conexiones_procesales:
            contenido += "### Conexiones Procesales\n"
            for arch1, arch2 in conexiones_procesales[:5]:
                contenido += f"- [[{arch1}]] ↔ [[{arch2}]]\n"
            contenido += "\n"
        
        return contenido
    
    def generar_seccion_rutas_aprendizaje(self):
        """Genera la sección de rutas de aprendizaje"""
        contenido = "## 🎯 Rutas de Aprendizaje\n\n"
        
        # Usar rutas explícitas de tags si existen
        rutas_tags = self.estadisticas['rutas_aprendizaje']
        
        if rutas_tags:
            for nombre_ruta, archivos_ruta in rutas_tags.items():
                contenido += f"### Ruta: {nombre_ruta.replace('-', ' ').title()}\n"
                for i, archivo_info in enumerate(archivos_ruta[:5], 1):
                    archivo = archivo_info['archivo']
                    nivel = archivo_info['nivel']
                    contenido += f"{i}. [[{archivo}]] ({nivel})\n"
                contenido += "\n"
        
        # Generar rutas automáticas basadas en conceptos más enlazados y tags
        conceptos_mas_enlazados = [concepto for concepto, _ in self.estadisticas['conceptos_mas_enlazados']]
        
        # Ruta 1: Fundamentos
        fundamentos = []
        for archivo, data in self.analizador.archivos_procesados.items():
            tags = data['tags']
            if ('concepto-central' in tags and 'nivel-basico' in tags) or archivo in ['Tierra', 'Geología']:
                fundamentos.append(archivo)
        
        if not fundamentos:  # Si no hay tags específicos, usar conceptos más enlazados
            palabras_fundamento = ['tierra', 'geología', 'tiempo geológico']
            fundamentos = [c for c in conceptos_mas_enlazados if any(p in c.lower() for p in palabras_fundamento)][:3]
        
        if fundamentos:
            contenido += "### Ruta 1: Fundamentos\n"
            contenido += f"1. {' → '.join([f'[[{f}]]' for f in fundamentos[:3]])}\n\n"
        
        # Ruta 2: Procesos Dinámicos
        dinamicos = []
        for archivo, data in self.analizador.archivos_procesados.items():
            tags = data['tags']
            if 'proceso-dinamico' in tags and archivo in conceptos_mas_enlazados[:20]:
                dinamicos.append(archivo)
        
        if not dinamicos:
            palabras_dinamico = ['tectónica', 'volcanismo', 'terremotos']
            dinamicos = [c for c in conceptos_mas_enlazados if any(p in c.lower() for p in palabras_dinamico)][:3]
        
        if dinamicos:
            contenido += "### Ruta 2: Procesos Dinámicos\n"
            contenido += f"1. {' → '.join([f'[[{d}]]' for d in dinamicos[:3]])}\n\n"
        
        # Ruta 3: Materiales
        materiales = []
        for archivo, data in self.analizador.archivos_procesados.items():
            tags = data['tags']
            if 'rocas-minerales' in tags and archivo in conceptos_mas_enlazados[:20]:
                materiales.append(archivo)
        
        if not materiales:
            palabras_material = ['rocas', 'minerales', 'ciclo']
            materiales = [c for c in conceptos_mas_enlazados if any(p in c.lower() for p in palabras_material)][:3]
        
        if materiales:
            contenido += "### Ruta 3: Materiales\n"
            contenido += f"1. {' → '.join([f'[[{m}]]' for m in materiales[:3]])}\n\n"
        
        return contenido
    
    def generar_seccion_tags_populares(self):
        """Genera una sección con los tags más populares"""
        contenido = "## 🏷️ Tags Más Utilizados\n\n"
        
        tags_populares = self.estadisticas['tags_mas_usados']
        
        if tags_populares:
            contenido += "### Top Tags del Vault\n"
            for tag, count in tags_populares[:15]:
                contenido += f"- `#{tag}` ({count} archivos)\n"
            contenido += "\n"
        
        return contenido
    
    def generar_indice_completo(self):
        """Genera el índice temático completo"""
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        contenido = f"""---
title: "Índice Temático - Geología"
tags:
  - navegacion
  - sistema-enlaces
  - mapa-conceptual
  - herramienta
  - obsidian
---

# 📚 Índice Temático

{self.generar_seccion_enlaces_importantes()}

{self.generar_seccion_navegacion_categorias()}

{self.generar_seccion_asignaturas()}

{self.generar_seccion_enlaces_bidireccionales()}

{self.generar_seccion_rutas_aprendizaje()}

{self.generar_seccion_tags_populares()}

---

*Sistema generado automáticamente basado en análisis de tags de Obsidian*
*Última actualización: {fecha_actual}*
"""
        
        return contenido
    
    def guardar_indice(self, nombre_archivo="Geología.md", directorio="../Índices"):
        """Guarda el índice generado en un archivo"""
        ruta_directorio = os.path.join(os.path.dirname(self.vault_path), directorio.lstrip('../'))
        ruta_completa = os.path.join(ruta_directorio, nombre_archivo)
        contenido = self.generar_indice_completo()
        
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(ruta_completa), exist_ok=True)
        
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            f.write(contenido)
        
        print(f"Índice temático generado en: {ruta_completa}")
        print(f"Total archivos procesados: {self.estadisticas['total_archivos']}")
        print(f"Total categorías: {len([k for k in self.estadisticas['categorias'].keys() if k != 'sin-categoria'])}")
        print(f"Enlaces bidireccionales encontrados: {len(self.estadisticas['enlaces_bidireccionales'])}")
        print(f"Tags únicos encontrados: {len(self.estadisticas['tags_mas_usados'])}")
        
        return ruta_completa

def main():
    vault_path = "../Geología"
    generador = GeneradorIndiceObsidian(vault_path)
    generador.guardar_indice()

if __name__ == "__main__":
    main()