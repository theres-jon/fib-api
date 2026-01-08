import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from app.fibonacci import fibonacci
from app.logging import logger

SERVER_PORT = os.getenv("SERVER_PORT", "8000")
FIB_MAX = os.getenv("MAX_FIB", "100000")

FIB_MAX_INT = int(FIB_MAX)

class GetFibs(BaseHTTPRequestHandler):

    def respond(self, status: int, body: str):
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    # Need something for the liveness probe
    def handle_health(self):
        return self.respond(200, "ok")

    # Future improvement - add caching on the Fib sequences
    def handle_fibonacci(self, params):
        if "n" not in params:
            return self.respond(422, "Missing required query parameter 'n'")

        try:
            n = int(params["n"][0])
        except (IndexError, ValueError):
            return self.respond(422, "'n' must be an integer")

        if n < 0 or n > FIB_MAX_INT:
            return self.respond(
                422,
                f"'n' must be between 0 and {FIB_MAX_INT}"
            )

        nums = fibonacci(n)
        result = ", ".join(map(str, nums))

        return self.respond(200, result)

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        logger.info(
            "Incoming request",
            path=parsed.path,
            query=parsed.query,
            client=self.client_address[0],
        )

        if parsed.path == "/health":
            return self.handle_health()

        if parsed.path == "/":
            return self.handle_fibonacci(params)

        return self.respond(404, "Not Found")

if __name__ == "__main__":
    from http.server import HTTPServer

    logger.info(f"Beginning server, listening on {SERVER_PORT}")
    httpd = HTTPServer(("", int(SERVER_PORT)), GetFibs)
    httpd.serve_forever()
