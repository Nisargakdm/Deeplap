import re
import json

def check():
    with open('backend/app/static/index.html', encoding='utf-8') as f:
        html = f.read()
    with open('backend/app/static/js/app.js', encoding='utf-8') as f:
        js = f.read()

    ids = set(re.findall(r'id=\"([^\"]+)\"', html))
    js_ids = set(re.findall(r'getElementById\([\'\"]([^\'\"]+)[\'\"]\)', js))

    missing = js_ids - ids
    print('Missing IDs in HTML:', missing)

if __name__ == "__main__":
    check()
