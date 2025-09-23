---
title: "Sistema de Etiquetado Semantico"
aliases: ["Sistema de Etiquetado Semántico"]
weight: 3
tags:
  - documentacion
  - sistema-etiquetado
  - metodologia
  - tags
  - organizacion
---
## Estructura de Frontmatter

```yaml
---
title: "Título del concepto"
aliases: ["Alias1", "Alias2"]
tags:
  - categoria-principal
  - importancia-X
  - nivel-X
  - concepto-tipo
---
```

## Sistema de Tags Semánticos

### Tags de Categoría
```markdown
- clima-oceanografia
- geomorfologia  
- rocas-minerales
- tectonica-placas
- historia-geologica
- estructura-terrestre
- procesos-geologicos
- recursos-riesgos
```

### Tags de Importancia
```markdown
- importancia-5  # Crítico
- importancia-4  # Muy importante
- importancia-3  # Importante
- importancia-2  # Moderado
- importancia-1  # Básico
```

### Tags de Tipo de Proceso
```markdown
- proceso-fundamental
- proceso-dinamico
- proceso-estructural
- proceso-historico
```

### Tags de Tipo de Concepto
```markdown
- concepto-central
- concepto-proceso
- concepto-estructura
- concepto-evento
- concepto-personaje
- concepto-herramienta
```

### Tags de Nivel de Aprendizaje
```markdown
- nivel-basico
- nivel-intermedio
- nivel-avanzado
```

### Tags de Rutas de Aprendizaje
```markdown
- ruta-fundamentos
- ruta-procesos-dinamicos
- ruta-materiales
- ruta-tiempo-evolucion
```

## Categorías Principales

### 🌊 Clima y Oceanografía
- **Clave**: `clima-oceanografia`
- **Conceptos centrales**: cambio-climatico, oceanos, clima-global
- **Procesos**: ciclos-biogeoquimicos, dinamica-oceanica

### 🏔️ Geomorfología
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
- **herramienta**: Métodos y técnicas

## Automatización de Secciones

### Enlaces Más Importantes
```python
# Buscar archivos con #importancia-5 #importancia-4 #concepto-central
# Ordenar por número de enlaces entrantes
```

### Navegación por Categorías
```python
# Agrupar por tags de categoría (#clima-oceanografia, etc.)
# Contar enlaces internos/externos por categoría
# Extraer #concepto-central como conceptos clave
```

### Enlaces Bidireccionales Recomendados
```python
# Detectar enlaces [[A]] ↔ [[B]] que aparecen en ambos archivos
# Agrupar por categorías similares vs. diferentes
```

### Rutas de Aprendizaje
```python
# Usar tags #ruta-* y #nivel-*
# Ordenar por #nivel-basico → #nivel-intermedio → #nivel-avanzado
# Detectar prerequisites automáticamente por enlaces
```

## Ejemplo de Archivo Mejorado (Compatible con Quartz)

```markdown
---
title: "Tectónica de placas"
aliases: ["Teoría de placas tectónicas", "Tectónica global"]
tags:
  - tectonica-placas
  - importancia-5
  - concepto-central
  - nivel-intermedio
  - ruta-fundamentos
---

La **tectónica de placas** es la teoría científica moderna que explica la dinámica de la [[Litosfera]].

## Ideas clave
- La [[Litosfera]] está fragmentada en [[Placas tectónicas]]
- Se mueven sobre la [[Astenosfera]]
- Explica [[Terremotos]], [[Volcanes]], [[Formación de montañas]]

## Enlaces relacionados
- [[Placas tectónicas]] - Fragmentos de litosfera
- [[Subducción]] - Proceso de hundimiento
- [[Orogenia]] - Formación de montañas
```

## Ventajas del Sistema Compatible con Quartz

### ✅ **Frontmatter estructurado**
- Metadatos claros: `title`, `aliases` y `tags`
- Tags organizados en formato YAML
- Fácil de mantener y expandir

### ✅ **Búsquedas naturales**
Utiliza el explorador de etiquetas de Quartz para filtrar por:
- Importancia: `importancia-5`
- Categoría: `tectonica-placas`
- Nivel: `nivel-basico`

### ✅ **Navegación mejorada**
- Enlaces bidireccionales automáticos
- Renderizado web estático
- Búsqueda de texto completo integrada

### ✅ **Compatible con automatización**
- Scripts Python para análisis de tags
- Generación automática de índices
- Estadísticas de contenido

---

*Sistema optimizado para Quartz - Generación estática de sitios web*