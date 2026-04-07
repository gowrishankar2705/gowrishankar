import os
import glob
import re

html_files = glob.glob('d:/Websites/portfolio/*.html')

new_fonts_link = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700&family=Quicksand:wght@500;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">'

new_root = """    :root {
      --bg-dark: #020617;
      --surface: rgba(14, 165, 233, 0.03);
      --card: rgba(14, 165, 233, 0.05);
      --border: rgba(14, 165, 233, 0.15);
      --primary: #0ea5e9;
      --glow: rgba(14, 165, 233, 0.5);
      --cyan: #14b8a6;
      --gold: #a78bfa;
      --white: #e2e8f0;
      --muted: #64748b;
      --text: #cbd5e1;
      --font-disp: 'Quicksand', sans-serif;
      --font-head: 'Outfit', sans-serif;
      --font-body: 'JetBrains Mono', monospace;
    }"""

old_root_regex = r":root\s*\{[^}]+\}"

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Fonts
        content = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Inter[^>]+>', new_fonts_link, content)
        content = content.replace("'Space Grotesk'", "'Quicksand'")
        content = content.replace("'Inter'", "'Outfit'")

        # Update Root
        content = re.sub(old_root_regex, new_root, content)

        # Background Gradient Water Effect
        content = content.replace(
            "radial-gradient(circle at 10% 10%, rgba(0, 240, 255, 0.08)",
            "radial-gradient(circle at 10% 20%, rgba(14, 165, 233, 0.1)"
        ).replace(
            "radial-gradient(circle at 90% 90%, rgba(255, 0, 229, 0.08)",
            "radial-gradient(circle at 80% 80%, rgba(20, 184, 166, 0.1)"
        )

        content = content.replace(
            "radial-gradient(circle, rgba(0, 240, 255, 0.05)",
            "radial-gradient(circle, rgba(14, 165, 233, 0.07)"
        )
        content = content.replace(
            "radial-gradient(circle, rgba(0, 240, 255, 0.15)",
            "radial-gradient(circle, rgba(14, 165, 233, 0.15)"
        )

        # Canvas particles -> Bioluminescent Plankton
        content = content.replace(
            "vx: (Math.random()-0.5)*0.3, vy: (Math.random()-0.5)*0.3",
            "vx: (Math.random()-0.5)*0.2, vy: (Math.random()*0.3)+0.1"
        )
        content = content.replace(
            "vx: (Math.random() - 0.5) * 0.5, vy: (Math.random() - 0.5) * 0.5",
            "vx: (Math.random()-0.5)*0.2, vy: (Math.random()*0.3)+0.1"
        )
        content = content.replace(
            "p.x += p.vx; p.y += p.vy;",
            "p.y -= p.vy; p.x += Math.sin(p.y * 0.01) * 0.5;"
        )
        content = content.replace(
            "if(p.x<0||p.x>bgW) p.vx*=-1; if(p.y<0||p.y>bgH) p.vy*=-1;",
            "if(p.y < -10) { p.y = bgH + 10; p.x = Math.random() * bgW; }"
        )
        content = content.replace(
            "if (p.x < 0 || p.x > bgW) p.vx *= -1; if (p.y < 0 || p.y > bgH) p.vy *= -1;",
            "if(p.y < -10) { p.y = bgH + 10; p.x = Math.random() * bgW; }"
        )
        # Hide the canvas line connections to make it look like free-floating plankton/bubbles
        content = content.replace("'rgba(255, 0, 229, 0.08)'", "'rgba(0, 0, 0, 0)'")

        # Color token replacements across all inline JS and CSS
        content = content.replace("rgba(0, 240, 255,", "rgba(14, 165, 233,")
        content = content.replace("rgba(255, 0, 229,", "rgba(20, 184, 166,")
        content = content.replace("#ff00e5", "#14b8a6")
        
        # Rounding elements for fluid/organic feel
        content = content.replace("border-radius: 4px", "border-radius: 16px")
        content = content.replace("border-radius: 2px", "border-radius: 30px")
        content = content.replace("border-radius: 8px", "border-radius: 24px")

        # Slide in animations - slower and more organic
        content = content.replace("cubic-bezier(0.16, 1, 0.3, 1)", "cubic-bezier(0.2, 0.8, 0.2, 1)")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fpath}")
    except Exception as e:
        print(f"Error on {fpath}: {e}")
