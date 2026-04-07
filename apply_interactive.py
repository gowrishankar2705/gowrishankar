import re

try:
    with open('d:/Websites/portfolio/projects.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # --- CSS REPLACEMENT ---
    css_start = content.find('/* P1 - Energy Dashboard */')
    css_end = content.find('/* Responsive */')
    
    new_css = """/* INTERACTIVE CSS BLOCK */
    /* P1 - Energy Dashboard (Interactive Bars) */
    .p-vis-1 { background: #08101a; display: flex; align-items: flex-end; justify-content: center; gap: 8px; padding-bottom: 60px; perspective: 600px; }
    .i-bar { width: 30px; height: 20%; background: rgba(168, 85, 247, 0.2); border-top: 3px solid var(--primary); transition: 0.2s cubic-bezier(0.2, 0.8, 0.2, 1); box-shadow: 0 0 10px rgba(168,85,247,0); border-radius: 4px 4px 0 0; }
    .i-bar.active { background: rgba(168, 85, 247, 0.8); height: 80% !important; box-shadow: 0 0 30px var(--primary); z-index: 5; transform: scaleY(1.1) translateZ(20px); }

    /* P2 - Object Nav System (Cursor Tracking Reticle) */
    .p-vis-2 { background: #050505; align-items: center; justify-content: center; display: flex; position: relative; overflow: hidden; }
    .reticle-container { position: absolute; inset: 0; pointer-events: none; }
    .i-reticle { position: absolute; width: 100px; height: 100px; border: 1px solid var(--cyan); border-radius: 50%; transform: translate(-50%, -50%); transition: 0.1s linear; display: flex; justify-content: center; align-items: center; box-shadow: inset 0 0 30px rgba(16,185,129,0.2), 0 0 20px rgba(16,185,129,0.3); }
    .i-reticle::before, .i-reticle::after { content: ''; position: absolute; background: var(--cyan); }
    .i-reticle::before { width: 140%; height: 1px; }
    .i-reticle::after { height: 140%; width: 1px; }
    .target-overlay { position: absolute; font-family: var(--font-body); color: var(--cyan); font-size: 10px; pointer-events: none; transition: 0.1s linear; transform: translate(30px, -60px); }
    .p-vis-2:hover .i-reticle { width: 80px; height: 80px; box-shadow: inset 0 0 40px rgba(16,185,129,0.5), 0 0 30px rgba(16,185,129,0.6); }

    /* P3 - AI Assistant (Holographic Multi-Ring Parallax) */
    .p-vis-3 { background: #020408; align-items: center; justify-content: center; display: flex; perspective: 1000px; overflow: hidden; }
    .ai-holo-core { position: relative; width: 160px; height: 160px; transform-style: preserve-3d; transition: transform 0.2s cubic-bezier(0.2,0.8,0.2,1); pointer-events: none; }
    .i-ring { position: absolute; inset: 0; border-radius: 50%; border: 2px dashed rgba(168, 85, 247, 0.4); transform-style: preserve-3d; }
    .i-ring-1 { border: 2px solid rgba(168, 85, 247, 0.6); animation: spinRing 10s linear infinite; }
    .i-ring-2 { border: 4px dashed var(--cyan); transform: scale(0.8) rotateX(60deg) rotateY(30deg); animation: spinRing2 15s linear infinite reverse; }
    .i-ring-3 { border: 2px dotted var(--gold); transform: scale(0.6) rotateX(-45deg); animation: spinRing 8s linear infinite; }
    .ai-holo-dot { position: absolute; top:50%; left:50%; width: 20px; height: 20px; background: var(--white); box-shadow: 0 0 40px 20px var(--primary); border-radius: 50%; transform: translate(-50%,-50%); }
    @keyframes spinRing { to { transform: rotateZ(360deg); } }
    @keyframes spinRing2 { to { transform: scale(0.8) rotateX(60deg) rotateY(30deg) rotateZ(360deg); } }

    /* P4 - Component Detector (Interactive Inspection Grid) */
    .p-vis-4 { background: #1a1a1a; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 8px; padding: 40px; position: relative; }
    .comp-box { width: 60px; height: 60px; background: #0c0c0c; border: 1px solid #333; transition: all 0.2s; border-radius: 4px; display: flex; align-items: center; justify-content: center; }
    .comp-box.inspected { border-color: var(--cyan); background: rgba(16,185,129,0.1); box-shadow: 0 0 20px rgba(16,185,129,0.3); transform: scale(1.1); z-index: 5; }
    .comp-box.inspected::after { content: '✓'; color: var(--cyan); font-family: var(--font-disp); }

    /* P5 - Ecommerce (3D Holographic Tilt Card) */
    .p-vis-5 { background: var(--surface); display: flex; justify-content: center; align-items: center; perspective: 1000px; }
    .i-3d-card { width: 220px; height: 320px; background: rgba(25, 5, 43, 0.8); backdrop-filter: blur(10px); border: 1px solid var(--border); border-radius: 12px; transition: transform 0.15s cubic-bezier(0.2,0.8,0.2,1), box-shadow 0.15s; transform-style: preserve-3d; display: flex; flex-direction: column; padding: 20px; gap: 15px; position: relative; overflow: hidden; pointer-events: none; }
    .i-3d-glare { position: absolute; inset: 0; background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.2), transparent 60%); opacity: 0; transition: opacity 0.3s; pointer-events: none; mix-blend-mode: overlay; z-index: 10; }
    .p-vis-5:hover .i-3d-card { box-shadow: -20px 30px 50px rgba(0,0,0,0.5); }
    .p-vis-5:hover .i-3d-glare { opacity: 1; }
    .i-sneaker { flex: 1; background: rgba(168, 85, 247, 0.1); border-radius: 8px; transition: 0.3s; transform: translateZ(30px); border: 1px solid rgba(168, 85, 247, 0.2); }
    .i-card-lines { width: 80%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; transform: translateZ(20px); }
    .i-card-btn { width: 100%; padding: 10px; background: var(--primary); text-align: center; color: #fff; border-radius: 4px; font-family: var(--font-disp); font-size: 11px; font-weight: 700; transform: translateZ(40px); box-shadow: 0 5px 15px rgba(168, 85, 247, 0.4); }

    /* P6 - Turf Booking (Interactive Booking Matrix) */
    .p-vis-6 { background: #081a10; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; }
    .turf-matrix { display: grid; grid-template-columns: repeat(5, 1fr); gap: 5px; width: 80%; max-width: 300px; z-index: 2; padding: 20px; background: rgba(0,0,0,0.6); border: 1px solid rgba(16,185,129,0.3); border-radius: 8px; }
    .t-slot { height: 40px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; transition: 0.2s; display: flex; align-items: center; justify-content: center; font-family: var(--font-body); font-size: 9px; color: var(--muted); cursor: pointer !important; }
    .t-slot:hover { background: rgba(16, 185, 129, 0.8); color: #000; font-weight: bold; box-shadow: 0 0 15px var(--cyan); border-color: var(--cyan); transform: scale(1.1); }

    /* P7 - AR Indoor Navigation (Mouse-Driven Cube) */
    .p-vis-7 { background: #050514; perspective: 1200px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
    .i-ar-cube { width: 140px; height: 140px; transform-style: preserve-3d; transition: transform 0.1s linear; pointer-events: none; }
    .ar-face { position: absolute; width: 140px; height: 140px; border: 2px solid var(--primary); background: rgba(168, 85, 247, 0.05); box-shadow: inset 0 0 20px rgba(168, 85, 247, 0.2); display: flex; align-items: center; justify-content: center; color: var(--cyan); font-family: var(--font-disp); font-size: 10px; }
    .front  { transform: translateZ(70px); }
    .back   { transform: rotateY(180deg) translateZ(70px); }
    .right  { transform: rotateY(90deg) translateZ(70px); }
    .left   { transform: rotateY(-90deg) translateZ(70px); }
    .top    { transform: rotateX(90deg) translateZ(70px); }
    .bottom { transform: rotateX(-90deg) translateZ(70px); }
    
    /* P8 - Drone Scanner (Follow-Me Drone) */
    .p-vis-8 { background: #0d120a; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; }
    .drone-grid { position: absolute; inset: 0; background: linear-gradient(rgba(16,185,129,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(16,185,129,0.1) 1px, transparent 1px); background-size: 40px 40px; transform: perspective(500px) rotateX(60deg); transform-origin: top; animation: flyOver 3s infinite linear; pointer-events: none; }
    .i-drone { position: absolute; width: 50px; height: 50px; background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 24 24" fill="%2310b981" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v4h-2zm0 6h2v2h-2z"/></svg>') no-repeat center center; pointer-events: none; transform: translate(-50%, -50%); transition: 0.15s cubic-bezier(0.2,0.8,0.2,1); z-index: 5; filter: drop-shadow(0 10px 10px rgba(0,0,0,0.5)); }
    .i-drone-beam { position: absolute; top: 100%; left: 50%; transform: translateX(-50%); width: 0; height: 0; border-left: 60px solid transparent; border-right: 60px solid transparent; border-bottom: 200px solid rgba(16,185,129,0.15); pointer-events: none; }
    
    /* P9 - Smart Parking (Dynamic Allocation) */
    .p-vis-9 { background: #0a1410; display: flex; align-items: center; justify-content: center; }
    .i-parking-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; width: 240px; z-index: 2; perspective: 800px; }
    .i-spot { height: 120px; border: 2px dashed rgba(255,255,255,0.1); border-radius: 8px; position: relative; transition: 0.3s; transform-style: preserve-3d; cursor: pointer !important; display: flex; align-items: center; justify-content: center; }
    .i-spot.empty:hover { border-color: rgba(255, 0, 102, 0.5); box-shadow: inset 0 0 30px rgba(255,0,102,0.1); transform: translateZ(20px); }
    .i-spot.empty:hover::before { content: 'LOCK'; color: var(--gold); font-family: var(--font-disp); position: absolute; z-index: 5; font-size: 14px; text-shadow: 0 0 10px var(--gold); }
    .i-car { width: 45px; height: 90px; background: var(--cyan); border-radius: 6px; box-shadow: 0 10px 20px rgba(0,0,0,0.5); transition: 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); transform: scale(0.9); }
    
    """
    
    content = content[:css_start] + new_css + content[css_end:]
    
    # --- HTML REPLACEMENT ---
    # We will safely replace individual visualizer contexts using simple string replaces instead of regex to prevent breaking the divs.
    
    # P1
    content = content.replace(
        '<div class="bar-chart"></div><div class="bar-chart"></div><div class="bar-chart"></div><div class="bar-chart"></div><div class="bar-chart"></div>',
        ''.join([f'<div class="i-bar" data-idx="{i}"></div>' for i in range(10)])
    )
    
    # P2
    content = content.replace(
        '<div class="bbox"><div class="bbox-cross"></div></div>',
        '<div class="reticle-container"><div class="i-reticle"></div><div class="target-overlay">X:0 Y:0</div></div>'
    )
    
    # P3
    p3_old = '<div class="ai-core"></div>\n          <div class="ai-waves">\n            <div class="ai-wave-bar"></div><div class="ai-wave-bar"></div><div class="ai-wave-bar"></div>\n            <div class="ai-wave-bar"></div><div class="ai-wave-bar"></div><div class="ai-wave-bar"></div>\n          </div>'
    p3_new = '<div class="ai-holo-core"><div class="i-ring i-ring-1"></div><div class="i-ring i-ring-2"></div><div class="i-ring i-ring-3"></div><div class="ai-holo-dot"></div></div>'
    if p3_old in content:
        content = content.replace(p3_old, p3_new)
    else:
        # Fallback regex if spacing differs
        content = re.sub(r'<div class="ai-core"></div>.*?</div>\s*</div>', p3_new, content, flags=re.DOTALL)
        
    # P4
    p4_old = '<div class="comp-chip">\n            <div class="comp-detect"></div>\n            <div class="comp-pins"><div class="pin-row"><div class="pin"></div><div class="pin"></div><div class="pin"></div></div><div class="pin-row"><div class="pin"></div><div class="pin"></div><div class="pin"></div></div></div>\n          </div>'
    p4_new = ''.join(['<div class="comp-box"></div>' for _ in range(12)])
    if p4_old in content:
        content = content.replace(p4_old, p4_new)
    else:
        content = re.sub(r'<div class="comp-chip">.*?</div>\s*</div>', p4_new, content, flags=re.DOTALL)
        
    # P5
    p5_old = '<div class="shop-ui">\n            <div class="shop-img"></div>\n            <div class="shop-title"></div>\n            <div class="shop-btn">ADD TO CART</div>\n          </div>'
    p5_new = '<div class="i-3d-card"><div class="i-3d-glare"></div><div class="i-sneaker"></div><div class="i-card-lines"></div><div class="i-card-lines" style="width:50%"></div><div class="i-card-btn">ADD TO CART</div></div>'
    if p5_old in content:
        content = content.replace(p5_old, p5_new)
    else:
        content = re.sub(r'<div class="shop-ui">.*?</div>\s*</div>', p5_new, content, flags=re.DOTALL)

    # P6
    p6_old = '<div class="turf-wrap">\n            <div class="turf-top">\n              <div class="t-lines"></div><div class="t-circ"></div>\n            </div>\n            <div class="turf-bot">\n              <div class="cal-ui">\n                <div class="c-line" style="width:80%"></div>\n                <div class="c-line" style="width:100%"></div>\n                <div class="c-line" style="width:60%"></div>\n                <div class="cal-btn">BOOK SLOT</div>\n              </div>\n            </div>\n          </div>'
    p6_new = '<div class="turf-matrix">' + ''.join(['<div class="t-slot">8AM</div>', '<div class="t-slot">9AM</div>', '<div class="t-slot">10AM</div>', '<div class="t-slot">11AM</div>', '<div class="t-slot">12PM</div>', '<div class="t-slot">1PM</div>', '<div class="t-slot">2PM</div>', '<div class="t-slot">3PM</div>', '<div class="t-slot">4PM</div>', '<div class="t-slot">5PM</div>', '<div class="t-slot">6PM</div>', '<div class="t-slot">7PM</div>', '<div class="t-slot">8PM</div>', '<div class="t-slot">9PM</div>', '<div class="t-slot">10PM</div>']) + '</div>'
    if p6_old in content:
        content = content.replace(p6_old, p6_new)
    else:
        content = re.sub(r'<div class="turf-wrap">.*?</div>\n          </div>\n        </div>', p6_new, content, flags=re.DOTALL)
    # The P6 replace might need to be isolated, let's just do a targeted regex specifically over turf-wrap
    if 'turf-matrix' not in content:
        content = re.sub(r'<div class="turf-wrap">.*?(?=</div>\s*</div>\s*<div class="p-right">)', p6_new, content, flags=re.DOTALL)

    # P7
    content = content.replace('class="ar-cube"', 'class="i-ar-cube"')

    # P8
    p8_old = '<div class="drone-scanner"></div>\n          <div class="drone-target dt-1"></div>\n          <div class="drone-target dt-2"></div>'
    p8_new = '<div class="i-drone"><div class="i-drone-beam"></div></div>'
    if p8_old in content:
        content = content.replace(p8_old, p8_new)
    else:
        content = re.sub(r'<div class="drone-scanner"></div>.*?<div class="drone-target dt-2"></div>', p8_new, content, flags=re.DOTALL)
        
    # P9
    p9_old = '<div class="parking-grid">\n            <div class="spot empty"></div>\n            <div class="spot occ"><div class="car-p"></div></div>\n            <div class="spot empty"></div>\n            <div class="spot empty"></div>\n            <div class="spot occ anim-car"><div class="car-p"></div></div>\n            <div class="spot occ"><div class="car-p"></div></div>\n          </div>'
    p9_new = '<div class="i-parking-grid">' + ''.join(['<div class="i-spot empty"></div>', '<div class="i-spot occ"><div class="i-car" style="background:var(--muted)"></div></div>', '<div class="i-spot empty"></div>', '<div class="i-spot empty"></div>', '<div class="i-spot occ"><div class="i-car"></div></div>', '<div class="i-spot empty"></div>']) + '</div>'
    if p9_old in content:
        content = content.replace(p9_old, p9_new)
    else:
        content = re.sub(r'<div class="parking-grid">.*?</div>\n          </div>', p9_new, content, flags=re.DOTALL)

    # --- JS INJECTION ---
    js_code = """
      // INTERACTIVE PROJECTS JS
      const p1 = document.querySelector('.p-vis-1');
      if(p1) {
        const bars = p1.querySelectorAll('.i-bar');
        p1.addEventListener('mousemove', e => {
          const rect = p1.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const ratio = x / rect.width;
          const targetIdx = Math.floor(ratio * bars.length);
          bars.forEach((b, i) => {
            if(i === targetIdx) b.classList.add('active');
            else {
               b.classList.remove('active');
               const dist = Math.abs(i - targetIdx);
               b.style.height = Math.max(20, 50 - (dist*10)) + '%';
            }
          });
        });
        p1.addEventListener('mouseleave', () => {
          bars.forEach(b => { b.classList.remove('active'); b.style.height = '20%'; });
        });
      }

      const p2 = document.querySelector('.p-vis-2');
      if(p2) {
        const reticle = p2.querySelector('.i-reticle');
        const overlay = p2.querySelector('.target-overlay');
        p2.addEventListener('mousemove', e => {
          const rect = p2.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          reticle.style.left = x + 'px';
          reticle.style.top = y + 'px';
          overlay.style.left = x + 'px';
          overlay.style.top = y + 'px';
          overlay.innerText = `LOCK_X: ${Math.round(x)} \\nLOCK_Y: ${Math.round(y)}`;
        });
        p2.addEventListener('mouseleave', () => {
          reticle.style.left = '50%'; reticle.style.top = '50%';
          overlay.innerText = `SCANNING...`;
        });
      }

      const p3 = document.querySelector('.p-vis-3');
      if(p3) {
        const core = p3.querySelector('.ai-holo-core');
        p3.addEventListener('mousemove', e => {
          const rect = p3.getBoundingClientRect();
          const x = (e.clientX - rect.left) / rect.width - 0.5;
          const y = (e.clientY - rect.top) / rect.height - 0.5;
          core.style.transform = `rotateY(${x * 60}deg) rotateX(${-y * 60}deg)`;
        });
        p3.addEventListener('mouseleave', () => core.style.transform = 'rotateY(0) rotateX(0)');
      }

      const p4 = document.querySelector('.p-vis-4');
      if(p4) {
        const boxes = p4.querySelectorAll('.comp-box');
        boxes.forEach(b => {
          b.addEventListener('mouseenter', () => b.classList.add('inspected'));
          b.addEventListener('mouseleave', () => b.classList.remove('inspected'));
        });
      }

      const p5 = document.querySelector('.p-vis-5');
      if(p5) {
        const card = p5.querySelector('.i-3d-card');
        const glare = p5.querySelector('.i-3d-glare');
        p5.addEventListener('mousemove', e => {
          const rect = p5.getBoundingClientRect();
          const x = e.clientX - rect.left; const y = e.clientY - rect.top;
          const rotX = -((y / rect.height) - 0.5) * 40;
          const rotY = ((x / rect.width) - 0.5) * 40;
          card.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg) translateZ(20px)`;
          glare.style.transform = `translate(${x - rect.width/2}px, ${y - rect.height/2}px)`;
        });
        p5.addEventListener('mouseleave', () => { card.style.transform = `rotateX(0deg) rotateY(0deg) translateZ(0)`; });
      }

      const p7 = document.querySelector('.p-vis-7');
      if(p7) {
        const cube = p7.querySelector('.i-ar-cube');
        p7.addEventListener('mousemove', e => {
          const rect = p7.getBoundingClientRect();
          const x = (e.clientX - rect.left) / rect.width - 0.5;
          const y = (e.clientY - rect.top) / rect.height - 0.5;
          cube.style.transform = `rotateY(${x * 360}deg) rotateX(${-y * 360}deg)`;
        });
      }

      const p8 = document.querySelector('.p-vis-8');
      if(p8) {
        const drone = p8.querySelector('.i-drone');
        p8.addEventListener('mousemove', e => {
          const rect = p8.getBoundingClientRect();
          const x = e.clientX - rect.left; const y = e.clientY - rect.top;
          drone.style.left = x + 'px'; drone.style.top = y + 'px';
        });
      }
    """
    
    # Inject js_code immediately before the existing background canvas block
    if '// Background Canvas' in content:
        content = content.replace('// Background Canvas', js_code + '\n      // Background Canvas')

    with open('d:/Websites/portfolio/projects.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("projects.html successfully updated with high-end interactive visualizations.")
except Exception as e:
    import traceback
    traceback.print_exc()
