# Practice exam, Task 02: a small HTTP server for the Containerfile you write.
# It reads PORT from the environment and serves the files in /srv/site.
import functools
import http.server
import os

PORT = int(os.environ.get("PORT", "9000"))
SITE_DIR = "/srv/site"

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=SITE_DIR)
print(f"serving {SITE_DIR} on port {PORT}", flush=True)
http.server.ThreadingHTTPServer(("0.0.0.0", PORT), handler).serve_forever()
