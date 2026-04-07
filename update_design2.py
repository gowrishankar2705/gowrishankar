import os
import glob

html_files = glob.glob('d:/Websites/portfolio/*.html')

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Canvas Particles Update
        content = content.replace(
            "bgCtx.fillStyle = 'rgba(240,244,255,0.4)';",
            "bgCtx.fillStyle = 'rgba(168, 85, 247, 0.6)';"
        )
        content = content.replace(
            "bgCtx.strokeStyle = 'rgba(240,244,255,0.06)';",
            "bgCtx.strokeStyle = 'rgba(16, 185, 129, 0.15)';"
        )
        
        # Glitch Transition Expansion
        old_glitch_sweep = """@keyframes glitchSweep {
      0% {
        transform: scaleX(0);
        transform-origin: left;
      }

      50% {
        transform: scaleX(1);
        transform-origin: left;
      }

      51% {
        transform: scaleX(1);
        transform-origin: right;
      }

      100% {
        transform: scaleX(0);
        transform-origin: right;
      }
    }"""
        
        old_glitch_sweep_inline = "@keyframes glitchSweep { 0% { transform: scaleX(0); transform-origin: left; } 50% { transform: scaleX(1); transform-origin: left; } 51% { transform: scaleX(1); transform-origin: right; } 100% { transform: scaleX(0); transform-origin: right; } }"

        new_glitch_sweep = """@keyframes glitchSweep { 
      0% { transform: scaleX(0) skewX(-15deg); transform-origin: left; filter: blur(10px); } 
      40% { transform: scaleX(1.05) skewX(0deg); transform-origin: left; filter: blur(0px); } 
      50% { transform: scaleX(1) skewX(0deg); transform-origin: left; } 
      51% { transform: scaleX(1) skewX(0deg); transform-origin: right; } 
      100% { transform: scaleX(0) skewX(15deg); transform-origin: right; filter: blur(10px); } 
    }"""
        
        content = content.replace(old_glitch_sweep, new_glitch_sweep)
        content = content.replace(old_glitch_sweep_inline, new_glitch_sweep)
        
        # Soften canvas speed
        content = content.replace(
            "vx: (Math.random()-0.5)*0.5, vy: (Math.random()-0.5)*0.5",
            "vx: (Math.random()-0.5)*0.3, vy: (Math.random()-0.5)*0.3" 
        )

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {html_file}")
    except Exception as e:
        print(f"Failed to update {html_file}: {e}")
