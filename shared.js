document.addEventListener('DOMContentLoaded', () => {
  initCursor();
  initBackgroundCanvas();
  initLoader();
  initTransitions();
  initScrollReveal();
  initNavbar();
  initCounters();
  initTilt();
});

function initCursor() {
  if (window.innerWidth <= 768) return;
  const cursor = document.createElement('div');
  cursor.classList.add('custom-cursor');
  document.body.appendChild(cursor);

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let cursorX = mouseX;
  let cursorY = mouseY;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  document.addEventListener('click', (e) => {
    const pulse = document.createElement('div');
    pulse.classList.add('sonar-pulse');
    pulse.style.left = e.clientX + 'px';
    pulse.style.top = e.clientY + 'px';
    document.body.appendChild(pulse);
    setTimeout(() => pulse.remove(), 600);
  });

  const interactiveElements = document.querySelectorAll('a, button, .tilt-card, input, textarea');
  interactiveElements.forEach(el => {
    el.addEventListener('mouseenter', () => cursor.classList.add('hover'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('hover'));
  });

  function animate() {
    let distX = mouseX - cursorX;
    let distY = mouseY - cursorY;

    // Smooth lerping for trailing ring
    cursorX += distX * 0.15;
    cursorY += distY * 0.15;

    // Hardware accelerated transform instead of CPU-bound top/left
    cursor.style.transform = `translate3d(${cursorX}px, ${cursorY}px, 0) translate(-50%, -50%)`;

    requestAnimationFrame(animate);
  }
  animate();
}

function initBackgroundCanvas() {
  const canvas = document.createElement('canvas');
  canvas.id = 'bg-canvas';
  document.body.prepend(canvas);

  const ctx = canvas.getContext('2d');
  let width, height;
  let particles = [];

  function resize() {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
  }

  window.addEventListener('resize', resize);
  resize();

  const particleCount = window.innerWidth < 768 ? 30 : 80;

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      radius: Math.random() * 1.5 + 0.5
    });
  }

  let mouseCoords = { x: null, y: null };
  window.addEventListener('mousemove', (e) => {
    mouseCoords.x = e.clientX;
    mouseCoords.y = e.clientY;
  });

  window.addEventListener('mouseout', () => {
    mouseCoords.x = null;
    mouseCoords.y = null;
  });

  function render() {
    ctx.clearRect(0, 0, width, height);

    ctx.fillStyle = 'rgba(255, 255, 255, 0.1)';
    ctx.lineWidth = 0.5;

    for (let i = 0; i < particles.length; i++) {
      let p = particles[i];
      p.x += p.vx;
      p.y += p.vy;

      if (p.x < 0 || p.x > width) p.vx *= -1;
      if (p.y < 0 || p.y > height) p.vy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fill();

      // Connect to mouse
      if (mouseCoords.x != null) {
        let dx = mouseCoords.x - p.x;
        let dy = mouseCoords.y - p.y;
        let dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 150) {
          ctx.beginPath();
          ctx.strokeStyle = `rgba(0, 212, 255, ${0.2 - dist / 750})`;
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(mouseCoords.x, mouseCoords.y);
          ctx.stroke();
        }
      }

      // Connect particles
      for (let j = i + 1; j < particles.length; j++) {
        let p2 = particles[j];
        let dx = p.x - p2.x;
        let dy = p.y - p2.y;
        let dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 100) {
          ctx.beginPath();
          ctx.strokeStyle = `rgba(255, 255, 255, ${0.1 - dist / 1000})`;
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(render);
  }
  render();
}

function initLoader() {
  if (sessionStorage.getItem('loaderShown')) {
    const loader = document.getElementById('loader');
    if (loader) loader.remove();
    return;
  }

  const loader = document.getElementById('loader');
  if (!loader) return;

  const text = loader.querySelector('.loader-text');
  const chars = text.textContent.split('');
  text.textContent = '';

  chars.forEach((c, i) => {
    const span = document.createElement('span');
    span.textContent = c === ' ' ? '\u00A0' : c;
    span.className = 'char';
    span.style.animation = `fadeUp 0.1s ${i * 0.05}s forwards`;
    text.appendChild(span);
  });

  const style = document.createElement('style');
  style.innerHTML = `
    @keyframes fadeUp {
      to { opacity: 1; transform: translateY(0); }
    }
  `;
  document.head.appendChild(style);

  setTimeout(() => {
    loader.style.opacity = '0';
    setTimeout(() => {
      loader.style.display = 'none';
      sessionStorage.setItem('loaderShown', 'true');
    }, 800);
  }, chars.length * 50 + 1000);
}

function initTransitions() {
  const overlay = document.createElement('div');
  overlay.className = 'page-transition';
  document.body.appendChild(overlay);

  document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', e => {
      const href = link.getAttribute('href');
      // ✅ FIX: Added parentheses to prevent null crash when href is null
      if (href && (href.startsWith('/') || href.endsWith('.html'))) {
        e.preventDefault();
        overlay.classList.add('active');
        setTimeout(() => {
          window.location.href = href;
        }, 500);
      }
    });
  });
}

function initScrollReveal() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // Text stagger setup
  document.querySelectorAll('.reveal-text').forEach(el => {
    const text = el.textContent;
    el.textContent = '';
    text.split('').forEach((char, i) => {
      const span = document.createElement('span');
      span.textContent = char === ' ' ? '\u00A0' : char;
      span.className = 'char';
      span.style.transitionDelay = `${i * 0.03}s`;
      el.appendChild(span);
    });
    observer.observe(el);
  });
}

function initNavbar() {
  const nav = document.querySelector('.navbar');
  if (!nav) return;
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');

  if (hamburger) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      const spans = hamburger.querySelectorAll('span');
      if (mobileMenu.classList.contains('open')) {
        spans[0].style.transform = 'translateY(7px) rotate(45deg)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'translateY(-7px) rotate(-45deg)';
      } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
      }
    });
  }

  const underline = document.querySelector('.nav-underline');
  const activeLink = document.querySelector('.nav-links a.active');

  function updateUnderline(el) {
    if (!underline) return;
    if (el) {
      underline.style.width = el.offsetWidth + 'px';
      underline.style.left = el.offsetLeft + 'px';
      underline.style.opacity = '1';
    } else {
      underline.style.opacity = '0';
    }
  }

  if (activeLink) updateUnderline(activeLink);

  const links = document.querySelectorAll('.nav-links a');
  links.forEach(link => {
    link.addEventListener('mouseenter', () => updateUnderline(link));
    link.addEventListener('mouseleave', () => updateUnderline(activeLink));
  });
}

function initCounters() {
  const counters = document.querySelectorAll('.counter');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = +entry.target.getAttribute('data-target');
        let count = 0;
        const speed = target / 50;

        const updateCount = () => {
          count += speed;
          if (count < target) {
            entry.target.innerText = Math.ceil(count);
            requestAnimationFrame(updateCount);
          } else {
            entry.target.innerText = target;
          }
        };
        updateCount();
        observer.unobserve(entry.target);
      }
    });
  });

  counters.forEach(counter => observer.observe(counter));
}

function initTilt() {
  if (window.innerWidth <= 768) return;
  const cards = document.querySelectorAll('.tilt-card');

  cards.forEach(card => {
    const parent = card;
    const content = card.querySelector('.tilt-content');
    if (!content) return;

    parent.addEventListener('mousemove', e => {
      const rect = parent.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -10;
      const rotateY = ((x - centerX) / centerX) * 10;

      // ✅ FIX: Removed escaped backticks — proper template literals
      content.style.transform = `translateZ(30px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    parent.addEventListener('mouseleave', () => {
      content.style.transform = `translateZ(30px) rotateX(0) rotateY(0)`;
      content.style.transition = 'transform 0.5s ease';
      setTimeout(() => content.style.transition = '', 500);
    });
  });
}