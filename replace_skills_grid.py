import os, re

def redesign_skills():
    try:
        with open('d:/Websites/portfolio/skills.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. REPLACE HTML STRUCTURE
        html_start = content.find('<!-- Skill Bars -->')
        html_end = content.find('</section>', html_start) + len('</section>')
        
        new_html = """<!-- HUD Skills Matrix -->
    <section class="hud-sec">
      <div class="skills-grid">
        
        <!-- Core -->
        <div class="cyber-card reveal-card">
          <div class="card-glare"></div>
          <div class="card-head">
            <div class="acc-title"><i class="fa-solid fa-brain"></i> Core</div>
            <div class="acc-badge">EXPERT</div>
          </div>
          <div class="card-body">
            <div class="skill-row"><div class="sk-name">Artificial Intelligence</div><div class="sk-bar"><div class="sk-fill" data-w="95%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">Machine Learning</div><div class="sk-bar"><div class="sk-fill" data-w="90%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">Data Analytics & Science</div><div class="sk-bar"><div class="sk-fill" data-w="85%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">SQL & Power BI</div><div class="sk-bar"><div class="sk-fill" data-w="85%"></div></div><div class="sk-pct">0%</div></div>
          </div>
        </div>

        <!-- Engineering -->
        <div class="cyber-card reveal-card" style="transition-delay:0.1s;">
          <div class="card-glare"></div>
          <div class="card-head">
            <div class="acc-title"><i class="fa-solid fa-code"></i> Engineering</div>
            <div class="acc-badge" style="border-color:var(--primary); color:var(--primary); background:rgba(168,85,247,0.05);">PROFICIENT</div>
          </div>
          <div class="card-body">
            <div class="skill-row"><div class="sk-name">Web Development</div><div class="sk-bar"><div class="sk-fill" data-w="90%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">App Development</div><div class="sk-bar"><div class="sk-fill" data-w="85%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">Backend (Node.js, Flask)</div><div class="sk-bar"><div class="sk-fill" data-w="85%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">UI/UX</div><div class="sk-bar"><div class="sk-fill" data-w="80%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">Product Development</div><div class="sk-bar"><div class="sk-fill" data-w="85%"></div></div><div class="sk-pct">0%</div></div>
          </div>
        </div>

        <!-- Tools & Libraries -->
        <div class="cyber-card reveal-card" style="transition-delay:0.2s;">
          <div class="card-glare"></div>
          <div class="card-head">
            <div class="acc-title"><i class="fa-solid fa-toolbox"></i> Tools</div>
            <div class="acc-badge" style="border-color:var(--gold); color:var(--gold); background:rgba(244,63,94,0.05);">ADVANCED</div>
          </div>
          <div class="card-body">
            <div class="skill-row"><div class="sk-name">PyTorch / TensorFlow</div><div class="sk-bar"><div class="sk-fill" data-w="90%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">OpenCV / YOLO</div><div class="sk-bar"><div class="sk-fill" data-w="85%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">Streamlit / FastAPI</div><div class="sk-bar"><div class="sk-fill" data-w="85%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">Docker</div><div class="sk-bar"><div class="sk-fill" data-w="80%"></div></div><div class="sk-pct">0%</div></div>
            <div class="skill-row"><div class="sk-name">Git / GitHub</div><div class="sk-bar"><div class="sk-fill" data-w="95%"></div></div><div class="sk-pct">0%</div></div>
          </div>
        </div>

      </div>
    </section>"""
        
        content = content[:html_start] + new_html + content[html_end:]


        # 2. REPLACE CSS
        # Removing old accordion styles and injecting new Grid/Cards CSS
        css_start = content.find('/* SKILL BARS ACCORDION */')
        css_end = content.find('/* TECH CONSTELLATION */', css_start)
        
        new_css = """/* Matrix Skills Grid */
    .hud-sec { padding: 80px 5%; margin: 0 auto; min-height: 80vh; display: flex; align-items: center; }
    .skills-grid { width: 100%; display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; }
    
    .cyber-card { background: rgba(8, 15, 30, 0.4); border: 1px solid var(--border); border-radius: 6px; overflow: hidden; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); position: relative; transform-style: preserve-3d; transition: transform 0.15s linear, box-shadow 0.15s linear, border-color 0.3s; transform: perspective(1500px); }
    .cyber-card:hover { border-color: rgba(16, 185, 129, 0.3); z-index: 10; }
    .card-glare { position: absolute; inset: 0; background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.08), transparent 50%); opacity: 0; pointer-events: none; mix-blend-mode: overlay; z-index: 10; transition: opacity 0.3s; }
    .cyber-card:hover .card-glare { opacity: 1; }
    
    .card-head { padding: 30px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed var(--border); background: rgba(168, 85, 247, 0.02); }
    .acc-title { font-family: var(--font-disp); font-size: 20px; font-weight: 700; color: var(--white); display: flex; align-items: center; gap: 12px; }
    .acc-title i { color: var(--cyan); width: 24px; text-align: center; }
    .acc-badge { font-family: var(--font-disp); font-size: 10px; padding: 4px 10px; border: 1px solid var(--cyan); color: var(--cyan); border-radius: 2px; letter-spacing: 0.15em; background: rgba(0,212,255,0.05); }
    
    .card-body { padding: 30px; }
    .skill-row { margin-bottom: 24px; font-family: var(--font-body); }
    .skill-row:last-child { margin-bottom: 0; }
    .sk-name { font-size: 13px; color: var(--white); margin-bottom: 8px; font-weight: 700; letter-spacing: 0.05em; display:flex; justify-content:space-between; }
    
    .sk-bar { width: 100%; height: 8px; background: rgba(255,255,255,0.04); border-radius: 1px; position: relative; overflow: hidden; }
    .sk-fill { position: absolute; left: 0; top: 0; bottom: 0; width: 0%; background: linear-gradient(90deg, var(--primary), var(--cyan)); transition: width 1.5s cubic-bezier(0.16,1,0.3,1); border-radius: 1px; -webkit-mask-image: repeating-linear-gradient(to right, #000 0, #000 6px, transparent 6px, transparent 8px); mask-image: repeating-linear-gradient(to right, #000 0, #000 6px, transparent 6px, transparent 8px); }
    .sk-pct { font-size: 12px; color: var(--gold); }
    
    .sk-bar::after { content: ''; position: absolute; top: 0; left: var(--x, 0); width: 150px; height: 100%; background: radial-gradient(circle, rgba(255,255,255,0.95), transparent); transform: translateX(-50%); mix-blend-mode: overlay; pointer-events: none; opacity: 0; transition: opacity 0.3s; }
    .sk-bar.h-active::after { opacity: 1; }

    .reveal-card { opacity: 0; transform: translateY(40px); transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1); filter: blur(4px); }
    .reveal-card.visible { opacity: 1; transform: translateY(0); filter: blur(0); }
    
    """
        content = content[:css_start] + new_css + content[css_end:]

        # Clean up old mobile CSS specific to acc
        content = content.replace('.acc-head { flex-direction: column; align-items: flex-start; gap: 15px; }', '')
        content = content.replace('.skill-row { flex-direction: column; align-items: flex-start; gap: 10px; }', '')
        content = content.replace('.sk-name { flex: auto; }', '')


        # 3. REPLACE JAVASCRIPT
        js_accordion_rx = re.compile(r'// Accordion.*?// Tech Constellation', re.DOTALL)
        
        new_js = """// 3D Matrix Skill Cards
      const cyberCards = document.querySelectorAll('.cyber-card');
      cyberCards.forEach(card => {
        const glare = card.querySelector('.card-glare');
        card.addEventListener('mousemove', e => {
          const rect = card.getBoundingClientRect();
          const x = (e.clientX - rect.left);
          const y = (e.clientY - rect.top);
          const cx = rect.width / 2;
          const cy = rect.height / 2;
          
          const rotX = -((y - cy) / cy) * 15;
          const rotY = ((x - cx) / cx) * 15;
          
          card.style.transform = `perspective(1000px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale3d(1.02, 1.02, 1.02)`;
          card.style.boxShadow = `${-rotY*2}px ${rotX*2}px 30px rgba(168, 85, 247, 0.15)`;
          if(glare) glare.style.transform = `translate(${x - cx}px, ${y - cy}px)`;
        });
        card.addEventListener('mouseleave', () => {
          card.style.transform = `perspective(1500px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
          card.style.boxShadow = `0 10px 30px rgba(0,0,0,0.5)`;
        });
      });

      // Segmented Bar Glow Trackers
      document.querySelectorAll('.sk-bar').forEach(bar => {
         bar.addEventListener('mousemove', e => {
            const rect = bar.getBoundingClientRect();
            const x = e.clientX - rect.left;
            bar.style.setProperty('--x', `${x}px`);
            if(!bar.classList.contains('h-active')) bar.classList.add('h-active');
         });
         bar.addEventListener('mouseleave', () => bar.classList.remove('h-active'));
      });

      // HUD Scroll Reveal Engine
      const hudObs = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if(e.isIntersecting) {
            e.target.classList.add('visible');
            // Trigger numbers & bars inside this card
            e.target.querySelectorAll('.skill-row').forEach(row => {
               const fill = row.querySelector('.sk-fill');
               const tw = fill.getAttribute('data-w');
               if(fill.style.width === tw) return; // already run
               
               fill.style.width = tw;
               const pctEl = row.parentElement.querySelector('.sk-pct');
               const targetPct = parseInt(tw);
               let cur = 0;
               const inc = targetPct / 20;
               const intv = setInterval(() => {
                   cur += inc;
                   if(cur >= targetPct) { cur = targetPct; clearInterval(intv); }
                   pctEl.innerText = Math.round(cur) + '%';
               }, 30);
            });
          }
        });
      }, {threshold: 0.15});
      document.querySelectorAll('.reveal-card').forEach(el => hudObs.observe(el));

      // Tech Constellation"""
        
        content = js_accordion_rx.sub(new_js, content)

        # Move .sk-pct into the .sk-name wrapper so it justifies properly
        content = content.replace('<div class="sk-name">', '<div class="sk-name"><span>')
        content = content.replace('</div><div class="sk-bar">', '</span><div class="sk-pct">0%</div></div><div class="sk-bar">')
        content = content.replace('</div><div class="sk-pct">0%</div></div>', '</div></div>')

        with open('d:/Websites/portfolio/skills.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("skills.html strictly refactored for 3D Cyber Grid integration.")
        
    except Exception as e:
        import traceback
        traceback.print_exc()

redesign_skills()
