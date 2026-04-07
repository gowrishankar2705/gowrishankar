import os

def update_orbit_and_constellation():
    try:
        with open('d:/Websites/portfolio/skills.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. ORBIT VISUAL CSS UPGRADE
        if '.orbit-wrap { position: relative; width: 600px; height: 600px; display: flex; align-items: center; justify-content: center; transform-style: preserve-3d; transition: transform 0.1s linear; }' not in content:
            content = content.replace('.orbit-wrap { position: relative; width: 600px; height: 600px; display: flex; align-items: center; justify-content: center; }', 
                                      '.orbit-wrap { position: relative; width: 600px; height: 600px; display: flex; align-items: center; justify-content: center; transform-style: preserve-3d; transition: transform 0.1s linear; }')
        
            # Update the gradient of the orbit-center
            content = content.replace('.orbit-center { width: 200px; height: 200px; background: radial-gradient(circle, var(--card) 0%, var(--surface) 100%); border-radius: 50%; border: 2px solid var(--primary); display: flex; align-items: center; justify-content: center; font-family: var(--font-disp); font-size: 18px; letter-spacing: 0.1em; color: var(--white); box-shadow: 0 0 50px var(--glow); position: relative; z-index: 10; font-weight: 700; text-shadow: 0 0 10px rgba(255,255,255,0.5); }',
                                      '.orbit-center { width: 200px; height: 200px; background: rgba(16,3,28,0.8); border-radius: 50%; border: 2px solid var(--primary); display: flex; align-items: center; justify-content: center; font-family: var(--font-disp); font-size: 18px; letter-spacing: 0.1em; color: var(--white); box-shadow: 0 0 50px var(--glow); position: relative; z-index: 10; font-weight: 700; text-shadow: 0 0 10px rgba(255,255,255,0.5); overflow: hidden; backdrop-filter: blur(10px); }'
                                      '\n    .orbit-core-light { position: absolute; inset: -50%; background: conic-gradient(from var(--angle, 0deg), transparent 0deg, var(--primary) 90deg, transparent 180deg); opacity: 0.5; filter: blur(30px); pointer-events: none; }')

            # inject the .orbit-core-light div inside .orbit-center
            content = content.replace('<div class="orbit-center interactive">\n          GOWRISHANKAR\n        </div>', 
                                      '<div class="orbit-center interactive">\n          <div class="orbit-core-light"></div>\n          GOWRISHANKAR\n        </div>')

        # 2. CONSTELLATION HTML UPGRADE (Canvas)
        const_html_old = """<!-- Tech Constellation -->
    <section class="constellation" id="constellation">
      <!-- Generated via JS for exact absolute positioning scattered across -->
    </section>"""
        const_html_new = """<!-- Tech Vector Canvas -->
    <section class="constellation" id="constellation">
      <canvas id="const-canvas"></canvas>
      <div class="const-overlay">
         <h2>DATA STREAM</h2>
         <p>Intercepting tech stack telemetry...</p>
      </div>
    </section>"""
        if const_html_old in content:
            content = content.replace(const_html_old, const_html_new)
            
            # CSS for new constellation
            const_css_new = """/* TECH VECTOR CANVAS */
    .constellation { min-height: 100vh; position: relative; overflow: hidden; background: #010204; border-top: 1px solid var(--border); display: flex; align-items: center; justify-content: center; }
    #const-canvas { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }
    .const-overlay { position: relative; z-index: 2; text-align: center; pointer-events: none; opacity: 0.3; }
    .const-overlay h2 { font-family: var(--font-disp); font-size: clamp(40px, 8vw, 120px); -webkit-text-stroke: 1px var(--border); color: transparent; letter-spacing: 0.1em; margin-bottom: 20px; }
    .const-overlay p { font-family: var(--font-body); color: var(--cyan); letter-spacing: 0.2em; text-transform: uppercase; }"""
            
            # Find the old /* TECH CONSTELLATION */ css and replace
            css_start = content.find('/* TECH CONSTELLATION */')
            css_end = content.find('@media (max-width: 900px)', css_start)
            content = content[:css_start] + const_css_new + '\n\n    ' + content[css_end:]

        # 3. JAVASCRIPT UPGRADE
        # Orbit mouse tracking
        orbit_js = """
      // 3D Orbital Gyroscope
      const orbitSec = document.querySelector('.orbit-sec');
      const orbitWrap = document.querySelector('.orbit-wrap');
      const orbitLight = document.querySelector('.orbit-core-light');
      if(orbitSec && orbitWrap) {
          orbitSec.addEventListener('mousemove', e => {
              const rect = orbitSec.getBoundingClientRect();
              const x = e.clientX - rect.left;
              const y = e.clientY - rect.top;
              const cx = rect.width / 2;
              const cy = rect.height / 2;
              
              const rotX = -((y - cy) / cy) * 20; 
              const rotY = ((x - cx) / cx) * 20;
              
              orbitWrap.style.transform = `scale(1) rotateX(${rotX}deg) rotateY(${rotY}deg)`;
              
              if(orbitLight) {
                  const angle = Math.atan2(y - cy, x - cx) * 180 / Math.PI;
                  orbitLight.style.setProperty('--angle', `${angle}deg`);
              }
          });
          orbitSec.addEventListener('mouseleave', () => {
              orbitWrap.style.transform = `scale(1) rotateX(0deg) rotateY(0deg)`;
          });
      }
        """
        if '// 3D Orbital Gyroscope' not in content:
            # insert right after document.addEventListener('DOMContentLoaded', () => {
            idx = content.find("document.addEventListener('DOMContentLoaded', () => {") + len("document.addEventListener('DOMContentLoaded', () => {")
            content = content[:idx] + orbit_js + content[idx:]

        # Constellation Canvas Physics
        js_const_start = content.find('// Tech Constellation')
        if js_const_start != -1:
            # Find the end of this block (before </script>)
            js_const_end = content.find('});\n  </script>', js_const_start)
            
            new_physics_js = """// Tech Vector Gravity Canvas
      const constCanvas = document.getElementById('const-canvas');
      const constSecObj = document.getElementById('constellation');
      if(constCanvas && constSecObj) {
          const ctx = constCanvas.getContext('2d');
          let cw = constCanvas.width = constSecObj.offsetWidth;
          let ch = constCanvas.height = constSecObj.offsetHeight;
          
          window.addEventListener('resize', () => {
              cw = constCanvas.width = constSecObj.offsetWidth;
              ch = constCanvas.height = constSecObj.offsetHeight;
          });

          const techWords = ['Artificial Intelligence', 'Machine Learning', 'Data Science', 'Power BI', 'Web Dev', 'App Dev', 'UI/UX', 'PyTorch', 'TensorFlow', 'Docker', 'Git', 'OpenCV', 'YOLO', 'Streamlit', 'Node.js', 'Flask'];
          const nodes = [];
          
          for(let i=0; i<techWords.length; i++) {
              nodes.push({
                  text: techWords[i],
                  x: Math.random() * cw,
                  y: Math.random() * ch,
                  vx: (Math.random() - 0.5) * 1.5,
                  vy: (Math.random() - 0.5) * 1.5,
                  size: Math.random() * 10 + 14 // 14 to 24 font size
              });
          }

          let mx = -1000, my = -1000;
          constSecObj.addEventListener('mousemove', e => {
              const rect = constSecObj.getBoundingClientRect();
              mx = e.clientX - rect.left;
              my = e.clientY - rect.top;
          });
          constSecObj.addEventListener('mouseleave', () => { mx = -1000; my = -1000; });

          function drawPhysics() {
              ctx.clearRect(0, 0, cw, ch);
              
              ctx.textAlign = 'center';
              ctx.textBaseline = 'middle';
              
              for(let i=0; i<nodes.length; i++) {
                  let n = nodes[i];
                  n.x += n.vx;
                  n.y += n.vy;
                  
                  // Bounce
                  if(n.x < 0 || n.x > cw) n.vx *= -1;
                  if(n.y < 0 || n.y > ch) n.vy *= -1;

                  // Gravity / Repulsion
                  const dx = mx - n.x;
                  const dy = my - n.y;
                  const dist = Math.sqrt(dx*dx + dy*dy);
                  
                  if(dist < 200) {
                      n.x -= (dx / dist) * 2; // Repel
                      n.y -= (dy / dist) * 2;
                      
                      // Draw laser to mouse
                      ctx.beginPath();
                      ctx.moveTo(n.x, n.y);
                      ctx.lineTo(mx, my);
                      ctx.strokeStyle = `rgba(168, 85, 247, ${1 - dist/200})`;
                      ctx.lineWidth = 1;
                      ctx.stroke();
                  }

                  // Draw text
                  ctx.font = `700 ${n.size}px 'JetBrains Mono', monospace`;
                  
                  // Color highlight based on mouse proximity
                  if(dist < 200) {
                      ctx.fillStyle = '#10b981'; // Cyan when near mouse
                      ctx.shadowColor = '#10b981';
                      ctx.shadowBlur = 10;
                  } else {
                      ctx.fillStyle = 'rgba(200, 216, 232, 0.4)'; // Muted normally
                      ctx.shadowBlur = 0;
                  }
                  
                  ctx.fillText(n.text, n.x, n.y);
                  
                  // Draw connections to other nodes
                  for(let j=i+1; j<nodes.length; j++) {
                      let n2 = nodes[j];
                      let dx2 = n.x - n2.x;
                      let dy2 = n.y - n2.y;
                      let dist2 = Math.sqrt(dx2*dx2 + dy2*dy2);
                      if(dist2 < 150) {
                          ctx.beginPath();
                          ctx.moveTo(n.x, n.y);
                          ctx.lineTo(n2.x, n2.y);
                          ctx.strokeStyle = `rgba(16, 185, 129, ${0.2 * (1 - dist2/150)})`;
                          ctx.lineWidth = 0.5;
                          ctx.stroke();
                      }
                  }
              }
              requestAnimationFrame(drawPhysics);
          }
          drawPhysics();
      }
      """
            content = content[:js_const_start] + new_physics_js + content[js_const_end:]

        with open('d:/Websites/portfolio/skills.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Orbit and Constellation Physics injected successfully.")
        
    except Exception as e:
        import traceback
        traceback.print_exc()

update_orbit_and_constellation()
