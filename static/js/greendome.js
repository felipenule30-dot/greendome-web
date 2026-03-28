/* ============================================================
   GREEN DOME — Main JavaScript
   Cursor · Partículas Hero · Scroll Reveal · Nav Scroll
   Brand: Púrpura profundo + Verde brillante
   ============================================================ */

'use strict';

/* ── Custom Cursor ─────────────────────────────────────────── */
(function initCursor() {
  const dot  = document.getElementById('cursorDot');
  const ring = document.getElementById('cursorRing');
  if (!dot || !ring) return;

  let mouseX = 0, mouseY = 0;
  let ringX  = 0, ringY  = 0;

  document.addEventListener('mousemove', e => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.left = mouseX + 'px';
    dot.style.top  = mouseY + 'px';
  });

  (function animateRing() {
    ringX += (mouseX - ringX) * 0.12;
    ringY += (mouseY - ringY) * 0.12;
    ring.style.left = ringX + 'px';
    ring.style.top  = ringY + 'px';
    requestAnimationFrame(animateRing);
  })();

  // Hide on touch devices
  if ('ontouchstart' in window) {
    dot.style.display  = 'none';
    ring.style.display = 'none';
    document.body.style.cursor = 'auto';
  }
})();

/* ── Nav Scroll Effect ─────────────────────────────────────── */
(function initNav() {
  const nav = document.getElementById('gdNav');
  if (!nav) return;

  const onScroll = () => {
    nav.classList.toggle('scrolled', window.scrollY > 60);
  };
  window.addEventListener('scroll', onScroll, { passive: true });

  // Hamburger (mobile) — animado con clase
  const burger = document.getElementById('navHamburger');
  const links  = nav.querySelector('.nav-links');
  if (burger && links) {
    burger.addEventListener('click', () => {
      const open = links.classList.toggle('nav-open');
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open);
    });
    // Cerrar al hacer click en un enlace
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        links.classList.remove('nav-open');
        burger.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }
})();

/* ── Scroll Reveal ─────────────────────────────────────────── */
(function initReveal() {
  const selectors = '.reveal, .reveal-left, .reveal-right';
  const els = document.querySelectorAll(selectors);
  if (!els.length) return;

  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  els.forEach((el, i) => {
    el.style.transitionDelay = (i % 5) * 0.08 + 's';
    io.observe(el);
  });
})();

/* ── Hero Particle Canvas ──────────────────────────────────── */
(function initHeroParticles() {
  const canvas = document.getElementById('heroParticles');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let W, H, particles;

  // Brand color palette — púrpura + verde
  const COLORS = [
    '#7ed957', '#5db845', '#3a7d2c',
    '#7ed957', '#5b3080', '#9060c0',
    '#c9a84c',
  ];
  const COUNT = window.innerWidth < 600 ? 45 : 90;

  function resize() {
    W = canvas.width  = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
  }

  function mkParticle() {
    return {
      x:     Math.random() * W,
      y:     Math.random() * H,
      r:     Math.random() * 2.5 + .4,
      vx:    (Math.random() - .5) * .35,
      vy:    -(Math.random() * .7 + .15),
      life:  Math.random(),
      color: COLORS[Math.floor(Math.random() * COLORS.length)],
      shape: Math.random() > 0.85 ? 'diamond' : 'circle', // 15% diamantes
    };
  }

  function init() {
    resize();
    particles = Array.from({ length: COUNT }, mkParticle);
  }

  function drawParticle(p) {
    const alpha = Math.sin(p.life * Math.PI) * .75;
    ctx.globalAlpha = alpha;
    ctx.fillStyle   = p.color;

    if (p.shape === 'diamond') {
      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate(Math.PI / 4);
      ctx.fillRect(-p.r, -p.r, p.r * 2, p.r * 2);
      ctx.restore();
    } else {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  let animating = true;
  function draw() {
    if (!animating) return;
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => {
      p.x    += p.vx;
      p.y    += p.vy;
      p.life += .0025;
      if (p.y < -10 || p.life > 1) Object.assign(p, mkParticle(), { y: H + 5 });
      drawParticle(p);
    });
    ctx.globalAlpha = 1;
    requestAnimationFrame(draw);
  }

  // Pausar cuando la pestaña no es visible — ahorra CPU/batería
  document.addEventListener('visibilitychange', () => {
    animating = !document.hidden;
    if (animating) draw();
  });

  window.addEventListener('resize', resize, { passive: true });
  init();
  draw();
})();

/* ── Smooth anchor scrolling ───────────────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

/* ── Personajes: arrastrar para scroll ─────────────────────── */
(function initDragScroll() {
  const wrap = document.querySelector('.personajes-scroll-wrap');
  if (!wrap) return;

  let isDown = false, startX, scrollLeft;

  wrap.addEventListener('mousedown', e => {
    isDown    = true;
    startX    = e.pageX - wrap.offsetLeft;
    scrollLeft = wrap.scrollLeft;
    wrap.style.cursor = 'grabbing';
  });
  wrap.addEventListener('mouseleave', () => { isDown = false; wrap.style.cursor = ''; });
  wrap.addEventListener('mouseup',    () => { isDown = false; wrap.style.cursor = ''; });
  wrap.addEventListener('mousemove',  e => {
    if (!isDown) return;
    e.preventDefault();
    const x    = e.pageX - wrap.offsetLeft;
    const walk = (x - startX) * 1.4;
    wrap.scrollLeft = scrollLeft - walk;
  });
})();

/* ── Magnetic CTA ─────────────────────────────────────────── */
(function initMagneticCTA() {
  const btn = document.querySelector('.hero-cta');
  if (!btn || 'ontouchstart' in window) return;

  btn.addEventListener('mousemove', e => {
    const r  = btn.getBoundingClientRect();
    const dx = (e.clientX - (r.left + r.width  / 2)) * 0.28;
    const dy = (e.clientY - (r.top  + r.height / 2)) * 0.28;
    btn.style.transitionDuration = '0s';
    btn.style.transform = `translateY(-4px) scale(1.05) translate(${dx.toFixed(1)}px,${dy.toFixed(1)}px)`;
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.transitionDuration = '';
    btn.style.transform = '';
  });
})();

/* ── 3D Tilt en mundo-cards ──────────────────────────────── */
(function initTilt() {
  const cards = document.querySelectorAll('.mundo-card');
  if (!cards.length || 'ontouchstart' in window) return;

  cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      // Desactiva transition de transform para respuesta instantánea
      card.style.transition = 'box-shadow .4s ease';
    });
    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width  - 0.5;
      const y = (e.clientY - r.top)  / r.height - 0.5;
      card.style.transform =
        `perspective(700px) translateY(-8px) scale(1.015) rotateX(${(-y * 7).toFixed(2)}deg) rotateY(${(x * 7).toFixed(2)}deg)`;
    });
    card.addEventListener('mouseleave', () => {
      // Restaura spring para el regreso
      card.style.transition = 'transform .5s cubic-bezier(0.34,1.56,0.64,1), box-shadow .4s ease';
      card.style.transform  = '';
      setTimeout(() => { card.style.transition = ''; }, 520);
    });
  });
})();

/* ── Parallax blob en hero ───────────────────────────────── */
(function initParallaxBlob() {
  const blob = document.querySelector('.hero-blob');
  const hero = document.querySelector('.hero');
  if (!blob || !hero || 'ontouchstart' in window) return;

  let tx = 0, ty = 0, cx = 0, cy = 0, raf, visible = false;

  window.addEventListener('mousemove', e => {
    if (!visible) return;
    cx = (e.clientX - window.innerWidth  / 2) * 0.022;
    cy = (e.clientY - window.innerHeight / 2) * 0.022;
  }, { passive: true });

  function loop() {
    if (!visible) return;
    tx += (cx - tx) * 0.055;
    ty += (cy - ty) * 0.055;
    blob.style.transform = `translate(calc(-50% + ${tx.toFixed(2)}px), calc(-50% + ${ty.toFixed(2)}px))`;
    raf = requestAnimationFrame(loop);
  }

  new IntersectionObserver(entries => {
    visible = entries[0].isIntersecting;
    if (visible) loop();
    else cancelAnimationFrame(raf);
  }, { threshold: 0 }).observe(hero);
})();

/* ── Stat cards: contador animado ──────────────────────────── */
(function initCounters() {
  const cards = document.querySelectorAll('.stat-number');
  if (!cards.length) return;

  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el  = e.target;
      const raw = el.textContent.trim();
      // Solo animar si es número puro
      const num = parseFloat(raw.replace(/[^0-9.]/g, ''));
      if (isNaN(num) || num === 0) return;
      const prefix = raw.match(/^[^0-9]*/)?.[0] || '';
      const suffix = raw.match(/[^0-9.]*$/)?.[0] || '';
      let start = 0;
      const dur  = 1200;
      const step = timestamp => {
        if (!start) start = timestamp;
        const prog = Math.min((timestamp - start) / dur, 1);
        const ease = 1 - Math.pow(1 - prog, 3); // ease-out cubic
        el.textContent = prefix + Math.round(num * ease) + suffix;
        if (prog < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
      io.unobserve(el);
    });
  }, { threshold: 0.5 });

  cards.forEach(c => io.observe(c));
})();
