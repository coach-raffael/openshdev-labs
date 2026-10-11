import os, sys, random, string, logging
from flask import Flask, request, jsonify, redirect, abort

APP_NAME = os.environ.get("APP_NAME", "shortly")
PORT     = int(os.environ.get("PORT", "8080"))
BASE_URL = os.environ.get("BASE_URL", f"http://localhost:{PORT}")

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
app = Flask(__name__)
links, hits = {}, {}                      # in-memory "database", on purpose

def new_code(n=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))

@app.get("/health")
def health():
    return jsonify(status="ok", backend="memory", app=APP_NAME)

@app.post("/shorten")
def shorten():
    url = request.form.get("url") or (request.get_json(silent=True) or {}).get("url")
    if not url:
        abort(400, "url is required")
    code = new_code()
    links[code], hits[code] = url, 0
    app.logger.info("shortened %s -> %s", url, code)
    return jsonify(code=code, short_url=f"{BASE_URL}/{code}")

@app.get("/<code>")
def follow(code):
    url = links.get(code)
    if not url:
        abort(404)
    hits[code] += 1
    return redirect(url, 302)

@app.get("/stats")
def stats():
    return jsonify(links=len(links), hits=sum(hits.values()), backend="memory")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
