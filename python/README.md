# Fibonacci Web Service

This project is a simple HTTP service that generates Fibonacci numbers based on user input.  
It is structured as a small, production-ready service with clear separation of concerns, structured logging, automated formatting, and basic test coverage.

## Requirements

- Python 3.10+
- Poetry

---
## Getting Started

```
app/        Application code (HTTP server, business logic, logging)
tests/      Unit tests
```


For local development

From the `python/` directory: 
- `make install` (or) `make docker-build`

This creates a virtual environment and installs all runtime and development dependencies.

From the `python/` directory:
- `make run` (or) `make docker-run`

The server will start on port 8000 by default.

### Environment Variables

SERVER_PORT  Port to bind the server (default: 8000)  
LOG_LEVEL    Log verbosity (default: INFO)

These can be added simply with putting them inline:
- `LOG_LEVEL=DEBUG SERVER_PORT=8080 make run`

Additionally we cap the max fibs that can be generated with
`MAX_FIBS`.

In an ideal world these would be set based on CPU/Memory of the host. 

---
### Fibonacci Endpoint

Request:

GET /?n=10

Response:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Invalid input returns `422 Unprocessable Entity`.

---

## Development

Common development tasks are automated via a Makefile:

make format    Format code with Black  
make test      Run unit tests  
make run       Start the server  
make build     Build the package

---
## Testing

From the Python directory

```
make install
make test
```

## Deploying
If installing with Helm and Minikube - please use the following
```
# Perform the docker build with the right Image Tag
docker build -f python/Dockerfile ./python -t fib-api:latest

minikube image load fib-api:latest

helm install fib-api ./chart
```

The primary consideration here is where the image is stored. Right now the chart serves it from a public Docker Hub registry. This is not recommended for production.