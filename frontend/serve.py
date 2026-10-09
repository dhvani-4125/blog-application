"""Tiny static server with single-page-app fallback. Usage: python serve.py [port]"""
import http.server, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, '.svg': 'image/svg+xml', '.js': 'text/javascript'}
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def send_head(self):
        path = self.translate_path(self.path.split('?')[0])
        if not os.path.exists(path) and '.' not in os.path.basename(path):
            self.path = '/index.html'
        return super().send_head()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5173
    print(f'THE WITHIN front end on http://localhost:{port}')
    http.server.ThreadingHTTPServer(('', port), Handler).serve_forever()
