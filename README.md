# Reef to Table — sitio estático (GitHub Pages)

Recreación del sitio [reeftotable.com](https://reeftotable.com) en HTML, CSS y JavaScript puros — sin frameworks, sin Node.js y sin dependencias de ningún tipo. Listo para publicarse directamente en GitHub Pages.

## Estructura del proyecto

```
reef-to-table/
├── index.html          → página "About" (inicio)
├── product.html         → página "Product"
├── businesses.html      → página "Businesses"
├── gallery.html         → página "Gallery"
├── contact.html         → página "Contact"
├── css/
│   └── style.css        → todos los estilos del sitio
├── images/               → todas las imágenes (temporales por ahora)
└── dev-tools/
    └── generate_placeholders.py  → script opcional que generó las imágenes temporales (no forma parte del sitio publicado)
```

## Imágenes: cómo reemplazarlas

Todas las imágenes que ves ahora son **temporales** (un fondo azul con el nombre de archivo escrito encima), generadas solo para que el sitio sea navegable de inmediato. Para poner tus fotos reales, simplemente reemplaza cada archivo dentro de `images/` **conservando el mismo nombre**, y el sitio las mostrará automáticamente — no hay que tocar ningún HTML ni CSS.

| Archivo a reemplazar | Dónde aparece | Contenido sugerido |
|---|---|---|
| `logo.png` | Header y footer de las 5 páginas | Logo de Reef to Table |
| `favicon.png` | Pestaña del navegador | Ícono pequeño de marca |
| `hero.jpg` | Home | Foto principal (banner con bandeja de ostras) |
| `oyster-closeup.jpg` | Home | Ostra en primer plano |
| `platter.jpg` | Home | Bandeja de ostras con romero |
| `product-01.jpg` | Product | Manos abriendo ostras |
| `product-02.jpg` | Product | Ostras horneadas con toppings |
| `product-03.jpg` | Product | Food truck / trailer de marca |
| `business-01.jpg` | Businesses | Manos abriendo ostras |
| `business-02.jpg` | Businesses | Ostras horneadas con toppings |
| `business-03.jpg` | Businesses | Food truck / trailer de marca |
| `gallery-01.jpg` a `gallery-12.jpg` | Gallery (cuadrícula "Just a glimpse…") | 12 fotos de la galería principal |
| `gallery-13.jpg` a `gallery-19.jpg` | Gallery (cuadrícula "favorite specials") | 7 fotos de platos/especiales |

Recomendaciones al reemplazar:
- Usa formato `.jpg` para fotos y `.png` para el logo/favicon (o ajusta la extensión en el HTML si usas otro formato).
- Para que la cuadrícula de la galería luzca prolija, usa fotos de proporción similar (aprox. cuadradas). Las demás imágenes se recortan automáticamente con `object-fit: cover`, así que no es necesario que tengan el tamaño exacto.
- Comprime las imágenes antes de subirlas (por ejemplo con [Squoosh](https://squoosh.app) o TinyPNG) para que el sitio cargue rápido.

## Cómo ver el sitio en tu computadora

No hace falta instalar nada. Dos opciones:

1. **Abrir directamente**: doble clic en `index.html` (funciona, aunque algunos navegadores restringen un poco las rutas relativas al abrir con `file://`).
2. **Servidor local simple** (recomendado): con Python instalado, desde la carpeta del proyecto:
   ```
   python3 -m http.server 8000
   ```
   Luego abre `http://localhost:8000` en el navegador.

## Cómo publicarlo en GitHub Pages

1. Crea un repositorio nuevo en GitHub (por ejemplo `reef-to-table`).
2. Sube todo el contenido de esta carpeta a la raíz del repositorio (`index.html` debe quedar en la raíz, no dentro de una subcarpeta).
3. En GitHub, ve a **Settings → Pages**.
4. En "Build and deployment", elige **Deploy from a branch**, rama `main`, carpeta `/ (root)`.
5. Guarda. GitHub te dará una URL del tipo `https://tu-usuario.github.io/reef-to-table/`.
6. (Opcional) Si quieres usar tu dominio propio `reeftotable.com`, crea un archivo `CNAME` en la raíz con ese dominio adentro, y configura un registro `CNAME`/`A` en tu proveedor de DNS apuntando a GitHub Pages.

## Pendiente antes de publicar en producción

- **Formulario de contacto** (`contact.html`): por ahora solo valida y muestra un mensaje en pantalla (`js/script.js`), pero no envía ningún correo — GitHub Pages no puede procesar formularios por sí solo. Antes de publicar, regístrate en un servicio gratuito como [Formspree](https://formspree.io) o [EmailJS](https://www.emailjs.com), y reemplaza el atributo `action="#"` del `<form>` por la URL que te den.
- **Reemplazar todas las imágenes temporales** según la tabla de arriba.
- **Google Fonts**: el sitio carga las tipografías Manrope y Poppins desde Google Fonts (una sola línea `<link>` en el `<head>` de cada página). Si prefieres un sitio 100% sin llamadas externas, puedes quitar esa línea; el sitio usará la tipografía del sistema como respaldo.
