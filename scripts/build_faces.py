#!/usr/bin/env python3
"""
מטמיע את תמונות הראש (assets/head_*.png) בתוך index.html כ-data URI,
כדי שהמשחק יהיה קובץ אחד עצמאי שרץ מכל מקום (גם file://).

הרצה:  python3 scripts/build_faces.py
"""
import base64, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, 'index.html')
FACES = {'farchi': 'assets/head_farchi.png', 'kwan': 'assets/head_kwan.png'}

def main():
    entries = []
    for key, rel in FACES.items():
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            sys.exit(f'חסר קובץ: {rel}')
        b64 = base64.b64encode(open(path, 'rb').read()).decode('ascii')
        entries.append(f'{key}: "data:image/png;base64,{b64}"')
        print(f'{rel}: {len(b64)/1024:.0f} KB base64')

    html = open(HTML, encoding='utf-8').read()
    block = '/*FACES_START*/\n' + ',\n'.join(entries) + '\n/*FACES_END*/'
    new, n = re.subn(r'/\*FACES_START\*/.*?/\*FACES_END\*/', lambda m: block, html,
                     count=1, flags=re.S)
    if not n:
        sys.exit('לא נמצאו הסימנים FACES_START/FACES_END ב-index.html')
    open(HTML, 'w', encoding='utf-8').write(new)
    print(f'index.html עודכן ({len(new)/1024:.0f} KB)')

if __name__ == '__main__':
    main()
