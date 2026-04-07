/**
 * SHARED JS — runs on every page
 * - Custom cursor
 * - Navbar scroll / active link
 * - Hamburger / mobile drawer
 * - Page transition (veil)
 * - Scroll progress bar
 * - IntersectionObserver fade-up
 */

/* ── Custom Cursor ── */
const dot  = document.querySelector('.cursor-dot');
const ring = document.querySelector('.cursor-ring');
let mx = 0, my = 0, rx = 0, ry = 0;

document.addEventListener('mousemove', e => {
  mx = e.clientX; my = e.clientY;
  dot.style.left  = mx + 'px';
  dot.style.top   = my + 'px';
});
(function animRing() {
  rx += (mx - rx) * 0.14;
  ry += (my - ry) * 0.14;
  ring.style.left = rx + 'px';
  ring.style.top  = ry + 'px';
  requestAnimationFrame(animRing);
})();

document.querySelectorAll('a, button, [role="button"], .skill-tag, .project-card, label, input, textarea, .filter-btn').forEach(el => {
  el.addEventListener('mouseenter', () => { dot.classList.add('hovered'); ring.classList.add('hovered'); });
  el.addEventListener('mouseleave', () => { dot.classList.remove('hovered'); ring.classList.remove('hovered'); });
});

/* ── Progress Bar ── */
const prog = document.querySelector('.progress-bar');
if (prog) {
  window.addEventListener('scroll', () => {
    const s = document.documentElement.scrollTop;
    const h = document.documentElement.scrollHeight - window.innerHeight;
    prog.style.width = (h > 0 ? (s/h)*100 : 0) + '%';
  }, { passive: true });
}

/* ── Navbar scroll + active ── */
const navbar = document.querySelector('.navbar');
const navLinks = document.querySelectorAll('.nav-links a, .nav-drawer a');

window.addEventListener('scroll', () => {
  if(navbar) navbar.classList.toggle('scrolled', window.scrollY > 20);
}, { passive: true });

// Mark active nav link based on current page filename
(function setActiveLink() {
  const page = location.pathname.split('/').pop() || 'index.html';
  navLinks.forEach(a => {
    const href = a.getAttribute('href').split('/').pop();
    a.classList.toggle('active', href === page);
  });
})();

/* ── Hamburger / Mobile Drawer ── */
const ham    = document.querySelector('.hamburger');
const drawer = document.querySelector('.nav-drawer');
if (ham && drawer) {
  ham.addEventListener('click', () => {
    ham.classList.toggle('open');
    drawer.classList.toggle('open');
  });
  drawer.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      ham.classList.remove('open');
      drawer.classList.remove('open');
    });
  });
}

/* ── Page Transition (veil) ── */
const veil = document.getElementById('page-veil');
function goTo(url) {
  if (!veil) { location.href = url; return; }
  veil.classList.add('out');
  setTimeout(() => { location.href = url; }, 440);
}
document.querySelectorAll('a[href]').forEach(a => {
  const href = a.getAttribute('href');
  // Only intercept same-origin, same-directory page links (not anchors, mailto, external)
  if (!href || href.startsWith('#') || href.startsWith('mailto') || href.startsWith('http') || href.includes('Gowrishankar_Resume')) return;
  a.addEventListener('click', e => {
    e.preventDefault();
    goTo(href);
  });
});
// Fade in on load
window.addEventListener('DOMContentLoaded', () => {
  if (veil) {
    veil.classList.add('in');
    setTimeout(() => veil.classList.remove('in'), 50);
  }
});

/* ── Fade-up IntersectionObserver ── */
const fuEls = document.querySelectorAll('.fu');
const fuIO  = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('show'); fuIO.unobserve(e.target); }
  });
}, { threshold: 0.1 });
fuEls.forEach(el => fuIO.observe(el));

/* ── Count-up for stat numbers ── */
function countUp(el) {
  const target = +el.dataset.count;
  const dur    = 1400;
  const step   = 30;
  const inc    = target / (dur / step);
  let cur = 0;
  const t = setInterval(() => {
    cur += inc;
    if (cur >= target) { el.textContent = target + (el.dataset.suffix||''); clearInterval(t); }
    else el.textContent = Math.floor(cur) + (el.dataset.suffix||'');
  }, step);
}
const countEls = document.querySelectorAll('[data-count]');
if (countEls.length) {
  const cIO = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { countUp(e.target); cIO.unobserve(e.target); } });
  }, { threshold: 0.5 });
  countEls.forEach(el => cIO.observe(el));
}
