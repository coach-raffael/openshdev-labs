import os, sys, time, random, string, logging
from flask import Flask, request, jsonify, redirect, abort
import psycopg

APP_NAME     = os.environ.get("APP_NAME", "shortly")
PORT         = int(os.environ.get("PORT", "8080"))
BASE_URL     = os.environ.get("BASE_URL", f"http://localhost:{PORT}")
DATABASE_URL = os.environ["DATABASE_URL"]            # no default: fail loudly if missing

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("shortly")

if os.environ.get("DEBUG") == "1":                   # Module 08: remote debugging
    import debugpy
    debugpy.listen(("0.0.0.0", 5678))
    log.info("debugpy listening on 0.0.0.0:5678")

def connect(retries=15, delay=2):
    for attempt in range(1, retries + 1):
        try:
            return psycopg.connect(DATABASE_URL, autocommit=True, connect_timeout=3)
        except psycopg.OperationalError as e:
            log.warning("database not ready (%s), attempt %d/%d", e, attempt, retries)
            time.sleep(delay)
    log.error("database unreachable, giving up")
    sys.exit(1)

def init_db():
    with connect() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS links (
            code TEXT PRIMARY KEY, url TEXT NOT NULL,
            hits INTEGER NOT NULL DEFAULT 0, created_at TIMESTAMPTZ DEFAULT now())""")

app = Flask(__name__)

def new_code(n=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))

@app.get("/health")
def health():
    try:
        with connect(retries=1) as conn:
            conn.execute("SELECT 1")
        return jsonify(status="ok", backend="postgresql", app=APP_NAME)
    except SystemExit:
        return jsonify(status="degraded", backend="postgresql", app=APP_NAME), 503

@app.post("/shorten")
def shorten():
    url = request.form.get("url") or (request.get_json(silent=True) or {}).get("url")
    if not url:
        abort(400, "url is required")
    code = new_code()
    with connect() as conn:
        conn.execute("INSERT INTO links (code, url) VALUES (%s, %s)", (code, url))
    log.info("shortened %s -> %s", url, code)
    return jsonify(code=code, short_url=f"{BASE_URL}/{code}")

@app.get("/<code>")
def follow(code):
    with connect() as conn:
        row = conn.execute("UPDATE links SET hits = hits + 1 WHERE code = %s RETURNING url", (code,)).fetchone()
    if not row:
        abort(404)
    return redirect(row[0], 302)

@app.get("/stats")
def stats():
    with connect() as conn:
        n, h = conn.execute("SELECT count(*), coalesce(sum(hits),0) FROM links").fetchone()
    return jsonify(links=n, hits=int(h), backend="postgresql")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=PORT)
