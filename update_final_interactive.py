import os

def update_skills():
    try:
        with open('d:/Websites/portfolio/skills.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Insert CSS
        if '.sk-bar::after' not in content:
            css_insert = "\n    .sk-bar::after { content: ''; position: absolute; top: 0; left: var(--x, 0); width: 80px; height: 100%; background: radial-gradient(circle, rgba(255,255,255,0.9), transparent); transform: translateX(-50%); mix-blend-mode: overlay; pointer-events: none; opacity: 0; transition: opacity 0.3s; }\n    .sk-bar.h-active::after { opacity: 1; }"
            content = content.replace('.sk-pct { flex: 0 0 50px; text-align: right; font-size: 13px; color: var(--gold); }', '.sk-pct { flex: 0 0 50px; text-align: right; font-size: 13px; color: var(--gold); }' + css_insert)

        # Replace Accordion JS for text counter
        old_acc_js = """      // Accordion
      document.querySelectorAll('.acc-head').forEach(head => {
        head.addEventListener('click', () => {
          const item = head.parentElement;
          item.classList.toggle('open');
          if(item.classList.contains('open')) {
            // trigger bar fills
            setTimeout(() => {
              item.querySelectorAll('.sk-fill').forEach(fill => {
                fill.style.width = fill.getAttribute('data-w');
              });
            }, 100);
          } else {
             item.querySelectorAll('.sk-fill').forEach(fill => fill.style.width = '0%');
          }
        });
      });"""

        new_acc_js = """      // Accordion
      document.querySelectorAll('.acc-head').forEach(head => {
        head.addEventListener('click', () => {
          const item = head.parentElement;
          item.classList.toggle('open');
          if(item.classList.contains('open')) {
            setTimeout(() => {
              item.querySelectorAll('.skill-row').forEach(row => {
                const fill = row.querySelector('.sk-fill');
                const tw = fill.getAttribute('data-w');
                fill.style.width = tw;
                const pctEl = row.querySelector('.sk-pct');
                const targetPct = parseInt(tw);
                let cur = 0;
                const inc = targetPct / 30;
                const intv = setInterval(() => {
                    cur += inc;
                    if(cur >= targetPct) { cur = targetPct; clearInterval(intv); }
                    pctEl.innerText = Math.round(cur) + '%';
                }, 40);
              });
            }, 100);
          } else {
             item.querySelectorAll('.sk-fill').forEach(fill => fill.style.width = '0%');
             item.querySelectorAll('.sk-pct').forEach(p => p.innerText = '0%');
          }
        });
      });
      
      // Bar Mouse Tracker
      document.querySelectorAll('.sk-bar').forEach(bar => {
         bar.addEventListener('mousemove', e => {
            const rect = bar.getBoundingClientRect();
            const x = e.clientX - rect.left;
            bar.style.setProperty('--x', `${x}px`);
            if(!bar.classList.contains('h-active')) bar.classList.add('h-active');
         });
         bar.addEventListener('mouseleave', () => bar.classList.remove('h-active'));
      });"""

        if old_acc_js in content:
            content = content.replace(old_acc_js, new_acc_js)
            
        with open('d:/Websites/portfolio/skills.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated skills.html")
    except Exception as e:
        print("Error updating skills:", e)

def update_contact():
    try:
        with open('d:/Websites/portfolio/contact.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Insert CSS
        if 'perspective: 1500px;' not in content:
            content = content.replace('.contact-right { flex: 0 0 50%; max-width: 600px; }', '.contact-right { flex: 0 0 50%; max-width: 600px; perspective: 1500px; transform-style: preserve-3d; }')
            content = content.replace('.term-window { background: rgba(5,10,20,0.8); border: 1px solid var(--border); border-radius: 6px; overflow: hidden; backdrop-filter: blur(10px); box-shadow: 0 20px 40px rgba(0,0,0,0.5); }', '.term-window { background: rgba(5,10,20,0.8); border: 1px solid var(--border); border-radius: 6px; overflow: hidden; backdrop-filter: blur(10px); box-shadow: 0 20px 40px rgba(0,0,0,0.5); transition: transform 0.15s linear, box-shadow 0.15s linear; transform-style: preserve-3d; }')
            content = content.replace('.g-link { font-family: var(--font-disp); font-size: clamp(40px, 5vw, 72px); font-weight: 700; color: transparent; -webkit-text-stroke: 1.5px var(--muted); text-decoration: none; padding: 20px 0; border-bottom: 1px solid var(--border); transition: 0.3s; position: relative; overflow: hidden; display: block; line-height: 1.1; }', '.g-link { font-family: var(--font-disp); font-size: clamp(40px, 5vw, 72px); font-weight: 700; color: transparent; -webkit-text-stroke: 1.5px var(--muted); text-decoration: none; padding: 20px 0; border-bottom: 1px solid var(--border); transition: color 0.3s, padding 0.3s, border 0.3s, text-shadow 0.3s, transform 0.15s cubic-bezier(0.2,0.8,0.2,1); position: relative; overflow: hidden; display: block; line-height: 1.1; }')
        
        # Insert JS
        js_code = """
      // INTERACTIVITY: CONTACT PAGE
      const cdRight = document.querySelector('.contact-right');
      const term = document.querySelector('.term-window');
      if(cdRight && term) {
        cdRight.addEventListener('mousemove', e => {
          const rect = cdRight.getBoundingClientRect();
          const x = (e.clientX - rect.left) / rect.width - 0.5;
          const y = (e.clientY - rect.top) / rect.height - 0.5;
          term.style.transform = `rotateY(${x * 30}deg) rotateX(${-y * 30}deg) translateZ(20px)`;
          term.style.boxShadow = `${-x*40}px ${-y*40}px 60px rgba(0,0,0,0.6)`;
        });
        cdRight.addEventListener('mouseleave', () => {
          term.style.transform = `rotateY(0deg) rotateX(0deg) translateZ(0)`;
          term.style.boxShadow = `0 20px 40px rgba(0,0,0,0.5)`;
        });
      }

      document.querySelectorAll('.g-link').forEach(link => {
        link.addEventListener('mousemove', e => {
          const rect = link.getBoundingClientRect();
          const x = (e.clientX - rect.left) - rect.width/2;
          const y = (e.clientY - rect.top) - rect.height/2;
          link.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px)`;
        });
        link.addEventListener('mouseleave', () => {
          link.style.transform = `translate(0px, 0px)`;
        });
      });
      """

        if '// INTERACTIVITY: CONTACT PAGE' not in content:
            content = content.replace('// Background Canvas', js_code + '\n      // Background Canvas')

        with open('d:/Websites/portfolio/contact.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated contact.html")
    except Exception as e:
        print("Error updating contact:", e)

update_skills()
update_contact()
