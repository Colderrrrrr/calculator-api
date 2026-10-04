FROM python:3.12-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 10001 appuser

WORKDIR /app

COPY requirements.txt .

# pip в рантайме не нужен, а Trivy находит уязвимости в нём самом
# и в библиотеках, которые он несёт с собой
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /usr/local/lib/python3.12/site-packages/pip* /usr/local/bin/pip*

COPY VERSION .
COPY app ./app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
