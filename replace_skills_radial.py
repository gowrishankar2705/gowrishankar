import os, re

def make_ring(name, pct, color_var):
    return f'''
          <div class="radial-node interactive" data-pct="{pct}">
              <div class="reactor-core" style="background: radial-gradient(circle, {color_var} 0%, transparent 70%);"></div>
              <svg viewBox="0 0 100 100" class="ring-svg">
                  <circle class="ring-bg" cx="50" cy="50" r="40"></circle>
                  <circle class="ring-fg" cx="50" cy="50" r="40" style="stroke: {color_var};"></circle>
                  <circle class="ring-tracker" cx="50" cy="50" r="46" style="stroke: {color_var};"></circle>
              </svg>
              <div class="ring-lbl">
                 <div class="rpct">0%</div>
                 <div class="rname">{name}</div>
              </div>
          </div>'''

core_html = ''.join([make_ring('Artificial Intelligence', 95, 'var(--primary)'), make_ring('Machine Learning', 90, 'var(--primary)'), make_ring('Data Analytics', 85, 'var(--primary)'), make_ring('SQL & Power BI', 85, 'var(--primary)')])
eng_html = ''.join([make_ring('Web Development', 90, 'var(--cyan)'), make_ring('App Development', 85, 'var(--cyan)'), make_ring('Backend', 85, 'var(--cyan)'), make_ring('UI/UX', 80, 'var(--cyan)'), make_ring('Product Dev', 85, 'var(--cyan)')])
tools_html = ''.join([make_ring('PyTorch / TF', 90, 'var(--gold)'), make_ring('OpenCV / YOLO', 85, 'var(--gold)'), make_ring('FastAPI', 85, 'var(--gold)'), make_ring('Docker', 80, 'var(--gold)'), make_ring('Git / GitHub', 95, 'var(--gold)')])

def replace_hud_radial():
    try:
        with open('d:/Websites/portfolio/skills.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. REPLACE HTML STRUCTURE
        html_start = content.find('<!-- HUD Skills Matrix -->')
        html_end = content.find('</section>', html_start) + len('</section>')
        
        new_html = f"""<!-- Sci-Fi Radial Core -->
    <section class="radial-sec">
      
      <div class="hud-nav reveal">
         <button class="hud-tab active interactive" data-trg="cat-core">CORE.exe</button>
         <button class="hud-tab interactive" data-trg="cat-eng">ENGINEERING.exe</button>
         <button class="hud-tab interactive" data-trg="cat-tools">TOOLS.exe</button>
      </div>

      <div class="hud-display reveal">
         <div class="hud-panel active" id="cat-core">
            <div class="radial-grid">{core_html}</div>
         </div>
         <div class="hud-panel" id="cat-eng">
            <div class="radial-grid">{eng_html}</div>
         </div>
         <div class="hud-panel" id="cat-tools">
            <div class="radial-grid">{tools_html}</div>
         </div>
      </div>

    </section>"""
        
        content = content[:html_start] + new_html + content[html_end:]


        # 2. REPLACE CSS
        css_start = content.find('/* Matrix Skills Grid */')
        css_end = content.find('/* TECH CONSTELLATION */', css_start)
        
        new_css = """/* Sci-Fi Radial HUD */
    .radial-sec { padding: 60px 5% 100px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; min-height: 80vh; }
    
    .hud-nav { display: flex; gap: 20px; margin-bottom: 60px; background: rgba(16, 3, 28, 0.6); padding: 10px 20px; border-radius: 40px; border: 1px solid var(--border); backdrop-filter: blur(10px); }
    .hud-tab { background: transparent; border: none; font-family: var(--font-disp); color: var(--muted); font-size: 14px; font-weight: 700; letter-spacing: 0.1em; padding: 12px 24px; border-radius: 30px; transition: all 0.3s cubic-bezier(0.16,1,0.3,1); position: relative; overflow: hidden; }
    .hud-tab::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent); transition: 0.5s; }
    .hud-tab:hover::before { left: 100%; }
    .hud-tab.active { background: rgba(168, 85, 247, 0.15); color: var(--white); box-shadow: 0 0 20px rgba(168, 85, 247, 0.3); }

    .hud-display { width: 100%; max-width: 1200px; position: relative; perspective: 1500px; }
    .hud-panel { display: none; width: 100%; animation: panelSpawn 0.6s cubic-bezier(0.16,1,0.3,1) forwards; }
    .hud-panel.active { display: block; }

    @keyframes panelSpawn { 
      0% { opacity: 0; transform: scale(0.9) translateY(40px) rotateX(10deg); filter: blur(10px) brightness(2) contrast(1.5) sepia(1); } 
      100% { opacity: 1; transform: scale(1) translateY(0) rotateX(0deg); filter: blur(0) brightness(1) contrast(1); } 
    }

    .radial-grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 50px; }
    
    .radial-node { width: 220px; height: 260px; display: flex; flex-direction: column; align-items: center; position: relative; transform-style: preserve-3d; transition: transform 0.2s linear; }
    .radial-node:hover { z-index: 10; }
    
    .reactor-core { position: absolute; top: 110px; left: 50%; transform: translate(-50%, -50%); width: 100px; height: 100px; border-radius: 50%; opacity: 0; pointer-events: none; transition: opacity 0.4s, transform 0.4s; filter: blur(15px); }
    .radial-node:hover .reactor-core { opacity: 0.6; transform: translate(-50%, -50%) scale(1.5); }
    
    .ring-svg { width: 180px; height: 180px; transform: rotate(-90deg); filter: drop-shadow(0 0 10px rgba(0,0,0,0.5)); transition: transform 0.4s cubic-bezier(0.16,1,0.3,1); }
    .radial-node:hover .ring-svg { transform: rotate(-90deg) scale(1.05) translateZ(30px); }
    
    circle { fill: transparent; stroke-width: 6; stroke-linecap: round; }
    .ring-bg { stroke: rgba(255,255,255,0.05); }
    .ring-fg { stroke-dasharray: 251.2; stroke-dashoffset: 251.2; transition: stroke-dashoffset 1.5s cubic-bezier(0.2, 0.8, 0.2, 1); filter: drop-shadow(0 0 8px currentColor); }
    
    .ring-tracker { stroke-width: 1; stroke-dasharray: 4 8; opacity: 0; transform-origin: 50px 50px; animation: trackerSpin 6s linear infinite; transition: opacity 0.4s; }
    .radial-node:hover .ring-tracker { opacity: 0.8; animation: trackerSpin 2s linear infinite; }
    @keyframes trackerSpin { 100% { transform: rotate(360deg); } }
    
    .ring-lbl { position: absolute; top: 110px; left: 50%; transform: translate(-50%, -50%); text-align: center; pointer-events: none; width: 100%; transition: transform 0.4s; }
    .radial-node:hover .ring-lbl { transform: translate(-50%, -50%) scale(1.1) translateZ(40px); text-shadow: 0 0 20px rgba(255,255,255,0.5); }
    
    .rpct { font-family: var(--font-disp); font-size: 28px; font-weight: 700; color: var(--white); line-height: 1; margin-bottom: 5px; }
    .rname { font-family: var(--font-body); font-size: 13px; color: var(--text); font-weight: 700; max-width: 160px; margin: 0 auto; line-height: 1.2; position: absolute; top: 90px; left: 50%; transform: translateX(-50%); width: 100%; }

    """
        content = content[:css_start] + new_css + content[css_end:]

        # 3. REPLACE JAVASCRIPT
        js_start = content.find('// 3D Matrix Skill Cards')
        if js_start == -1: js_start = content.find('// Matrix Skill Cards') 
        js_end = content.find('// Tech Constellation', js_start)
        
        new_js = """// Radial HUD Engine
      const hudTabs = document.querySelectorAll('.hud-tab');
      const hudPanels = document.querySelectorAll('.hud-panel');
      const circumference = 251.2;

      function activatePanel(targetId) {
         hudPanels.forEach(p => p.classList.remove('active'));
         const target = document.getElementById(targetId);
         target.classList.add('active');
         
         // Trigger rings
         target.querySelectorAll('.radial-node').forEach((node, i) => {
             const fg = node.querySelector('.ring-fg');
             const pctEl = node.querySelector('.rpct');
             const dataPct = parseInt(node.getAttribute('data-pct'));
             
             // Staggered execution
             setTimeout(() => {
                 fg.style.strokeDashoffset = circumference - (dataPct / 100) * circumference;
                 let cur = 0;
                 const inc = dataPct / 30;
                 const intv = setInterval(() => {
                     cur += inc;
                     if(cur >= dataPct) { cur = dataPct; clearInterval(intv); }
                     pctEl.innerText = Math.round(cur) + '%';
                 }, 30);
             }, i * 100);
         });
      }

      hudTabs.forEach(tab => {
          tab.addEventListener('click', () => {
              if(tab.classList.contains('active')) return;
              hudTabs.forEach(t => t.classList.remove('active'));
              tab.classList.add('active');
              activatePanel(tab.getAttribute('data-trg'));
          });
      });

      // 3D Radial Node Physics
      document.querySelectorAll('.radial-node').forEach(node => {
          node.addEventListener('mousemove', e => {
              const rect = node.getBoundingClientRect();
              const x = e.clientX - rect.left;
              const y = e.clientY - rect.top;
              const cx = rect.width / 2;
              const cy = rect.height / 2;
              
              const rotX = -((y - cy) / cy) * 30; // 30deg pop
              const rotY = ((x - cx) / cx) * 30;
              
              node.style.transform = `scale(1) rotateX(${rotX}deg) rotateY(${rotY}deg)`;
          });
          node.addEventListener('mouseleave', () => {
              node.style.transform = `scale(1) rotateX(0deg) rotateY(0deg)`;
          });
      });

      // Scroll Reveal Initial Trigger
      let initialTriggered = false;
      const rObs = new IntersectionObserver((entries) => {
          entries.forEach(e => {
              if(e.isIntersecting && !initialTriggered) {
                  initialTriggered = true;
                  activatePanel('cat-core'); 
              }
          });
      }, {threshold: 0.2});
      const disp = document.querySelector('.hud-display');
      if(disp) rObs.observe(disp);

      """
        
        content = content[:js_start] + new_js + content[js_end:]

        with open('d:/Websites/portfolio/skills.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("skills.html Radial HUD Matrix injected successfully.")
        
    except Exception as e:
        import traceback
        traceback.print_exc()

replace_hud_radial()
