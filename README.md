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

1. обновляет Python-пакеты до последних версий и записывает их в `requirements.txt`;
2. запускает тесты (если они упали, версия не выпускается);
3. увеличивает версию в файле `VERSION` и ставит тег: коммит `feat: ...` даёт 1.0.0 → 1.1.0, любой другой — 1.0.0 → 1.0.1;
4. собирает Docker-образ на свежем базовом образе и публикует его в `ghcr.io/colderrrrrr/calculator-api`.

Dependabot раз в неделю дополнительно проверяет обновления Python-пакетов и базового Docker-образа.
