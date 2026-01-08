# Build Container
FROM python:3.13-slim AS builder

# It's easiest to have the virtual environment
# built local w/ the app. This way we can bring 
# over the app + venv together. 
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app
RUN pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock* ./
RUN poetry install --without dev --no-root
COPY app ./app

# Runtime Container. Grab the venv
# and app folders - and set the path 
# correctly. Without the PATH we will see
# errors with python not resolving our app 
# modules. 
FROM python:3.13-slim AS runtime
WORKDIR /app

ENV PATH="/app/.venv/bin:${PATH}"
COPY --from=builder /app/app ./app
COPY --from=builder /app/.venv /app/.venv

RUN adduser --disabled-password appuser
USER appuser

# Since the port is exposed via the app
# at runtime we will avoid exposing it
# as part of hte docker manifest. As such
# we've intentionally omitted an EXPOSE
# declaration.
CMD ["python", "-m", "app.main"]