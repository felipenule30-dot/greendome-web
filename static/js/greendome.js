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

  // Hamburger (mobile)
  const burger = document.getElementById('navHamburger');
  const links  = nav.querySelector('.nav-links');
  if (burger && links) {
    burger.addEventListener('click', () => {
      const open = links.style.display === 'flex';
      links.style.cssText = open
        ? ''
        : 'display:flex;flex-direction:column;position:absolute;top:100%;left:0;right:0;background:rgba(13,10,20,.97);padding:1.5rem 5vw;gap:1.2rem;border-bottom:1px solid rgba(126,217,87,.15);backdrop-filter:blur(16px);';
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

  function draw() {
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
