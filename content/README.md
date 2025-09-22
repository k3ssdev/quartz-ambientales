# 🌿 Base de Conocimientos - Ciencias Ambientales UNED

Sistema automatizado de gestión de conocimientos para el Grado en Ciencias Ambientales, con etiquetado semántico compatible con Obsidian.

## 🧠 Metodología de Generación de Contenido

### **Proceso de Creación Asistida por IA**

Este vault se construye mediante una metodología híbrida que combina:

1. **📚 Fuente Principal**: Apuntes y materiales de estudio personales de las asignaturas UNED
2. **🤖 Procesamiento IA**: Modelos de resumen que estructuran y organizan el contenido de manera clara y precisa
3. **🔄 Expansión Dinámica**: Durante el proceso de estudio, la IA propone descripciones cortas y concisas para nuevos conceptos que van surgiendo

### **Flujo de Trabajo**
```
Apuntes Originales → IA Resumen/Estructura → Conceptos Organizados → Etiquetado Automático
                                    ↓
Estudio Activo → Nuevos Conceptos → IA Describe → Integración Semántica
```

### **Ventajas del Sistema**
- ✅ **Consistencia**: Descripciones uniformes y bien estructuradas
- ✅ **Completitud**: No se pierden conceptos importantes durante el estudio
- ✅ **Escalabilidad**: Fácil expansión a nuevas asignaturas
- ✅ **Interconexión**: Enlaces semánticos automáticos entre conceptos

## 📁 Estructura del Proyectoase de Conocimientos - Ciencias Ambientales UNED

Sistema automatizado de gestión de conocimientos para el Grado en Ciencias Ambientales, con etiquetado semántico compatible con Obsidian.

## 📁 Estructura del Proyecto

```
BASE_CONOCIMIENTOS/
├── Geología/              # Asignatura: Geología I (completada)
├── Índices/               # Índices organizados
│   ├── Geología.md        # Índice específico de Geología
│   └── Primero.md         # Índice del primer curso
├── scripts/               # Scripts de automatización
│   ├── analizador_obsidian.py
│   ├── analizar_cumplimiento.py
│   ├── generar_indice_obsidian.py
│   └── migrar_asignaturas.py
├── index.md           # Índice principal de todas las asignaturas
├── SISTEMA_ETIQUETADO.md  # Documentación del sistema de tags
└── README.md              # Este archivo
```

## 🎓 Sistema de Etiquetado por Asignaturas

### **Estructura de Tags**
```
#curso-cuatrimestre-asignatura
```

**Ejemplos:**
- `#primero-1-geologia-1` - Geología I (1er curso, 1er cuatrimestre)
- `#primero-2-geologia-2` - Geología II (1er curso, 2do cuatrimestre)
- `#segundo-1-ecologia-1` - Ecología I (2do curso, 1er cuatrimestre)
``` ###**Niveles de Aprendizaje**
```markdown #nivel-basico #Conceptos fundamentales #nivel-intermedio #Nivel estándar #nivel-avanzado #Conceptos especializados
``` ##📝 Ejemplo de Archivo con Tags

```markdown
---
dg-publish: true
aliases: ["Teoría de placas tectónicas"]
---

La **tectónica de placas** es la teoría científica moderna... ##Enlaces relacionados
- [[Placas tectónicas]] - Fragmentos de litosfera
- [[Subducción]] - Proceso de hundimiento

--- #tectonica-placas #importancia-5 #concepto-central #nivel-intermedio
``` ##🔍 Búsquedas en Obsidian ###**Por Importancia**
```
tag:#importancia-5
``` ###**Por Categoría**
```
tag:#tectonica-placas
``` ###**Combinadas**
```
tag:#concepto-central AND tag:#nivel-basico
``` ###**Dataview Queries**
```dataview
LIST
#clima-oceanografia #concepto-central #concepto-estructura #concepto-evento #concepto-proceso #estructura-terrestre #geomorfologia #historia-geologica #importancia-1 #importancia-2 #importancia-3 #importancia-4 #importancia-5 #nivel-avanzado #nivel-basico #nivel-intermedio #recursos-riesgos #rocas-minerales #tectonica-placas
SORT file.mtime DESC
``` ##✅ Ventajas del Sistema

- ✅ **Compatible 100% con Obsidian nativo**
- ✅ **Frontmatter minimalista** (solo aliases y dg-publish)
- ✅ **Tags aparecen en el panel lateral** de Obsidian
- ✅ **Búsquedas naturales** con el sistema de tags
- ✅ **Graph view mejorado** con filtros por tags
- ✅ **Compatible con plugins** populares de Obsidian
- ✅ **Generación automática** del Índice Temático
- ✅ **Escalable** - crece automáticamente con nuevos archivos
- ✅ **Asistencia IA continua** para mantener calidad y coherencia

## 🤝 Proceso de Colaboración con IA

### **Durante el Estudio**
1. **Identificación**: Encuentro un concepto nuevo en los materiales de estudio
2. **Contexto**: Proporciono el contexto del concepto a la IA
3. **Generación**: La IA crea una descripción clara, concisa y bien estructurada
4. **Integración**: Se añaden automáticamente los tags apropiados y enlaces relacionados
5. **Revisión**: Verifico que la descripción capture correctamente la esencia del concepto

### **Ejemplos de Colaboración**
- **Concepto nuevo**: "Subducción"
- **IA genera**: Definición + contexto geológico + ejemplos + enlaces a conceptos relacionados
- **Sistema añade**: Tags apropiados (#tectonica-placas, #proceso-dinamico, #importancia-4)
- **Resultado**: Concepto perfectamente integrado en la red de conocimientos

### **Beneficios de esta Metodología**
- 📝 **Descripciones consistentes** en estilo y profundidad
- 🔗 **Enlaces semánticos** automáticos entre conceptos relacionados
- 🎯 **Enfoque pedagógico** adaptado al nivel de cada concepto
- ⚡ **Rapidez** en la documentación de nuevos conceptos
- 🧠 **Retención mejorada** gracias a la estructura clara

## 🛠️ Instalación

1. **Clonar archivos** en la raíz de tu vault
2. **Instalar dependencias** de Python:
   ```bash
   pip install pyyaml
   ```
3. **Ejecutar migración** (opcional):
   ```bash
   python3 migrar_tags_obsidian.py
   ```
4. **Generar índice**:
   ```bash
   python3 generar_indice_obsidian.py
   ``` ##📊 Output del Sistema

El sistema genera automáticamente:

- 🔗 **Enlaces Más Importantes** (por número de enlaces entrantes)
- 📁 **Navegación por Categorías** (con métricas de conectividad)
- 🔄 **Enlaces Bidireccionales** (detectados automáticamente)
- 🎯 **Rutas de Aprendizaje** (basadas en tags y niveles)
- 🏷️ **Tags Más Populares** (estadísticas del vault)

---

*Sistema desarrollado para maximizar la compatibilidad con Obsidian*