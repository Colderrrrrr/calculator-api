# Calculator API

REST API калькулятор на FastAPI.

## Запуск

```bash
docker build -t calculator-api .
docker run -p 8000:8000 calculator-api
```

Документация: http://localhost:8000/docs

## CI/CD

При каждом пуше в `main` GitHub Actions:

1. запускает тесты;
2. увеличивает версию в файле `VERSION` и ставит тег;
3. собирает Docker-образ и публикует его в `ghcr.io/colderrrrrr/calculator-api`.

Dependabot раз в неделю проверяет обновления Python-пакетов и базового Docker-образа.
