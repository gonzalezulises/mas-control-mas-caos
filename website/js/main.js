/**
 * Más control, más caos — Animaciones completas
 * © 2025 Ulises González - Rizo.ma
 *
 * 6 Animaciones conceptuales:
 * 1. Title Reveal - Entrada dramática del título
 * 2. Runaway Spiral - Espirales de caos que pulsan
 * 3. Node Cascade - Nodos que propagan "trabajo"
 * 4. Breaking Connections - Conexiones que fallan
 * 5. Concentric Pulse - Círculos que buscan control
 * 6. Particle Drift - Partículas que derivan y cambian
 */

(function() {
  'use strict';

  // Verificar que anime.js esté disponible
  if (typeof anime === 'undefined') {
    console.warn('anime.js no está disponible.');
    showFallback();
    return;
  }

  // Mostrar contenido sin animaciones
  function showFallback() {
    document.querySelectorAll('.title-line, .hero .subtitle').forEach(el => {
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
    document.querySelectorAll('.spiral-path').forEach(el => {
      el.style.strokeDashoffset = '0';
    });
  }

  // ==========================================================================
  // 1. TITLE REVEAL - Entrada dramática del título
  // ==========================================================================

  function initTitleReveal() {
    const timeline = anime.timeline({
      easing: 'easeOutExpo'
    });

    // "Más control," aparece primero
    timeline.add({
      targets: '.title-control',
      opacity: [0, 1],
      translateY: [30, 0],
      duration: 1000
    });

    // Pausa dramática, luego "más caos" explota
    timeline.add({
      targets: '.title-chaos',
      opacity: [0, 1],
      translateY: [50, 0],
      scale: [0.8, 1],
      duration: 800,
      easing: 'easeOutBack'
    }, '+=200');

    // Subtítulo aparece suavemente
    timeline.add({
      targets: '.hero .subtitle',
      opacity: [0, 1],
      translateY: [20, 0],
      duration: 600
    }, '-=400');

    // CTA aparece
    timeline.add({
      targets: '.hero .cta-primary',
      opacity: [0, 1],
      translateY: [10, 0],
      duration: 400
    }, '-=200');
  }

  // ==========================================================================
  // 2. RUNAWAY SPIRAL - Espirales de caos que pulsan y crecen
  // ==========================================================================

  function initRunawaySpiral() {
    // Dibujar las espirales progresivamente
    anime({
      targets: '.spiral-path',
      strokeDashoffset: [anime.setDashoffset, 0],
      duration: 3000,
      delay: anime.stagger(500),
      easing: 'easeInOutQuad',
      complete: function() {
        // Una vez dibujadas, empezar pulsación
        startSpiralPulse();
      }
    });
  }

  function startSpiralPulse() {
    // Pulsación continua - el caos nunca descansa
    anime({
      targets: '.chaos-spiral',
      scale: [1, 1.05, 1],
      opacity: [1, 0.8, 1],
      duration: 4000,
      easing: 'easeInOutSine',
      loop: true
    });

    // Las espirales individuales pulsan desfasadas
    anime({
      targets: '.spiral-1',
      strokeWidth: [4, 6, 4],
      duration: 3000,
      easing: 'easeInOutQuad',
      loop: true
    });

    anime({
      targets: '.spiral-2',
      strokeWidth: [3, 5, 3],
      duration: 3500,
      easing: 'easeInOutQuad',
      loop: true,
      delay: 500
    });
  }

  // ==========================================================================
  // 3. NODE CASCADE - Nodos que propagan señales (Coding Trance)
  // ==========================================================================

  function initNodeCascade() {
    // El nodo central emite pulsos
    anime({
      targets: '.node-center',
      scale: [1, 1.3, 1],
      opacity: [1, 0.7, 1],
      duration: 2000,
      easing: 'easeInOutQuad',
      loop: true
    });

    // Los nodos azules responden en cascada
    anime({
      targets: '.node-blue',
      scale: [1, 1.2, 1],
      opacity: [0.8, 1, 0.8],
      duration: 2000,
      delay: anime.stagger(200, {start: 300}),
      easing: 'easeInOutQuad',
      loop: true
    });

    // Los nodos rojos (fallas) parpadean de forma errática
    anime({
      targets: '.node-red',
      scale: [1, 1.4, 1],
      opacity: [0.7, 1, 0.5, 1, 0.7],
      duration: 3000,
      delay: anime.stagger(400),
      easing: 'easeInOutQuad',
      loop: true
    });
  }

  // ==========================================================================
  // 4. BREAKING CONNECTIONS - Conexiones que fallan intermitentemente
  // ==========================================================================

  function initBreakingConnections() {
    // Las conexiones rotas aparecen y desaparecen
    anime({
      targets: '.broken-line',
      opacity: [0, 0.8, 0.8, 0],
      strokeDashoffset: [20, 0, 0, -20],
      duration: 4000,
      delay: anime.stagger(1000),
      easing: 'easeInOutQuad',
      loop: true
    });

    // Las conexiones normales también tiemblan sutilmente
    anime({
      targets: '.connection',
      opacity: [0.5, 0.7, 0.5],
      duration: 3000,
      delay: anime.stagger(100),
      easing: 'easeInOutSine',
      loop: true
    });
  }

  // ==========================================================================
  // 5. CONCENTRIC PULSE - Círculos que buscan control sin lograrlo
  // ==========================================================================

  function initConcentricPulse() {
    // Cada círculo pulsa hacia afuera, buscando estabilidad
    anime({
      targets: '.pulse-circle',
      scale: [1, 1.02, 1],
      opacity: [0.6, 0.8, 0.6],
      strokeWidth: ['+=0', '+=0.5', '+=0'],
      duration: 4000,
      delay: anime.stagger(300, {direction: 'reverse'}),
      easing: 'easeInOutSine',
      loop: true
    });
  }

  // ==========================================================================
  // 6. PARTICLE DRIFT - Partículas que derivan y algunas se vuelven rojas
  // ==========================================================================

  function initParticleDrift() {
    const particles = document.querySelectorAll('.particle');

    particles.forEach((particle, index) => {
      // Movimiento aleatorio flotante
      const randomX = anime.random(-30, 30);
      const randomY = anime.random(-30, 30);
      const duration = anime.random(5000, 8000);

      anime({
        targets: particle,
        translateX: [0, randomX, -randomX/2, 0],
        translateY: [0, randomY, -randomY/2, 0],
        opacity: [0.3, 0.6, 0.3],
        duration: duration,
        easing: 'easeInOutSine',
        loop: true
      });

      // Algunas partículas cambian a rojo (señales ignoradas)
      if (index % 3 === 0) {
        anime({
          targets: particle,
          fill: ['#3d7ab7', '#dc143c', '#3d7ab7'],
          r: [particle.getAttribute('r'), parseFloat(particle.getAttribute('r')) * 1.5, particle.getAttribute('r')],
          duration: duration * 2,
          easing: 'easeInOutQuad',
          loop: true,
          delay: duration / 2
        });
      }
    });
  }

  // ==========================================================================
  // 7. LOOP VISUAL - Animación de la sección tensión
  // ==========================================================================

  function initLoopAnimation() {
    anime({
      targets: '.loop-arrows',
      rotate: '1turn',
      duration: 3000,
      easing: 'easeInQuad',
      loop: true
    });
  }

  // ==========================================================================
  // 8. BUTTON HOVER - Interacción profesional en botones
  // ==========================================================================

  function initButtonAnimations() {
    const buttons = document.querySelectorAll('.btn, .cta-primary');

    buttons.forEach(btn => {
      // Hover enter - efecto elástico profesional
      btn.addEventListener('mouseenter', () => {
        anime.remove(btn); // Cancelar animaciones previas
        anime({
          targets: btn,
          scale: [1, 1.05],
          translateY: [0, -3],
          duration: 400,
          easing: 'easeOutElastic(1, .6)'
        });
      });

      // Hover leave - retorno suave
      btn.addEventListener('mouseleave', () => {
        anime.remove(btn);
        anime({
          targets: btn,
          scale: 1,
          translateY: 0,
          duration: 300,
          easing: 'easeOutQuad'
        });
      });

      // Click - efecto de presión
      btn.addEventListener('mousedown', () => {
        anime({
          targets: btn,
          scale: 0.95,
          duration: 100,
          easing: 'easeInQuad'
        });
      });

      btn.addEventListener('mouseup', () => {
        anime({
          targets: btn,
          scale: 1.05,
          duration: 200,
          easing: 'easeOutElastic(1, .5)'
        });
      });
    });

    // Efecto especial para CTA principal del hero - pulso sutil
    const heroCta = document.querySelector('.hero .cta-primary');
    if (heroCta) {
      anime({
        targets: heroCta,
        boxShadow: [
          '0 0 0 0 rgba(139, 0, 0, 0.4)',
          '0 0 0 15px rgba(139, 0, 0, 0)',
          '0 0 0 0 rgba(139, 0, 0, 0)'
        ],
        duration: 2000,
        easing: 'easeInOutQuad',
        loop: true,
        delay: 3000 // Empieza después de que aparece el título
      });
    }
  }

  // ==========================================================================
  // SCROLL-TRIGGERED ANIMATIONS
  // ==========================================================================

  function initScrollAnimations() {
    // Observador para animar elementos cuando entran en viewport
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;

          if (el.classList.contains('tension')) {
            anime({
              targets: '.tension p',
              opacity: [0, 1],
              translateY: [20, 0],
              duration: 600,
              delay: anime.stagger(200),
              easing: 'easeOutQuad'
            });
          }

          if (el.classList.contains('tesis')) {
            anime({
              targets: 'blockquote',
              opacity: [0, 1],
              translateX: [-20, 0],
              duration: 800,
              easing: 'easeOutQuad'
            });
          }

          if (el.classList.contains('contenido')) {
            anime({
              targets: '.contenido li',
              opacity: [0, 1],
              translateX: [-10, 0],
              duration: 400,
              delay: anime.stagger(100),
              easing: 'easeOutQuad'
            });
          }

          observer.unobserve(el);
        }
      });
    }, { threshold: 0.2 });

    document.querySelectorAll('.tension, .tesis, .contenido').forEach(section => {
      observer.observe(section);
    });
  }

  // ==========================================================================
  // INICIALIZACIÓN
  // ==========================================================================

  function init() {
    // Respetar preferencia de movimiento reducido
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReducedMotion) {
      showFallback();
      return;
    }

    // Inicializar todas las animaciones
    initTitleReveal();

    // Animaciones del SVG de fondo (con delay para que cargue el título primero)
    setTimeout(() => {
      initRunawaySpiral();
      initNodeCascade();
      initBreakingConnections();
      initConcentricPulse();
      initParticleDrift();
    }, 1500);

    initLoopAnimation();
    initButtonAnimations();
    initScrollAnimations();
  }

  // Ejecutar cuando el DOM esté listo
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
