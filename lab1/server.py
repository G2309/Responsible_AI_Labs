import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BLOCKED = [
    "hate", "kill", "violence", "stupid", "idiot", "spam", "scam",
    "abuse", "attack", "racist", "odio", "matar", "violencia", "estupido",
]


def classify(text):
    lowered = text.lower()
    hits = [w for w in BLOCKED if w in lowered]
    if hits:
        confidence = round(min(0.99, 0.7 + 0.07 * len(hits)), 2)
        return {
            "verdict": "blocked",
            "confidence": confidence,
            "reason": "prohibited terms: " + ", ".join(hits),
        }
    return {
        "verdict": "allowed",
        "confidence": 0.95,
        "reason": "no prohibited content detected",
    }


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        client_ip = self.client_address[0]
        if self.path != "/moderate":
            self._send(404, {"error": "not found"})
            print(f'[POST {self.path}] {client_ip} -> 404')
            return
        try:
            length = int(self.headers.get("Content-Length", 0) or 0)
            raw = self.rfile.read(length) if length > 0 else b""
            data = json.loads(raw.decode("utf-8"))
            text = data.get("text")
            if not isinstance(text, str) or text.strip() == "":
                self._send(400, {"error": "text is required"})
                print(f'[POST /moderate] {client_ip} -> 400 {{"error":"text is required"}}')
                return
            result = classify(text)
            self._send(200, result)
            print(f"[POST /moderate] {client_ip} -> 200 {json.dumps(result)}")
        except (ValueError, UnicodeDecodeError):
            self._send(400, {"error": "text is required"})
            print(f'[POST /moderate] {client_ip} -> 400 {{"error":"text is required"}}')
        except Exception as e:
            self._send(500, {"error": str(e)})
            print(f'[POST /moderate] {client_ip} -> 500 {{"error":"{e}"}}')

    def log_message(self, *args):
        return


def main():
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"servidor escuchando en {host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()


main()
