#!/usr/bin/env python3
"""
Analizador Compatible con Tags de Obsidian
Procesa archivos usando el sistema nativo de tags de Obsidian (#tag)
"""

import os
import re
import yaml
from collections import Counter, defaultdict
from pathlib import Path

class AnalizadorObsidian:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.archivos_procesados = {}
        self.enlaces_entrantes = Counter()
        self.enlaces_salientes = defaultdict(list)
        self.tags_por_archivo = defaultdict(set)
        self.categorias = defaultdict(lambda: {'archivos': [], 'enlaces_internos': 0, 'enlaces_externos': 0})
        
        # Mapeo de tags a categorías
        self.categorias_tags = {
            'clima-oceanografia': 'clima-oceanografia',
            'geomorfologia': 'geomorfologia', 
            'rocas-minerales': 'rocas-minerales',
            'tectonica-placas': 'tectonica-placas',
            'historia-geologica': 'historia-geologica',
            'estructura-terrestre': 'estructura-terrestre',
            'procesos-geologicos': 'procesos-geologicos',
            'conceptos-fundamentales': 'conceptos-fundamentales',
            'recursos-riesgos': 'recursos-riesgos'
        }
        
        # Tags de asignatura por curso-cuatrimestre
        self.asignaturas_tags = {
            # Primer curso
            'primero-1-geologia-1': 'Geología I',
            'primero-2-geologia-2': 'Geología II',
            'primero-1-biologia-1': 'Biología I',
            'primero-2-biologia-2': 'Biología II',
            'primero-1-matematicas-1': 'Matemáticas I',
            'primero-2-matematicas-2': 'Matemáticas II',
            'primero-1-fisica-ambiental': 'Bases Físicas del Medio Ambiente',
            'primero-2-quimica-ambiental': 'Bases Químicas del Medio Ambiente',
            'primero-2-sig': 'Sistemas de Información Geográfica',
            'primero-1-sociedad': 'Medio Ambiente y Sociedad',
            
            # Segundo curso
            'segundo-1-estadistica': 'Estadística Aplicada al Medio Ambiente',
            'segundo-1-contaminantes': 'Origen y Control de los Contaminantes',
            'segundo-1-diversidad-vegetal': 'Diversidad Vegetal',
            'segundo-2-diversidad-animal': 'Diversidad Animal',
            'segundo-1-ecologia-1': 'Ecología I',
            'segundo-2-ecologia-2': 'Ecología II',
            'segundo-1-administracion': 'Administración y Legislación Ambiental',
            'segundo-1-agentes-fisicos': 'Contaminación por Agentes Físicos',
            'segundo-2-instrumentales': 'Técnicas Instrumentales',
            'segundo-2-economia-ambiental': 'Economía Ambiental',
            'segundo-2-ingenieria-ambiental': 'Bases de la Ingeniería Ambiental',
            'segundo-2-meteorologia': 'Meteorología y Climatología'
        }
        
    def extraer_frontmatter(self, contenido):
        """Extrae y parsea el frontmatter YAML"""
        match = re.match(r'^---\n(.*?)\n---', contenido, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except yaml.YAMLError:
                return {}
        return {}
    
    def extraer_tags_obsidian(self, contenido):
        """Extrae todos los tags de Obsidian (#tag) del contenido"""
        # Tags inline en el contenido
        tags_inline = set(re.findall(r'#([\w-]+)', contenido))
        
        # Tags en el frontmatter
        frontmatter = self.extraer_frontmatter(contenido)
        tags_fm = set()
        if 'tags' in frontmatter:
            if isinstance(frontmatter['tags'], list):
                tags_fm.update(frontmatter['tags'])
            elif isinstance(frontmatter['tags'], str):
                tags_fm.add(frontmatter['tags'])
        
        return tags_inline.union(tags_fm)
    
    def extraer_enlaces_wiki(self, contenido):
        """Extrae enlaces tipo [[Enlace]] del contenido"""
        patron = r'\[\[([^\]]+)\]\]'
        enlaces = re.findall(patron, contenido)
        enlaces_limpios = []
        for enlace in enlaces:
            if '|' in enlace:
                enlace = enlace.split('|')[0]
            enlaces_limpios.append(enlace.strip())
        return enlaces_limpios
    
    def determinar_categoria_por_tags(self, tags):
        """Determina la categoría principal basándose en los tags"""
        for tag in tags:
            if tag in self.categorias_tags:
                return self.categorias_tags[tag]
        return 'sin-categoria'
    
    def determinar_categoria_por_ubicacion(self, ruta_archivo):
        """Infiere la categoría basándose en la ubicación del archivo"""
        ruta_str = str(ruta_archivo).lower()
        
        if 'clima y oceanografía' in ruta_str or 'clima' in ruta_str:
            return 'clima-oceanografia'
        elif 'geomorfología' in ruta_str:
            return 'geomorfologia'
        elif 'rocas y minerales' in ruta_str or 'rocas' in ruta_str or 'minerales' in ruta_str:
            return 'rocas-minerales'
        elif 'tectónica de placas' in ruta_str or 'tectonica' in ruta_str:
            return 'tectonica-placas'
        elif 'historia geológica' in ruta_str or 'historia' in ruta_str:
            return 'historia-geologica'
        elif 'estructura terrestre' in ruta_str or 'estructura' in ruta_str:
            return 'estructura-terrestre'
        elif 'procesos geológicos' in ruta_str or 'procesos' in ruta_str:
            return 'procesos-geologicos'
        elif 'conceptos fundamentales' in ruta_str or 'fundamentales' in ruta_str:
            return 'conceptos-fundamentales'
        elif 'recursos y riesgos' in ruta_str or 'recursos' in ruta_str or 'riesgos' in ruta_str:
            return 'recursos-riesgos'
        elif 'organismos' in ruta_str or 'paleontología' in ruta_str:
            return 'historia-geologica'
        else:
            return 'sin-categoria'
    
    def extraer_importancia_de_tags(self, tags):
        """Extrae el nivel de importancia de los tags"""
        for tag in tags:
            if tag.startswith('importancia-'):
                try:
                    return int(tag.split('-')[1])
                except ValueError:
                    continue
        return 2  # Importancia por defecto
    
    def tiene_tag_tipo(self, tags, tipo):
        """Verifica si el archivo tiene un tag de cierto tipo"""
        return any(tag.startswith(f'{tipo}-') or tag == tipo for tag in tags)
    
    def procesar_archivo(self, ruta_archivo):
        """Procesa un archivo markdown individual"""
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            # Extraer tags de Obsidian
            tags = self.extraer_tags_obsidian(contenido)
            
            # Extraer metadatos básicos
            frontmatter = self.extraer_frontmatter(contenido)
            
            # Determinar categoría
            categoria = self.determinar_categoria_por_tags(tags)
            if categoria == 'sin-categoria':
                categoria = self.determinar_categoria_por_ubicacion(ruta_archivo)
            
            # Extraer enlaces
            enlaces = self.extraer_enlaces_wiki(contenido)
            
            # Nombre del archivo sin extensión
            nombre_archivo = ruta_archivo.stem
            
            # Almacenar información
            self.archivos_procesados[nombre_archivo] = {
                'ruta': ruta_archivo,
                'frontmatter': frontmatter,
                'tags': tags,
                'categoria': categoria,
                'enlaces_salientes': enlaces,
                'contenido_length': len(contenido),
                'importancia': self.extraer_importancia_de_tags(tags),
                'es_central': self.tiene_tag_tipo(tags, 'concepto-central'),
                'nivel': self.extraer_nivel_de_tags(tags)
            }
            
            # Almacenar tags por archivo
            self.tags_por_archivo[nombre_archivo] = tags
            
            # Contar enlaces entrantes
            for enlace in enlaces:
                self.enlaces_entrantes[enlace] += 1
                self.enlaces_salientes[nombre_archivo].append(enlace)
            
            # Procesar metadatos por categoría
            self.categorias[categoria]['archivos'].append(nombre_archivo)
            self.categorias[categoria]['enlaces_externos'] += len(enlaces)
            
            return True
            
        except Exception as e:
            print(f"Error procesando {ruta_archivo}: {e}")
            return False
    
    def extraer_nivel_de_tags(self, tags):
        """Extrae el nivel de aprendizaje de los tags"""
        for tag in tags:
            if tag.startswith('nivel-'):
                return tag.split('-')[1]
        return 'intermedio'  # Nivel por defecto
    
    def extraer_asignatura_de_tags(self, tags):
        """Extrae información de asignatura de los tags"""
        for tag in tags:
            if tag in self.asignaturas_tags:
                return {
                    'tag': tag,
                    'nombre': self.asignaturas_tags[tag],
                    'curso': tag.split('-')[0],
                    'cuatrimestre': tag.split('-')[1] if len(tag.split('-')) > 1 else '1'
                }
        return None

    def procesar_directorio(self, directorio=None):
        """Procesa todos los archivos .md en el directorio"""
        if directorio is None:
            directorio = self.vault_path
        
        archivos_md = list(Path(directorio).rglob("*.md"))
        
        # Filtrar archivos de índices y archivos que no sean conceptos
        archivos_filtrados = []
        for archivo in archivos_md:
            # Excluir archivos en carpetas de índices
            if 'Índices' in str(archivo) or 'índices' in str(archivo):
                continue
            # Excluir archivos específicos como home.md, README.md, etc.
            nombre_archivo = archivo.name.lower()
            if nombre_archivo in ['home.md', 'readme.md', 'planning.md', 'índice temático.md']:
                continue
            archivos_filtrados.append(archivo)
        
        print(f"Procesando {len(archivos_filtrados)} archivos...")
        
        for archivo in archivos_filtrados:
            self.procesar_archivo(archivo)
        
        # Calcular enlaces internos
        self._calcular_enlaces_internos()
    
    def _calcular_enlaces_internos(self):
        """Calcula enlaces internos después de procesar todos los archivos"""
        for categoria in self.categorias:
            self.categorias[categoria]['enlaces_internos'] = 0
        
        for nombre_archivo, data in self.archivos_procesados.items():
            categoria = data['categoria']
            enlaces_internos = 0
            
            for enlace in data['enlaces_salientes']:
                if enlace in self.archivos_procesados:
                    enlace_categoria = self.archivos_procesados[enlace]['categoria']
                    if enlace_categoria == categoria:
                        enlaces_internos += 1
            
            self.categorias[categoria]['enlaces_internos'] += enlaces_internos
    
    def obtener_conceptos_centrales_por_categoria(self, limite=3):
        """Obtiene conceptos centrales por categoría"""
        conceptos_por_categoria = defaultdict(list)
        
        for nombre, data in self.archivos_procesados.items():
            categoria = data['categoria']
            enlaces_entrantes = self.enlaces_entrantes[nombre]
            importancia = data['importancia']
            es_central = data['es_central']
            
            # Incluir si es central explícitamente, tiene alta importancia o muchos enlaces
            if es_central or importancia >= 4 or enlaces_entrantes >= 5:
                conceptos_por_categoria[categoria].append({
                    'nombre': nombre,
                    'enlaces_entrantes': enlaces_entrantes,
                    'importancia': importancia,
                    'es_central': es_central
                })
        
        # Ordenar y limitar por categoría
        for categoria in conceptos_por_categoria:
            conceptos_por_categoria[categoria].sort(
                key=lambda x: (x['es_central'], x['enlaces_entrantes'], x['importancia']), 
                reverse=True
            )
            conceptos_por_categoria[categoria] = conceptos_por_categoria[categoria][:limite]
        
        return conceptos_por_categoria
    
    def obtener_enlaces_bidireccionales(self):
        """Detecta enlaces bidireccionales automáticamente"""
        bidireccionales = []
        
        for archivo1, data1 in self.archivos_procesados.items():
            for enlace in data1['enlaces_salientes']:
                if enlace in self.archivos_procesados:
                    data2 = self.archivos_procesados[enlace]
                    # Si el archivo enlazado también enlaza de vuelta
                    if archivo1 in data2['enlaces_salientes']:
                        # Evitar duplicados
                        par = tuple(sorted([archivo1, enlace]))
                        if par not in bidireccionales:
                            bidireccionales.append(par)
        
        return bidireccionales
    
    def obtener_rutas_aprendizaje(self):
        """Genera rutas de aprendizaje basadas en tags"""
        rutas = defaultdict(list)
        
        for archivo, data in self.archivos_procesados.items():
            tags = data['tags']
            nivel = data['nivel']
            
            # Buscar tags de rutas
            for tag in tags:
                if tag.startswith('ruta-'):
                    nombre_ruta = tag[5:]  # Quitar 'ruta-'
                    rutas[nombre_ruta].append({
                        'archivo': archivo,
                        'nivel': nivel,
                        'importancia': data['importancia']
                    })
        
        # Ordenar rutas por nivel e importancia
        orden_nivel = {'basico': 1, 'intermedio': 2, 'avanzado': 3}
        
        for ruta in rutas:
            rutas[ruta].sort(key=lambda x: (orden_nivel.get(x['nivel'], 2), -x['importancia']))
        
        return rutas
    
    def generar_estadisticas(self):
        """Genera estadísticas completas del sistema"""
        return {
            'total_archivos': len(self.archivos_procesados),
            'total_enlaces': sum(len(data['enlaces_salientes']) for data in self.archivos_procesados.values()),
            'conceptos_mas_enlazados': self.enlaces_entrantes.most_common(20),
            'categorias': dict(self.categorias),
            'conceptos_centrales': self.obtener_conceptos_centrales_por_categoria(),
            'enlaces_bidireccionales': self.obtener_enlaces_bidireccionales(),
            'rutas_aprendizaje': self.obtener_rutas_aprendizaje(),
            'tags_mas_usados': Counter([tag for tags in self.tags_por_archivo.values() for tag in tags]).most_common(30)
        }

def main():
    vault_path = "../Geología"
    analizador = AnalizadorObsidian(vault_path)
    analizador.procesar_directorio()
    
    estadisticas = analizador.generar_estadisticas()
    
    print("=== ESTADÍSTICAS DE OBSIDIAN VAULT ===")
    print(f"Total archivos procesados: {estadisticas['total_archivos']}")
    print(f"Total enlaces encontrados: {estadisticas['total_enlaces']}")
    
    print("\n=== CONCEPTOS MÁS ENLAZADOS ===")
    for concepto, enlaces in estadisticas['conceptos_mas_enlazados'][:10]:
        print(f"- {concepto}: {enlaces} enlaces entrantes")
    
    print("\n=== TAGS MÁS USADOS ===")
    for tag, count in estadisticas['tags_mas_usados'][:15]:
        print(f"- #{tag}: {count} archivos")
    
    return estadisticas

if __name__ == "__main__":
    stats = main()