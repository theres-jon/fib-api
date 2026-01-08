import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from app.fibonacci import fibonacci
from app.logging import logger

SERVER_PORT = os.getenv("SERVER_PORT", 8000)


class GetFibs(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)

        logger.info(
            "Received request for fibs with parameters", extra={"params": params}
        )

        if "n" not in params:
            self.send_response(422)
            return

        try:
            key = int(params["n"][0])
        except (IndexError, ValueError) as exc:
            logger.error(
                "Invalid input while generating Fibonacci numbers",
                exc_info=exc,
                extra={"error_type": type(exc).__name__},
            )
            self.send_response(422)

        nums = fibonacci(key)

        # convert nums from int to string list
        str_nums = [str(n) for n in nums]
        final_nums = ", ".join(str_nums)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(final_nums, "UTF-8"))
        return


if __name__ == "__main__":
    from http.server import HTTPServer

    logger.info(f"Beginning server, listening on {SERVER_PORT}")
    httpd = HTTPServer(("", SERVER_PORT), GetFibs)
    httpd.serve_forever()
