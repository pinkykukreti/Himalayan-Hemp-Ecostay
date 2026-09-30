from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

if __name__ == '__main__':
    root = Path(__file__).resolve().parent / 'dist'
    server = ThreadingHTTPServer(('127.0.0.1', 8000), partial(SimpleHTTPRequestHandler, directory=str(root)))
    print('Open http://127.0.0.1:8000 — press Ctrl+C to stop.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
