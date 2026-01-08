.PHONY: install format test run build docker-build docker-run docker-push

IMAGE_NAME ?= fib-api
PORT ?= 8000

install:
	poetry install

format:
	poetry run black .

test:
	poetry run pytest

run:
	poetry run python -m app.main

build:
	poetry build

# -----------------------------
# Docker targets
# -----------------------------

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-push:
	docker tag $(IMAGE_NAME) jonryan/fib-api:latest
	docker push jonryan/fib-api:latest

docker-run:
	docker run --rm -p $(PORT):$(PORT) $(IMAGE_NAME)
