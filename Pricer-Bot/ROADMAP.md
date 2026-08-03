# Roadmap — Bot de precios

Plan de milestones para llegar a "buscador por ID + recordar mis productos". Se va tachando a medida que se completa. No hay apuro en llegar al final — cada milestone se aborda cuando el anterior esté sólido.

---

## ✅ Hecho hasta ahora
- # Milestone A — Búsqueda confiable por ID exacto
- Descarga automática de datos SEPA (con chequeo de "ya existe" para no descargar de más)
- Extracción de ZIPs anidados
- Lectura de CSV con `csv.DictReader` (separador `|`)
- Búsqueda por texto en `productos_descripcion` (con sus limitaciones ya vistas: falsos positivos por substrings)
- Función `buscar_por_id(ruta_archivo, id_producto)`

---

## Milestone B — "Mi lista de productos" (persistencia)
**Por qué:** hoy, cada vez que cerrás el programa, se pierde todo lo que buscaste. La idea es guardar en disco los productos que te interesan, para no tener que re-buscarlos por nombre cada vez — el corazón de "que lo recuerde".

**Qué hace falta:**
- Un archivo `mis_productos.json` que guarde una lista de productos trackeados (id, nombre, fecha en que lo agregaste).
- Funciones: `cargar_mi_lista()` (leer el JSON, o devolver lista vacía si el archivo no existe todavía) y `agregar_a_mi_lista(producto)` (sumar uno nuevo y volver a guardar).

**Concepto nuevo:** el módulo `json` — muy parecido a lo que ya sabés de diccionarios, solo que ahora los guardás/leés de un archivo en vez de tenerlos solo en memoria mientras el programa corre. Es un paso corto desde donde ya estás.

---

## Milestone C — Comparar precios de "mi lista" entre sucursales y cadenas
**Por qué:** acá se junta todo — recorrés tu lista guardada, y para cada producto buscás su precio en todos los comercios que tengas descargados, no solo Coto.

**Qué hace falta:** un loop que recorra todas las carpetas de comercios descargados (`sepa_data/comercio_XX/`), aplicando `buscar_por_id` en cada una, y quedándote con el precio más bajo encontrado.

**Concepto nuevo:** recorrer múltiples carpetas con un loop (usando `os.listdir` o similar) — una extensión natural de lo que ya sabés de `os.path.exists`.

---

## Milestone D — Identificar y descargar más cadenas, no solo Coto
**Por qué:** hoy solo extrajimos `comercio_12`. Para comparar de verdad entre supermercados, hay que saber qué ID corresponde a Dia, Carrefour, Jumbo, etc. (mismo método que usamos para descubrir que 12 era Coto: leer su `comercio.csv`).

**Qué hace falta:** repetir la extracción + lectura de `comercio.csv` para unos cuantos IDs más del ZIP grande, armando un diccionario tipo `{"Dia": 5, "Carrefour": 20, ...}` una vez identificados.

**Concepto nuevo:** ninguno nuevo — es aplicar varias veces algo que ya hicimos.

---

## Milestone E — Automatizar el chequeo (la idea original del proyecto)
**Por qué:** cerrar el círculo con la idea de "que me avise cuándo conviene comprar", en vez de correr el script a mano cada vez.

**Qué hace falta:** que el script, al final, imprima un resumen tipo "producto X bajó de precio en la sucursal Y" — y eventualmente, programar que se ejecute solo todos los días (Windows tiene una herramienta para esto, Task Scheduler).

**Concepto nuevo:** dependiendo de qué tan lejos quieras llegar — desde algo simple (imprimir un resumen) hasta notificaciones por mail o Telegram.

---

*Actualizado a medida que avanzamos. Si tachás un milestone, hacé commit del cambio — así el historial de git también cuenta la historia del proyecto.*
