FROM python:3.11.3-slim-bullseye

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    git \
    cmake

RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH $PATH:/root/.local/bin/

# packages install
WORKDIR /app/src

COPY ./app/pyproject.toml /app/src/pyproject.toml
RUN poetry install

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
