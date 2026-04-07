import os
import glob
import re

html_files = glob.glob('d:/Websites/portfolio/*.html')

quantum_fonts = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">'

quantum_root = """    :root {
      --bg-dark: #0b0f19;
      --surface: rgba(255, 255, 255, 0.02);
      --card: rgba(255, 255, 255, 0.03);
      --border: rgba(255, 255, 255, 0.08);
      --primary: #00f0ff;
      --glow: rgba(0, 240, 255, 0.4);
      --cyan: #ff00e5;
      --gold: #ffffff;
      --white: #ffffff;
      --muted: #8a9bb5;
      --text: #e2e8f0;
      --font-disp: 'Space Grotesk', sans-serif;
      --font-head: 'Inter', sans-serif;
      --font-body: 'JetBrains Mono', monospace;
    }"""

old_root_regex = r":root\s*\{[^}]+\}"

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Fonts
        content = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Outfit[^>]+>', quantum_fonts, content)
        content = content.replace("'Quicksand'", "'Space Grotesk'")
        content = content.replace("'Outfit'", "'Inter'")

        # Update Root
        content = re.sub(old_root_regex, quantum_root, content)

        # Revert Background Gradient Water Effect
        content = content.replace(
            "radial-gradient(circle at 10% 20%, rgba(14, 165, 233, 0.1)",
            "radial-gradient(circle at 10% 10%, rgba(0, 240, 255, 0.08)"
        ).replace(
            "radial-gradient(circle at 80% 80%, rgba(20, 184, 166, 0.1)",
            "radial-gradient(circle at 90% 90%, rgba(255, 0, 229, 0.08)"
        )

        content = content.replace(
            "radial-gradient(circle, rgba(14, 165, 233, 0.07)",
            "radial-gradient(circle, rgba(0, 240, 255, 0.05)"
        )
        content = content.replace(
            "radial-gradient(circle, rgba(14, 165, 233, 0.15)",
            "radial-gradient(circle, rgba(0, 240, 255, 0.15)"
        )

        # Revert Canvas particles
        content = content.replace(
            "vx: (Math.random()-0.5)*0.2, vy: (Math.random()*0.3)+0.1",
            "vx: (Math.random()-0.5)*0.5, vy: (Math.random()-0.5)*0.5"
        )
        content = content.replace(
            "p.y -= p.vy; p.x += Math.sin(p.y * 0.01) * 0.5;",
            "p.x += p.vx; p.y += p.vy;"
        )
        content = content.replace(
            "if(p.y < -10) { p.y = bgH + 10; p.x = Math.random() * bgW; }",
            "if(p.x<0||p.x>bgW) p.vx*=-1; if(p.y<0||p.y>bgH) p.vy*=-1;"
        )
        content = content.replace("'rgba(0, 0, 0, 0)'", "'rgba(255, 0, 229, 0.08)'") # Bring back connections globally

        # Revert Color token replacements across all inline JS and CSS
        content = content.replace("rgba(14, 165, 233,", "rgba(0, 240, 255,")
        content = content.replace("rgba(20, 184, 166,", "rgba(255, 0, 229,")
        content = content.replace("#14b8a6", "#ff00e5")
        
        # Revert Rounding elements for fluid/organic feel
        content = content.replace("border-radius: 16px", "border-radius: 4px")
        content = content.replace("border-radius: 30px", "border-radius: 2px")
        content = content.replace("border-radius: 24px", "border-radius: 8px")

        # Slide in animations - back to snappy
        content = content.replace("cubic-bezier(0.2, 0.8, 0.2, 1)", "cubic-bezier(0.16, 1, 0.3, 1)")

        # In index.html specifically:
        if "index.html" in fpath:
            content = content.replace(
                "const sysMsg = [\"> SYSTEM ONLINE\", \"> FLUID DYNAMICS: ACTIVE\", \"> BIOLUMINESCENCE: 100%\", \"> DEPTH: OPTIMAL\"];",
                "const sysMsg = [\"> SYSTEM ONLINE\", \"> QUANTUM CORES: ACTIVE\", \"> HOLOGRAPHICS: 100%\", \"> CAFFEINE: OPTIMAL\"];"
            )

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Reverted {fpath}")
    except Exception as e:
        print(f"Error on {fpath}: {e}")
