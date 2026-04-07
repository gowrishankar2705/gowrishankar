import os

def redesign_P4_P5_Neural():
    # 1. UPDATE PROJECTS.HTML
    try:
        with open('d:/Websites/portfolio/projects.html', 'r', encoding='utf-8') as f:
            p_content = f.read()

        # Update P4 HTML
        p4_html_old = '<div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div>'
        p4_html_new = '<div class="p4-board">\n            <div class="p4-scanner"></div>\n            <div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div><div class="comp-box"></div>\n          </div>'
        p_content = p_content.replace(p4_html_old, p4_html_new)

        # Update P5 HTML
        p5_html_old = '<div class="i-3d-card"><div class="i-3d-glare"></div><div class="i-sneaker"></div><div class="i-card-lines"></div><div class="i-card-lines" style="width:50%"></div><div class="i-card-btn">ADD TO CART</div></div>'
        p5_html_new = '<div class="sw-scene">\n             <div class="sw-sneaker"></div>\n             <div class="sw-ui-title">XR SPEED TRAINER</div>\n             <div class="sw-ui-price">$149.00</div>\n             <div class="sw-ui-btn interactive">ADD TO CART</div>\n          </div>'
        p_content = p_content.replace(p5_html_old, p5_html_new)

        # Update CSS
        p_css_start = p_content.find('/* P4 - Component Detector (Interactive Inspection Grid) */')
        p_css_end = p_content.find('/* P6 - Turf Booking (Interactive Booking Matrix) */')
        
        new_project_css = """/* P4 - Component Detector (Scanner Engine) */
    .p-vis-4 { background: #0c0c0c; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; }
    .p4-board { position: relative; width: 340px; height: 260px; background: rgba(16, 185, 129, 0.02); border: 2px solid rgba(16,185,129,0.1); border-radius: 8px; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 10px; padding: 20px; box-shadow: inset 0 0 40px rgba(0,0,0,0.8); }
    .p4-scanner { position: absolute; top: 0; bottom: 0; left: 0; width: 4px; background: var(--cyan); box-shadow: 0 0 20px 5px rgba(16,185,129,0.5), inset 0 0 10px #fff; z-index: 10; animation: scanSweep 3s ease-in-out infinite alternate; pointer-events: none; }
    @keyframes scanSweep { 0% { left: 0%; opacity: 0; } 10% { opacity: 1; } 90% { opacity: 1; } 100% { left: 100%; opacity: 0; } }
    .comp-box { width: 60px; height: 60px; background: #050505; border: 1px dashed #333; transition: all 0.1s; border-radius: 4px; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; }
    .comp-box::before { content: ''; position: absolute; inset: 0; background: radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%); opacity: 0; transition: 0.1s; }
    .comp-box.inspected { border: 2px solid var(--cyan); box-shadow: 0 0 15px rgba(16,185,129,0.3); transform: scale(1.05); z-index: 5; }
    .comp-box.inspected::before { opacity: 1; }
    .comp-box.inspected::after { content: ''; position: absolute; width: 10px; height: 10px; border-top: 2px solid var(--cyan); border-left: 2px solid var(--cyan); top: 5px; left: 5px; }
    
    /* P5 - Ecommerce (3D Exploded View) */
    .p-vis-5 { background: var(--surface); display: flex; justify-content: center; align-items: center; perspective: 1200px; overflow: hidden; }
    .sw-scene { width: 300px; height: 300px; position: relative; transform-style: preserve-3d; transition: transform 0.1s linear; pointer-events: none; }
    .sw-sneaker { position: absolute; top: 50%; left: 50%; width: 220px; height: 120px; background: linear-gradient(135deg, rgba(168,85,247,0.8), rgba(244,63,94,0.8)); transform: translate(-50%, -50%) translateZ(0px) rotate(-15deg); border-radius: 120px 60px 40px 20px; box-shadow: 0 30px 40px rgba(0,0,0,0.8), inset 0 10px 20px rgba(255,255,255,0.2); pointer-events: auto; }
    .sw-sneaker::after { content: ''; position: absolute; bottom: -20px; left: 10%; width: 80%; height: 20px; background: rgba(0,0,0,0.5); filter: blur(10px); border-radius: 50%; transform: rotate(15deg); }
    .sw-ui-title { position: absolute; top: 40px; left: 0px; font-family: var(--font-disp); font-size: 24px; font-weight: 900; color: var(--white); text-shadow: 0 10px 20px rgba(0,0,0,0.5); transform: translateZ(60px); letter-spacing: 0.1em; pointer-events: none; }
    .sw-ui-price { position: absolute; top: 75px; left: 0px; font-family: var(--font-body); font-size: 16px; color: var(--gold); font-weight: 700; transform: translateZ(80px); background: rgba(0,0,0,0.6); padding: 5px 10px; border-radius: 4px; pointer-events: none; border: 1px solid rgba(244,63,94,0.3); }
    .sw-ui-btn { position: absolute; bottom: 40px; right: 0px; background: var(--cyan); color: #000; padding: 12px 24px; font-family: var(--font-disp); font-size: 12px; font-weight: 900; border-radius: 30px; transform: translateZ(100px); box-shadow: 0 15px 25px rgba(16,185,129,0.3); pointer-events: auto; transition: 0.2s; }
    .sw-ui-btn:hover { background: var(--white); transform: translateZ(110px) scale(1.05); }

    """
        p_content = p_content[:p_css_start] + new_project_css + p_content[p_css_end:]

        # Update JS in projects.html
        p_js_start = p_content.find('// 3D Tilt P5')
        p_js_end = p_content.find('// P7 Drone', p_js_start)
        
        new_project_js = """// P4 Scanner Logic
      const p4Vis = document.querySelector('.p-vis-4');
      const p4Scanner = document.querySelector('.p4-scanner');
      const compBoxes = document.querySelectorAll('.comp-box');
      if(p4Vis && p4Scanner) {
          function checkScanner() {
              const sRect = p4Scanner.getBoundingClientRect();
              compBoxes.forEach(box => {
                  const bRect = box.getBoundingClientRect();
                  // if scanner X is inside the box X bounds
                  if(sRect.left > bRect.left && sRect.right < bRect.right) {
                      box.classList.add('inspected');
                  } else {
                      box.classList.remove('inspected');
                  }
              });
              requestAnimationFrame(checkScanner);
          }
          checkScanner();
      }

      // P5 Exploded 3D Mousemove
      const p5Vis = document.querySelector('.p-vis-5');
      const swScene = document.querySelector('.sw-scene');
      if(p5Vis && swScene) {
          p5Vis.addEventListener('mousemove', e => {
              const rect = p5Vis.getBoundingClientRect();
              const x = e.clientX - rect.left;
              const y = e.clientY - rect.top;
              const cx = rect.width / 2;
              const cy = rect.height / 2;
              
              const rotX = -((y - cy) / cy) * 20; 
              const rotY = ((x - cx) / cx) * 35; // major Y rotation
              
              swScene.style.transform = `scale(1.1) rotateX(${rotX}deg) rotateY(${rotY}deg)`;
          });
          p5Vis.addEventListener('mouseleave', () => {
              swScene.style.transform = `scale(1) rotateX(0deg) rotateY(0deg)`;
          });
      }

      """
        if p_js_start != -1:
            p_content = p_content[:p_js_start] + new_project_js + p_content[p_js_end:]
        else:
            # Fallback if comment not exactly found
            # We append it where appropriate
            pass

        with open('d:/Websites/portfolio/projects.html', 'w', encoding='utf-8') as f:
            f.write(p_content)


        # 2. UPDATE SKILLS.HTML
        with open('d:/Websites/portfolio/skills.html', 'r', encoding='utf-8') as f:
            s_content = f.read()

        s_html_old = '<!-- Tech Vector Canvas -->\n    <section class="constellation" id="constellation">\n      <canvas id="const-canvas"></canvas>\n      <div class="const-overlay">\n         <h2>DATA STREAM</h2>\n         <p>Intercepting tech stack telemetry...</p>\n      </div>\n    </section>'
        s_html_new = """<!-- Neural Network Pipeline -->
    <section class="neural-sec" id="neural-net">
      <canvas id="nn-canvas"></canvas>
      <div class="nn-overlay">
         <h2>NEURAL SYNC</h2>
         <p>Initializing synaptic pathway mapping...</p>
      </div>
      <div class="nn-layers-dom">
         <div class="nn-col">
            <div class="nn-node interactive" data-layer="0"><i class="fa-solid fa-microphone"></i> Audio</div>
            <div class="nn-node interactive" data-layer="0"><i class="fa-solid fa-camera"></i> Vision</div>
            <div class="nn-node interactive" data-layer="0"><i class="fa-solid fa-font"></i> NLP</div>
         </div>
         <div class="nn-col">
            <div class="nn-node interactive hidden-node" data-layer="1">CNN</div>
            <div class="nn-node interactive hidden-node" data-layer="1">LSTM</div>
            <div class="nn-node interactive hidden-node" data-layer="1">Transformers</div>
            <div class="nn-node interactive hidden-node" data-layer="1">Dense</div>
         </div>
         <div class="nn-col">
            <div class="nn-node interactive" data-layer="2"><i class="fa-solid fa-bullseye"></i> Predict</div>
            <div class="nn-node interactive" data-layer="2"><i class="fa-solid fa-robot"></i> Act</div>
         </div>
      </div>
    </section>"""
        
        s_content = s_content.replace(s_html_old, s_html_new)

        s_css_start = s_content.find('/* TECH VECTOR CANVAS */')
        s_css_end = s_content.find('@media (max-width: 900px)', s_css_start)
        
        s_css_new = """/* NEURAL NETWORK PIPELINE */
    .neural-sec { min-height: 100vh; position: relative; overflow: hidden; background: #010204; border-top: 1px solid var(--border); display: flex; align-items: center; justify-content: center; }
    #nn-canvas { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; filter: drop-shadow(0 0 5px rgba(168,85,247,0.5)); }
    .nn-overlay { position: absolute; top: 10%; z-index: 2; text-align: center; pointer-events: none; opacity: 0.1; transition: opacity 0.5s; }
    .neural-sec:hover .nn-overlay { opacity: 0.8; }
    .nn-overlay h2 { font-family: var(--font-disp); font-size: clamp(40px, 8vw, 100px); -webkit-text-stroke: 1px var(--primary); color: transparent; letter-spacing: 0.1em; margin-bottom: 20px; }
    .nn-overlay p { font-family: var(--font-body); color: var(--white); letter-spacing: 0.2em; text-transform: uppercase; text-shadow: 0 0 10px var(--primary); }
    
    .nn-layers-dom { position: relative; z-index: 5; width: 80%; max-width: 900px; height: 60vh; display: flex; justify-content: space-between; align-items: stretch; }
    .nn-col { display: flex; flex-direction: column; justify-content: space-evenly; align-items: center; }
    .nn-node { background: rgba(16, 3, 28, 0.8); border: 2px solid var(--primary); border-radius: 30px; padding: 12px 24px; font-family: var(--font-disp); font-size: 12px; font-weight: 700; color: var(--white); letter-spacing: 0.1em; transition: all 0.3s; position: relative; display: flex; gap: 8px; align-items: center; box-shadow: 0 0 15px rgba(168,85,247,0.2); }
    .hidden-node { border-radius: 50%; width: 70px; height: 70px; display: flex; justify-content: center; align-items: center; text-align: center; font-size: 9px; padding: 10px; background: rgba(16,185,129,0.05); border-color: rgba(16,185,129,0.5); color: var(--cyan); }
    
    .nn-node:hover { transform: scale(1.15) translateZ(20px); background: var(--primary); color: #000; box-shadow: 0 0 30px var(--primary); }
    .hidden-node:hover { background: var(--cyan); color: #000; box-shadow: 0 0 30px var(--cyan); }

    """
        s_content = s_content[:s_css_start] + s_css_new + s_content[s_css_end:]

        s_js_start = s_content.find('// Tech Vector Gravity Canvas')
        s_js_end = s_content.find('});\n  </script>', s_js_start)
        
        s_js_new = """// Neural Network Pathway Engine
      const nnCanvas = document.getElementById('nn-canvas');
      const nnSec = document.getElementById('neural-net');
      if(nnCanvas && nnSec) {
          const ctx = nnCanvas.getContext('2d');
          let cw = nnCanvas.width = nnSec.offsetWidth;
          let ch = nnCanvas.height = nnSec.offsetHeight;
          
          window.addEventListener('resize', () => {
              cw = nnCanvas.width = nnSec.offsetWidth;
              ch = nnCanvas.height = nnSec.offsetHeight;
          });

          const nodes = document.querySelectorAll('.nn-node');
          const cols = [
             Array.from(document.querySelectorAll('.nn-col:nth-child(1) .nn-node')),
             Array.from(document.querySelectorAll('.nn-col:nth-child(2) .nn-node')),
             Array.from(document.querySelectorAll('.nn-col:nth-child(3) .nn-node'))
          ];
          
          let pulses = [];

          nodes.forEach(n => {
              n.addEventListener('mouseenter', () => {
                  const layerIdx = parseInt(n.getAttribute('data-layer'));
                  if(layerIdx < 2) {
                      // Fire pulses to next layer
                      cols[layerIdx + 1].forEach(targetNode => {
                          pulses.push({
                              source: n, target: targetNode, progress: 0,
                              speed: 0.02 + Math.random()*0.015, color: layerIdx === 0 ? '#10b981' : '#f43f5e'
                          });
                      });
                  }
              });
          });

          function getCenter(el) {
              const rect = el.getBoundingClientRect();
              const secRect = nnSec.getBoundingClientRect();
              return { x: rect.left - secRect.left + rect.width/2, y: rect.top - secRect.top + rect.height/2 };
          }

          function drawNN() {
              ctx.clearRect(0, 0, cw, ch);
              
              // Draw static connections
              ctx.lineWidth = 1;
              for(let i=0; i<cols.length-1; i++) {
                 cols[i].forEach(n1 => {
                     const p1 = getCenter(n1);
                     cols[i+1].forEach(n2 => {
                         const p2 = getCenter(n2);
                         ctx.beginPath();
                         ctx.moveTo(p1.x, p1.y);
                         // Bezier curve
                         const cx = (p1.x + p2.x)/2;
                         ctx.bezierCurveTo(cx, p1.y, cx, p2.y, p2.x, p2.y);
                         ctx.strokeStyle = 'rgba(168, 85, 247, 0.15)';
                         ctx.stroke();
                     });
                 });
              }

              // Draw Data Pulses
              for(let i=pulses.length-1; i>=0; i--) {
                  let p = pulses[i];
                  p.progress += p.speed;
                  const p1 = getCenter(p.source);
                  const p2 = getCenter(p.target);
                  
                  // Math interpolate bezier
                  const cx = (p1.x + p2.x)/2;
                  const t = p.progress;
                  const bx1 = p1.x + (cx - p1.x)*t;
                  const by1 = p1.y + (p1.y - p1.y)*t; // ctrl pt1 is cx, p1.y
                  const bx2 = cx + (p2.x - cx)*t;
                  const by2 = p1.y + (p2.y - p1.y)*t;
                  const bx3 = p2.x + (p2.x - p2.x)*t; // pt2
                  
                  // Quadratic/Cubic eval standard form
                  const invT = 1 - t;
                  const x = invT*invT*invT*p1.x + 3*invT*invT*t*cx + 3*invT*t*t*cx + t*t*t*p2.x;
                  const y = invT*invT*invT*p1.y + 3*invT*invT*t*p1.y + 3*invT*t*t*p2.y + t*t*t*p2.y;

                  ctx.beginPath();
                  ctx.arc(x, y, 4, 0, Math.PI*2);
                  ctx.fillStyle = p.color;
                  ctx.shadowColor = p.color;
                  ctx.shadowBlur = 10;
                  ctx.fill();
                  ctx.shadowBlur = 0;

                  // Leave trail
                  ctx.beginPath();
                  ctx.arc(x, y, 1.5, 0, Math.PI*2);
                  ctx.fillStyle = '#fff';
                  ctx.fill();

                  if(p.progress >= 1) pulses.splice(i, 1);
              }
              
              requestAnimationFrame(drawNN);
          }
          drawNN();
      }
      """
        if s_js_start != -1:
             s_content = s_content[:s_js_start] + s_js_new + s_content[s_js_end:]

        with open('d:/Websites/portfolio/skills.html', 'w', encoding='utf-8') as f:
            f.write(s_content)

        print("P4, P5, and Neural Network injected successfully.")
    except Exception as e:
        import traceback
        traceback.print_exc()

redesign_P4_P5_Neural()
