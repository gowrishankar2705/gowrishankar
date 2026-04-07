import os

def create_ring(name, pct, var_color):
    return f"""
          <div class="radial-node interactive" data-pct="{pct}">
              <div class="reactor-core" style="background: radial-gradient(circle, {var_color} 0%, transparent 70%);"></div>
              <svg viewBox="0 0 100 100" class="ring-svg">
                  <circle class="ring-bg" cx="50" cy="50" r="40"></circle>
                  <circle class="ring-fg" cx="50" cy="50" r="40" style="stroke: {var_color};"></circle>
                  <circle class="ring-tracker" cx="50" cy="50" r="46" style="stroke: {var_color};"></circle>
              </svg>
              <div class="ring-lbl">
                 <div class="rpct">0%</div>
                 <div class="rname">{name}</div>
              </div>
          </div>"""

def add_extra_skills():
    try:
        with open('d:/Websites/portfolio/skills.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. ADD CORE SKILLS
        core_idx = content.find('</div>\n         </div>\n         <div class="hud-panel" id="cat-eng">')
        if core_idx != -1:
            core_add = create_ring('NLP / Gen AI', 90, 'var(--primary)') + create_ring('Deep Learning', 95, 'var(--primary)')
            content = content[:core_idx] + core_add + content[core_idx:]

        # 2. ADD ENGINEERING SKILLS
        eng_idx = content.find('</div>\n         </div>\n         <div class="hud-panel" id="cat-tools">')
        if eng_idx != -1:
            eng_add = create_ring('React / Next.js', 85, 'var(--cyan)') + create_ring('System Design', 80, 'var(--cyan)')
            content = content[:eng_idx] + eng_add + content[eng_idx:]

        # 3. ADD TOOLS SKILLS
        tools_idx = content.find('</div>\n         </div>\n      </div>\n\n    </section>')
        if tools_idx != -1:
            tools_add = create_ring('Hugging Face', 90, 'var(--gold)') + create_ring('Kubernetes', 80, 'var(--gold)')
            content = content[:tools_idx] + tools_add + content[tools_idx:]

        # 4. ADD TO TECH WORDS
        target_js = "const techWords = ['Artificial Intelligence', 'Machine Learning', 'Data Science', 'Power BI', 'Web Dev', 'App Dev', 'UI/UX', 'PyTorch', 'TensorFlow', 'Docker', 'Git', 'OpenCV', 'YOLO', 'Streamlit', 'Node.js', 'Flask'];"
        new_js = "const techWords = ['Artificial Intelligence', 'Machine Learning', 'Data Science', 'Power BI', 'Web Dev', 'App Dev', 'UI/UX', 'PyTorch', 'TensorFlow', 'Docker', 'Git', 'OpenCV', 'YOLO', 'Streamlit', 'Node.js', 'Flask', 'Next.js', 'React', 'Kubernetes', 'LLMs', 'NLP', 'System Design', 'Hugging Face'];"
        
        content = content.replace(target_js, new_js)

        with open('d:/Websites/portfolio/skills.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Extra skills added successfully.")
    except Exception as e:
        import traceback
        traceback.print_exc()

add_extra_skills()
