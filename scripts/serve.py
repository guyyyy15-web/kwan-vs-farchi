#!/usr/bin/env python3
"""שרת סטטי פשוט למשחק (ללא cache) — python3 scripts/serve.py [port]"""
import http.server, os, sys, functools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

os.chdir(ROOT)
handler = functools.partial(NoCache, directory=ROOT)
with http.server.ThreadingHTTPServer(('127.0.0.1', PORT), handler) as httpd:
    print(f'serving {ROOT} at http://localhost:{PORT}/', flush=True)
    httpd.serve_forever()
