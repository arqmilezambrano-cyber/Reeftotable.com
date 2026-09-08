/* ==========================================================================
   Reef to Table — script.js
   JavaScript puro (vanilla), sin dependencias ni librerías externas.

   Contiene 3 piezas independientes:
   1. Menú hamburguesa (móvil)
   2. Animación de aparición al hacer scroll (reemplaza el fadeIn nativo
      de Squarespace) usando IntersectionObserver
   3. Manejo básico del formulario de contacto (solo front-end)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {

  /* ------------------------------------------------------------------
     1. Menú hamburguesa
     ------------------------------------------------------------------ */
  var navToggle = document.getElementById('navToggle');
  var siteNav = document.getElementById('siteNav');

  if (navToggle && siteNav) {
    navToggle.addEventListener('click', function () {
      var isOpen = siteNav.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Cierra el menú al elegir una opción (útil en móvil)
    siteNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        siteNav.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ------------------------------------------------------------------
     2. Animación de aparición al hacer scroll
     ------------------------------------------------------------------ */
  var revealEls = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window && revealEls.length) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15,
      rootMargin: '0px 0px -40px 0px'
    });

    revealEls.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    // Fallback: navegadores sin soporte muestran el contenido directamente
    revealEls.forEach(function (el) {
      el.classList.add('is-visible');
    });
  }

  /* ------------------------------------------------------------------
     3. Formulario de contacto (solo front-end)
     ------------------------------------------------------------------
     GitHub Pages no puede procesar formularios por sí solo.
     Este bloque valida y muestra un mensaje en pantalla, pero NO envía
     ningún correo todavía. Antes de publicar, reemplaza el "action"
     del <form> en contact.html por la URL de un servicio como
     Formspree, EmailJS o Getform, y este mismo código servirá para
     mostrar el estado de envío.
     ------------------------------------------------------------------ */
  var contactForm = document.getElementById('contactForm');
  var formStatus = document.getElementById('formStatus');

  if (contactForm && formStatus) {
    contactForm.addEventListener('submit', function (event) {
      event.preventDefault();

      if (!contactForm.checkValidity()) {
        formStatus.textContent = 'Please fill in all required fields.';
        formStatus.className = 'form-status error';
        return;
      }

      // Placeholder: aquí iría el envío real (fetch a Formspree/EmailJS, etc.)
      formStatus.textContent = 'Thanks! (Demo form — connect it to Formspree/EmailJS before publishing.)';
      formStatus.className = 'form-status success';
      contactForm.reset();
    });
  }

});
