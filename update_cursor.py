import os, glob, re

files = glob.glob('d:/Websites/portfolio/*.html')

css_targ = 'cursor: none !important;'
css_repl = 'cursor: crosshair; } a, button, .interactive, input, textarea, .story-card, .val-panel, .thumb { cursor: pointer;'

dot_html_targ = '<div class="cursor-dot"></div>'

cp_css = '''.cursor-ring { width: 36px; height: 36px; border: 1px solid var(--primary); border-radius: 50%; position: fixed; pointer-events: none; z-index: 9999; transform: translate(-50%, -50%); transition: width 0.2s, height 0.2s, background 0.2s; }
    .click-pulse { position: fixed; width: 20px; height: 20px; border: 2px solid var(--cyan); border-radius: 50%; transform: translate(-50%, -50%); pointer-events: none; z-index: 10000; animation: clickExpand 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
    @keyframes clickExpand { 0% { width: 20px; height: 20px; opacity: 1; border-width: 2px; } 100% { width: 80px; height: 80px; opacity: 0; border-width: 0px; box-shadow: 0 0 20px var(--primary); } }'''

js_repl = '''      // Cursor & Click Pulse
      const ring = document.querySelector('.cursor-ring');
      if (window.matchMedia("(pointer: fine)").matches && ring) {
        let mouseX = window.innerWidth/2, mouseY = window.innerHeight/2;
        let ringX = mouseX, ringY = mouseY;
        window.addEventListener('mousemove', e => { mouseX = e.clientX; mouseY = e.clientY; });
        function loop() {
          ringX += (mouseX - ringX) * 0.15; ringY += (mouseY - ringY) * 0.15;
          ring.style.transform = `translate(${ringX}px, ${ringY}px) translate(-50%, -50%)`;
          requestAnimationFrame(loop);
        }
        requestAnimationFrame(loop);
        document.querySelectorAll('a, button, input, textarea, .interactive, .thumb, .story-card, .val-panel').forEach(el => {
          el.addEventListener('mouseenter', () => ring.classList.add('active'));
          el.addEventListener('mouseleave', () => ring.classList.remove('active'));
        });
        
        window.addEventListener('click', e => {
            const p = document.createElement('div');
            p.classList.add('click-pulse');
            p.style.left = e.clientX + 'px';
            p.style.top = e.clientY + 'px';
            document.body.appendChild(p);
            setTimeout(() => p.remove(), 600);
        });
      }'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    og = content
    content = content.replace(css_targ, css_repl)
    content = content.replace(dot_html_targ, '')
    
    # regex hack for css
    content = re.sub(r'\.cursor-dot \{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.cursor-dot\.active \{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.cursor-ring \{.*?\}', cp_css, content, flags=re.DOTALL)
    
    # js replace
    content = re.sub(r'// Cursor\s+const dot = document\.querySelector\(\'\.cursor-dot\'\);.*?\}\);(?:\n\s*\})?', js_repl + '\n', content, flags=re.DOTALL)

    if og != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Updated', f)
    else:
        print('No change', f)
