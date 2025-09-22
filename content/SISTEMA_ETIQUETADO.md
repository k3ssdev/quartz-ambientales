#🏷️ Sistema de Etiquetado Semántico Compatible con Obsidian ##Estructura de Frontmatter Minimalista

```yaml
---
dg-publish: true
aliases: ["Alias1", "Alias2"]
---
``` ##Sistema de Tags Semánticos con ####Tags de Categoría
```markdown #clima-oceanografia #geomorfologia #rocas-minerales #tectonica-placas #historia-geologica #estructura-terrestre #procesos-geologicos #recursos-riesgos
``` ###Tags de Importancia
```markdown #importancia-5 #importancia-4 #importancia-3 #importancia-2 #importancia-1
``` ###Tags de Tipo de Proceso
```markdown #proceso-fundamental #proceso-dinamico #proceso-estructural #proceso-historico
``` ###Tags de Tipo de Concepto
```markdown #concepto-central #concepto-proceso #concepto-estructura #concepto-evento #concepto-personaje #concepto-herramienta
``` ###Tags de Nivel de Aprendizaje
```markdown #nivel-basico #nivel-intermedio #nivel-avanzado
``` ###Tags de Rutas de Aprendizaje
```markdown #ruta-fundamentos #ruta-procesos-dinamicos #ruta-materiales #ruta-tiempo-evolucion
``` ##Categorías Principales ###🌊 Clima y Oceanografía
- **Clave**: `clima-oceanografia`
- **Conceptos centrales**: cambio-climatico, oceanos, clima-global
- **Procesos**: ciclos-biogeoquimicos, dinamica-oceanica ###🏔️ Geomorfología
- **Clave**: `geomorfologia` 
- **Conceptos centrales**: relieve, cordilleras, valles
- **Procesos**: erosion, meteorizacion, modelado ###🪨 Rocas y Minerales
- **Clave**: `rocas-minerales`
- **Conceptos centrales**: rocas-igneas, rocas-sedimentarias, rocas-metamorficas
- **Procesos**: ciclo-rocas, cristalizacion ###🌍 Tectónica de Placas
- **Clave**: `tectonica-placas`
- **Conceptos centrales**: placas-tectonicas, subduccion, dorsales-oceanicas
- **Procesos**: orogenia, expansion-oceanica ###📚 Historia Geológica
- **Clave**: `historia-geologica`
- **Conceptos centrales**: tiempo-geologico, estratigrafia, paleontologia
- **Procesos**: datacion, evolucion ###🏗️ Estructura Terrestre
- **Clave**: `estructura-terrestre`
- **Conceptos centrales**: geosfera, capas-tierra
- **Procesos**: diferenciacion ###⚡ Procesos Geológicos
- **Clave**: `procesos-geologicos`
- **Conceptos centrales**: geodinamica-interna, geodinamica-externa
- **Procesos**: volcanismo, terremotos ###🎯 Conceptos Fundamentales
- **Clave**: `conceptos-fundamentales`
- **Conceptos centrales**: uniformismo, catastrofismo
- **Procesos**: metodo-cientifico ###⚠️ Recursos y Riesgos
- **Clave**: `recursos-riesgos`
- **Conceptos centrales**: riesgos-naturales, recursos-naturales
- **Procesos**: prevencion, mitigacion ##Niveles de Importancia

1. **Nivel 5**: Conceptos fundamentales más enlazados (Tierra, Tectónica de placas)
2. **Nivel 4**: Procesos centrales (Volcanismo, Terremotos, Fósiles)
3. **Nivel 3**: Estructuras importantes (Corteza, Manto, Núcleo)
4. **Nivel 2**: Conceptos especializados
5. **Nivel 1**: Detalles específicos ##Tipos de Proceso

- **fundamental**: Conceptos base (Tierra, Geología)
- **dinamico**: Procesos activos (Volcanismo, Erosión)
- **estructural**: Elementos de estructura (Capas, Placas)
- **historico**: Eventos temporales (Eras, Períodos) ##Tipos de Concepto

- **central**: Conceptos más importantes y enlazados
- **proceso**: Fenómenos dinámicos
- **estructura**: Elementos físicos
- **evento**: Sucesos temporales
- **personaje**: Científicos importantes
- **herramienta**: Métodos y técnicas ##Automatización de Secciones ###Enlaces Más Importantes
```python #Buscar archivos con #importancia-5 #importancia-4 #concepto-central #Ordenar por número de enlaces entrantes
``` ###Navegación por Categorías
```python #Agrupar por tags de categoría (#clima-oceanografia, etc.) #Contar enlaces internos/externos por categoría #Extraer #concepto-central como conceptos clave
``` ###Enlaces Bidireccionales Recomendados
```python #Detectar enlaces [[A]] ↔ [[B]] que aparecen en ambos archivos #Agrupar por categorías similares vs. diferentes
``` ###Rutas de Aprendizaje
```python #Usar tags #ruta-* y #nivel-* #Ordenar por #nivel-basico → #nivel-intermedio → #nivel-avanzado #Detectar prerequisites automáticamente por enlaces
``` ##Ejemplo de Archivo Mejorado (Compatible con Obsidian)

```markdown
---
dg-publish: true
aliases: ["Teoría de placas tectónicas", "Tectónica global"]
---

La **tectónica de placas** es la teoría científica moderna que explica la dinámica de la [[Litosfera]]. ##Ideas clave
- La [[Litosfera]] está fragmentada en [[Placas tectónicas]]
- Se mueven sobre la [[Astenosfera]]
- Explica [[Terremotos]], [[Volcanes]], [[Formación de montañas]] ##Enlaces relacionados
- [[Placas tectónicas]] - Fragmentos de litosfera
- [[Subducción]] - Proceso de hundimiento
- [[Orogenia]] - Formación de montañas

--- #tectonica-placas #importancia-5 #proceso-fundamental #concepto-central #nivel-intermedio #ruta-fundamentos #ruta-procesos-dinamicos
``` ##Ventajas del Sistema Obsidian-Friendly ###✅ **Compatible con Obsidian nativo**
- Tags aparecen en el tag panel
- Funciona con queries nativas de Obsidian
- Compatible con plugins populares ###✅ **Busquedas naturales**
```markdown
tag:#importancia-5
tag:#tectonica-placas
tag:#concepto-central AND tag:#nivel-basico
``` ###✅ **Graph view mejorado**
- Los tags se muestran como nodos
- Agrupación visual por categorías
- Filtrado por importancia/nivel ###✅ **Queries de Dataview**
```dataview
LIST
#clima-oceanografia #concepto-central #concepto-estructura #concepto-evento #concepto-herramienta #concepto-personaje #concepto-proceso #estructura-terrestre #geomorfologia #historia-geologica #importancia-1 #importancia-2 #importancia-3 #importancia-4 #importancia-5 #nivel- #nivel-avanzado #nivel-basico #nivel-intermedio #proceso-dinamico #proceso-estructural #proceso-fundamental #proceso-historico #recursos-riesgos #rocas-minerales #tectonica-placas
SORT file.mtime DESC
``` ###✅ **Frontmatter minimalista**
- Solo lo esencial: `dg-publish` y `aliases`
- Toda la semántica en tags
- Más fácil de mantener