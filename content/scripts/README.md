---
title: "Scripts de Automatización"
weight: 60
draft: true
tags:
  - scripts
  - automatizacion
  - herramientas
  - python
  - documentacion
---

# 🛠️ Scripts de Automatización - Base de Conocimientos UNED

Este directorio contiene los scripts de Python para automatizar el mantenimiento y análisis de la base de conocimientos de Ciencias Ambientales.

## 📜 Scripts Disponibles

### 1. `analisis_contenido.py`
**Análisis completo del contenido y estadísticas automáticas**

```bash
# Análisis completo del sistema
python3 analisis_contenido.py

# Solo estadísticas para el índice
python3 analisis_contenido.py --solo-stats

# Actualizar automáticamente el índice general
python3 analisis_contenido.py --actualizar-indice
```

**Funciones:**
- ✅ Análisis de cumplimiento del sistema de etiquetado
- 📊 Generación de estadísticas automáticas
- 🔄 Actualización automática del índice general
- 🏷️ Validación de tags por categorías y asignaturas

### 2. `actualizar_estadisticas.py`
**Interfaz simplificada para actualización de estadísticas**

```bash
# Menú interactivo
python3 actualizar_estadisticas.py

# Solo ver estadísticas
python3 actualizar_estadisticas.py --stats

# Actualizar índice automáticamente
python3 actualizar_estadisticas.py --update

# Análisis completo
python3 actualizar_estadisticas.py --full
```

**Características:**
- 🎮 Menú interactivo amigable
- ⚡ Comandos rápidos por línea de comandos
- 🔄 Integración con `analisis_contenido.py`
- ✅ Confirmación de actualizaciones

### 3. `generar_indice_obsidian.py`
**Generación automática de índices por asignatura**

```bash
python3 generar_indice_obsidian.py
```

**Funciones:**
- 📚 Genera índices organizados por curso y asignatura
- 🏷️ Organización automática por categorías
- ⭐ Destaca conceptos centrales e importantes
- 🔗 Manejo automático de enlaces bidireccionales

### 4. `migrar_asignaturas.py`
**Migración masiva de tags de asignatura**

```bash
python3 migrar_asignaturas.py
```

**Propósito:**
- 🏷️ Añade tags de asignatura (#primero-1-geologia-1) a archivos existentes
- 📁 Procesa archivos en masa manteniendo estructura existente
- ✅ Validación antes de aplicar cambios
- 📊 Reporte detallado de migración

### 5. `analizador_obsidian.py`
**Motor de análisis core del sistema**

Este es el módulo base utilizado por los otros scripts. Contiene:
- 🔍 Análisis de archivos markdown de Obsidian
- 🏷️ Extracción de tags y metadatos
- 🔗 Análisis de enlaces y relaciones
- 📊 Generación de estadísticas base

## 📊 Flujo de Trabajo Recomendado

### Uso Diario
1. **Ver estadísticas actuales:**
   ```bash
   python3 actualizar_estadisticas.py --stats
   ```

2. **Actualizar índice general:**
   ```bash
   python3 actualizar_estadisticas.py --update
   ```

### Análisis Periódico
1. **Análisis completo mensual:**
   ```bash
   python3 actualizar_estadisticas.py --full
   ```

2. **Regenerar índices de asignaturas:**
   ```bash
   python3 generar_indice_obsidian.py
   ```

### Migración de Nuevas Asignaturas
1. **Añadir nuevos archivos al vault**
2. **Ejecutar migración de tags:**
   ```bash
   python3 migrar_asignaturas.py
   ```
3. **Actualizar estadísticas:**
   ```bash
   python3 actualizar_estadisticas.py --update
   ```

## 📈 Estadísticas Automáticas

El sistema genera automáticamente:
- **Total de archivos** procesados
- **Asignaturas activas** detectadas
- **Tags únicos** en uso
- **Porcentaje de cumplimiento** del sistema estándar
- **Fecha de última actualización**

## 🔧 Configuración

### Dependencias
```bash
pip install pyyaml
```

### Estructura de Directorios
```
scripts/
├── analisis_contenido.py      # Motor principal
├── actualizar_estadisticas.py # Interfaz amigable
├── generar_indice_obsidian.py # Generador de índices
├── migrar_asignaturas.py      # Migrador de tags
├── analizador_obsidian.py     # Módulo base
└── README.md                  # Esta documentación
```

### Configuración de Asignaturas
Las asignaturas se configuran en `analizador_obsidian.py` en el diccionario `asignaturas_tags`:

```python
self.asignaturas_tags = {
    'primero-1-geologia-1': 'Geología I',
    'primero-2-geologia-2': 'Geología II',
    # ... más asignaturas
}
```

## 🚀 Automatización Avanzada

### Cron Job (Linux/Mac)
Para actualizar estadísticas diariamente:
```bash
# Editar crontab
crontab -e

# Añadir línea (actualizar a las 8:00 AM diarias)
0 8 * * * cd /ruta/a/scripts && python3 actualizar_estadisticas.py --update
```

### Tarea Programada (Windows)
Usar Task Scheduler para ejecutar:
```cmd
python3 actualizar_estadisticas.py --update
```

## 🐛 Solución de Problemas

### Error: "No se encontró el bloque de estadísticas"
- Verificar que `index.md` existe
- Asegurar que el bloque de estadísticas tiene el formato correcto

### Error: "ModuleNotFoundError: yaml"
```bash
pip install pyyaml
```

### Archivos no procesados
- Verificar rutas relativas en los scripts
- Comprobar permisos de escritura en directorios

## 📝 Contribuir

Para añadir nuevas funcionalidades:
1. Modificar `analizador_obsidian.py` para nuevas capacidades de análisis
2. Extender `analisis_contenido.py` para nueva lógica de negocio
3. Actualizar `actualizar_estadisticas.py` para nuevas opciones de interfaz

---

*Última actualización: 21/09/2025*
*Autor: Alberto Pérez del Río*
*Licencia: MIT*