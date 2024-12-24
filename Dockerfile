FROM python:3.12

WORKDIR /MLECH.Backend

COPY pyproject.toml uv.lock ./

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY . .

ENV PYTHONPATH=/app
ENV PORT=8000

COPY ./setEnv/.env /app/app/config/.env

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
