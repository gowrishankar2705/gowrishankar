import os
import re
import glob

html_files = glob.glob('d:/Websites/portfolio/*.html')

# Colors
replacements = [
    (r'--bg-dark:\s*#[0-9a-fA-F]+', '--bg-dark: #05010a'),
    (r'--surface:\s*#[0-9a-fA-F]+', '--surface: #10031c'),
    (r'--card:\s*#[0-9a-fA-F]+', '--card: #19052b'),
    (r'--primary:\s*#[0-9a-fA-F]+', '--primary: #a855f7'),
    (r'--cyan:\s*#[0-9a-fA-F]+', '--cyan: #10b981'),
    (r'--gold:\s*#[0-9a-fA-F]+', '--gold: #f43f5e'),
    (r'--glow:\s*rgba\([^\)]+\)', '--glow: rgba(168, 85, 247, 0.4)'),
    (r'--border:\s*rgba\([^\)]+\)', '--border: rgba(255, 255, 255, 0.08)'),
    (r'rgba\(0,\s*102,\s*255,\s*0\.2\)', 'rgba(168, 85, 247, 0.2)'), # General blue borders
    (r'rgba\(0,\s*102,\s*255,\s*0\.1\)', 'rgba(168, 85, 247, 0.1)'), # General blue hovers
    (r'rgba\(0,\s*102,\s*255,\s*0\.4\)', 'rgba(168, 85, 247, 0.4)'),
    (r'rgba\(0,\s*102,\s*255,\s*0\.05\)', 'rgba(168, 85, 247, 0.05)'),
    (r'rgba\(0,\s*102,\s*255,\s*0\.15\)', 'rgba(168, 85, 247, 0.15)'),
    (r'rgba\(0,\s*102,\s*255,\s*0\.02\)', 'rgba(168, 85, 247, 0.02)'),
]

# Background Radial gradient
radial_old_1 = r'radial-gradient\(circle,\s*rgba\(0,\s*102,\s*255,\s*0\.05\)\s*0%,\s*transparent\s*60%\)'
radial_new_1 = 'radial-gradient(circle, rgba(168, 85, 247, 0.12) 0%, rgba(16, 185, 129, 0.04) 40%, transparent 70%)'

# Center glow
glow_old = r'radial-gradient\(circle,\s*rgba\(0,\s*102,\s*255,\s*0\.15\)\s*0%,\s*transparent\s*60%\)'
glow_new = 'radial-gradient(circle, rgba(168, 85, 247, 0.25) 0%, transparent 60%)'

# Neural circle
nc_old = r'radial-gradient\(circle at center,\s*#0a1628\s*0%,\s*#060d18\s*100%\)'
nc_new = 'radial-gradient(circle at center, #19052b 0%, #10031c 100%)'

# Green pulse (live clock dot)
pulse_old = r'#00ff66'
pulse_new = '#10b981'

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply color replacements
        for old, new in replacements:
            content = re.sub(old, new, content)
            
        # Apply specific gradient replacements
        content = re.sub(radial_old_1, radial_new_1, content)
        content = re.sub(glow_old, glow_new, content)
        content = re.sub(nc_old, nc_new, content)
        content = content.replace(pulse_old, pulse_new)
        
        # Cursor Active State Enhance
        cursor_active_old = r'\.cursor-ring\.active\s*\{\s*width:\s*50px;\s*height:\s*50px;\s*background:\s*rgba\([^)]+\);\s*\}'
        cursor_active_new = '.cursor-ring.active { width: 60px; height: 60px; background: rgba(168, 85, 247, 0.15); border-color: var(--cyan); box-shadow: 0 0 15px var(--primary); transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }'
        content = re.sub(cursor_active_old, cursor_active_new, content)

        # Pulse Ring Enhance
        pulse_ring_old = r'@keyframes pulseRing \{ 0% \{ transform: scale\(0\.8\); opacity: 1; \} 100% \{ transform: scale\(1\.5\); opacity: 0; \} \}'
        pulse_ring_new = '@keyframes pulseRing { 0% { transform: scale(0.8); opacity: 0.8; box-shadow: 0 0 0 0 rgba(168, 85, 247, 0.7); } 100% { transform: scale(1.6); opacity: 0; box-shadow: 0 0 20px 10px rgba(168, 85, 247, 0); } }'
        content = re.sub(pulse_ring_old, pulse_ring_new, content)
        
        # Reveal Animation Enhance
        reveal_old = r'\.reveal \{ opacity: 0; transform: translateY\(30px\); transition: all 0\.8s cubic-bezier\(0\.16,\s*1,\s*0\.3,\s*1\); \}'
        reveal_new = '.reveal { opacity: 0; transform: translateY(40px) scale(0.98); filter: blur(4px); transition: all 1s cubic-bezier(0.16, 1, 0.3, 1); }'
        content = re.sub(reveal_old, reveal_new, content)
        
        reveal_vis_old = r'\.reveal\.visible \{ opacity: 1; transform: translateY\(0\); \}'
        reveal_vis_new = '.reveal.visible { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }'
        content = re.sub(reveal_vis_old, reveal_vis_new, content)
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {html_file}")
    except Exception as e:
        print(f"Failed to update {html_file}: {e}")
