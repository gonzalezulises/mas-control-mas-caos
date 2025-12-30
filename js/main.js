/**
 * Más control, más caos — Animaciones
 * © 2025 Ulises González - Rizo.ma
 *
 * Dependencia: anime.js v3.2.2
 */

(function() {
  'use strict';

  // Verificar que anime.js esté disponible
  if (typeof anime === 'undefined') {
    console.warn('anime.js no está disponible. Las animaciones están deshabilitadas.');
    // Mostrar contenido sin animaciones
    document.querySelectorAll('.hero .title .letter, .hero .subtitle').forEach(el => {
      el.style.opacity = '1';
    });
    return;
  }

  // ==========================================================================
  // 1. ANIMACIÓN DEL TÍTULO HERO - Entrada secuencial de letras
  // ==========================================================================

  function initTitleAnimation() {
    const title = document.querySelector('.hero .title');
    if (!title) return;

    const text = title.textContent;
    title.innerHTML = '';

    // Envolver cada letra en un span
    text.split('').forEach(char => {
      const span = document.createElement('span');
      span.className = 'letter';
      // Preservar espacios como entidades
      span.innerHTML = char === ' ' ? '&nbsp;' : char;
      title.appendChild(span);
    });

    // Timeline de animación
    anime.timeline({
      easing: 'easeOutExpo'
    })
    .add({
      targets: '.hero .title .letter',
      opacity: [0, 1],
      translateY: [20, 0],
      duration: 800,
      delay: anime.stagger(50)
    })
    .add({
      targets: '.hero .subtitle',
      opacity: [0, 1],
      translateY: [10, 0],
      duration: 600
    }, '-=400');
  }

  // ==========================================================================
  // 2. ANIMACIÓN DEL LOOP VISUAL - Feedback runaway
  // ==========================================================================

  function initLoopAnimation() {
    const loopVisual = document.querySelector('.loop-visual svg');
    if (!loopVisual) return;

    // Animación que acelera progresivamente
    anime({
      targets: '.loop-visual svg .arrows',
      rotate: '1turn',
      duration: 3000,
      easing: 'easeInQuad',
      loop: true,
      direction: 'normal'
    });
  }

  // ==========================================================================
  // 3. ANIMACIÓN DE BOTONES CTA - Hover
  // ==========================================================================

  function initButtonAnimations() {
    const buttons = document.querySelectorAll('.btn, .cta-primary');

    buttons.forEach(btn => {
      btn.addEventListener('mouseenter', () => {
        anime({
          targets: btn,
          scale: 1.02,
          duration: 200,
          easing: 'easeOutQuad'
        });
      });

      btn.addEventListener('mouseleave', () => {
        anime({
          targets: btn,
          scale: 1,
          duration: 200,
          easing: 'easeOutQuad'
        });
      });
    });
  }

  // ==========================================================================
  // INICIALIZACIÓN
  // ==========================================================================

  function init() {
    // Respetar preferencia de movimiento reducido
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReducedMotion) {
      // Mostrar contenido sin animaciones
      document.querySelectorAll('.hero .title .letter, .hero .subtitle').forEach(el => {
        el.style.opacity = '1';
      });
      return;
    }

    initTitleAnimation();
    initLoopAnimation();
    initButtonAnimations();
  }

  // Ejecutar cuando el DOM esté listo
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
