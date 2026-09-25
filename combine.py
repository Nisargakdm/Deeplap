import os

def combine_files():
    base_dir = r"d:\Test\polaris-maritime-attribution-AIS\backend\app\static"
    html_path = os.path.join(base_dir, "index.html")
    css_path = os.path.join(base_dir, "css", "styles.css")
    js_path = os.path.join(base_dir, "js", "app.js")
    
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()
        
    with open(js_path, "r", encoding="utf-8") as f:
        js_content = f.read()
        
    # Replace the <link rel="stylesheet" href="/static/css/styles.css"> with inline CSS
    html_content = html_content.replace('<link rel="stylesheet" href="/static/css/styles.css">', f'<style>{css_content}</style>')
    
    # Replace the <script type="module" src="/static/js/app.js"></script> with inline JS
    html_content = html_content.replace('<script type="module" src="/static/js/app.js"></script>', f'<script type="module">{js_content}</script>')
    
    output_path = r"d:\Test\polaris-maritime-attribution-AIS\complete_design.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Successfully combined into {output_path}")

if __name__ == "__main__":
    combine_files()
