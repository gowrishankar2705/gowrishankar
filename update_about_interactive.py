import os

try:
    with open('d:/Websites/portfolio/about.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. TEXT LEGIBILITY AND CSS UPGRADES
    # Update about-p
    content = content.replace(
        '.about-p { font-family: var(--font-head); font-size: 18px; color: var(--muted); line-height: 1.9; margin-bottom: 40px; max-width: 600px; }',
        '.about-p { font-family: var(--font-head); font-size: 19px; color: var(--text); font-weight: 500; line-height: 1.9; margin-bottom: 40px; max-width: 600px; text-shadow: 0 0 10px rgba(255,255,255,0.1); }'
    )
    
    # Update about-h1-outline
    content = content.replace(
        '.about-h1-outline { font-family: var(--font-disp); font-size: clamp(32px, 5vw, 58px); line-height: 1.1; margin-bottom: 30px; color: transparent; -webkit-text-stroke: 1.5px var(--cyan); }',
        '.about-h1-outline { font-family: var(--font-disp); font-size: clamp(32px, 5vw, 58px); line-height: 1.1; margin-bottom: 30px; color: transparent; -webkit-text-stroke: 1.5px var(--cyan); text-shadow: 0 0 15px rgba(16, 185, 129, 0.4); }'
    )
    
    # Update portrait framework and center-gs
    content = content.replace(
        '.portrait-frame { width: 100%; max-width: 400px; aspect-ratio: 4/5; background: var(--card); border-radius: 12px; position: relative; display: flex; align-items: center; justify-content: center; border: 1px solid var(--border); overflow: hidden; }',
        '.portrait-frame { width: 100%; max-width: 400px; aspect-ratio: 4/5; background: var(--card); border-radius: 12px; position: relative; display: flex; align-items: center; justify-content: center; border: 1px solid var(--border); overflow: hidden; transform-style: preserve-3d; transition: transform 0.1s linear, box-shadow 0.1s linear; }\n    .frame-glare { position: absolute; inset: 0; background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.15), transparent 60%); opacity: 0; pointer-events: none; mix-blend-mode: overlay; z-index: 10; transition: opacity 0.3s; }\n    .hero-right:hover .frame-glare { opacity: 1; }'
    )
    content = content.replace(
        '.center-gs { font-family: var(--font-disp); font-size: 120px; color: transparent; -webkit-text-stroke: 1px rgba(168, 85, 247, 0.4); z-index: 2; position: relative; }',
        '.center-gs { font-family: var(--font-disp); font-size: 120px; color: rgba(168, 85, 247, 0.05); -webkit-text-stroke: 2px var(--primary); text-shadow: 0 0 25px var(--glow); z-index: 2; position: relative; transform: translateZ(30px); }'
    )
    
    # Update badge-ai
    content = content.replace(
        '.badge-ai { position: absolute; bottom: -15px; right: -15px; background: var(--primary); color: #fff; font-family: var(--font-disp); font-size: 12px; padding: 10px 20px; border-radius: 4px; display: flex; align-items: center; gap: 8px; box-shadow: 0 10px 30px rgba(168, 85, 247, 0.4); z-index: 3; pointer-events: none; }',
        '.badge-ai { position: absolute; bottom: -15px; right: -15px; background: var(--primary); color: #fff; font-family: var(--font-disp); font-size: 12px; padding: 10px 20px; border-radius: 4px; display: flex; align-items: center; gap: 8px; box-shadow: 0 10px 30px rgba(168, 85, 247, 0.4); z-index: 3; pointer-events: none; transform: translateZ(50px); }'
    )

    # Add Story Card CSS
    content = content.replace(
        '.story-card:hover { transform: translateY(-10px); background: #0c1c33; border-color: rgba(0,102,255,0.3); }',
        '.story-card:hover { transform: translateY(-10px); background: #0c1c33; border-color: rgba(0,102,255,0.3); box-shadow: 0 10px 40px rgba(0,0,0,0.5); }\n    .story-card::before { content: ""; position: absolute; top: var(--y, 50%); left: var(--x, 50%); width: 300px; height: 300px; background: radial-gradient(circle closest-side, rgba(168,85,247,0.15), transparent); transform: translate(-50%, -50%); pointer-events: none; z-index: 0; opacity: 0; transition: opacity 0.3s; }\n    .story-card:hover::before { opacity: 1; }'
    )
    
    # Add Val-Icon Magic CSS
    content = content.replace(
        '.val-icon { font-size: 80px; color: transparent; -webkit-text-stroke: 1px var(--cyan); margin-bottom: 20px; filter: drop-shadow(0 0 20px rgba(0,212,255,0.2)); transition: 0.3s; }',
        '.val-icon { font-size: 80px; color: transparent; -webkit-text-stroke: 1px var(--cyan); margin-bottom: 20px; filter: drop-shadow(0 0 20px rgba(0,212,255,0.2)); transition: transform 0.15s cubic-bezier(0.2,0.8,0.2,1); pointer-events: none; }'
    )


    # 2. HTML STRUCTURE FIXES
    # Add frame-glare HTML inside portrait-frame
    if '<div class="frame-glare"></div>' not in content:
        content = content.replace(
            '<div class="portrait-frame">',
            '<div class="portrait-frame">\n          <div class="frame-glare"></div>'
        )

    # 3. INTERACTIVE JS INJECTION
    js_code = """
      // INTERACTIVITY: ABOUT PAGE 
      const heroRight = document.querySelector('.hero-right');
      const portrait = document.querySelector('.portrait-frame');
      const glare = document.querySelector('.frame-glare');
      if(heroRight && portrait) {
        heroRight.addEventListener('mousemove', e => {
          const rect = heroRight.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          const rotX = -((y / rect.height) - 0.5) * 30; // Max 15deg
          const rotY = ((x / rect.width) - 0.5) * 30;
          portrait.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg) scale(1.02)`;
          portrait.style.boxShadow = `${-rotY}px ${rotX}px 40px rgba(168, 85, 247, 0.2)`;
          if(glare) glare.style.transform = `translate(${x - rect.width/2}px, ${y - rect.height/2}px)`;
        });
        heroRight.addEventListener('mouseleave', () => {
          portrait.style.transform = `rotateX(0deg) rotateY(0deg) scale(1)`;
          portrait.style.boxShadow = `0 0 0 rgba(0,0,0,0)`;
        });
      }

      const storyCards = document.querySelectorAll('.story-card');
      storyCards.forEach(card => {
        card.addEventListener('mousemove', e => {
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          card.style.setProperty('--x', `${x}px`);
          card.style.setProperty('--y', `${y}px`);
        });
      });

      const valPanels = document.querySelectorAll('.val-panel');
      valPanels.forEach(panel => {
        const icon = panel.querySelector('.val-icon');
        const vis = panel.querySelector('.val-vis');
        if(vis && icon) {
          vis.addEventListener('mousemove', e => {
            const rect = vis.getBoundingClientRect();
            const x = (e.clientX - rect.left) - rect.width/2;
            const y = (e.clientY - rect.top) - rect.height/2;
            icon.style.transform = `translate(${x*0.4}px, ${y*0.4}px) scale(1.1)`;
          });
          vis.addEventListener('mouseleave', () => {
            icon.style.transform = `translate(0px, 0px) scale(1)`;
          });
        }
      });
    """
    
    if '// INTERACTIVITY: ABOUT PAGE' not in content:
        content = content.replace('// Background Canvas', js_code + '\n      // Background Canvas')

    with open('d:/Websites/portfolio/about.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("about.html successfully updated with high-end text legibility and interactive UI logic.")
except Exception as e:
    import traceback
    traceback.print_exc()
