<<<<<<< HEAD
# Calculator API

REST API калькулятор на FastAPI.

=======
>>>>>>> c9f2134209eb07121d8d62f3903e305738fc4b16
## Запуск

```bash
docker build -t calculator-api .
docker run -p 8000:8000 calculator-api
```

Документация: http://localhost:8000/docs

## CI/CD

При каждом пуше в `main` GitHub Actions:

<<<<<<< HEAD
1. обновляет Python-пакеты до последних версий и записывает их в `requirements.txt`;
2. запускает тесты (если они упали, версия не выпускается);
3. увеличивает версию в файле `VERSION` и ставит тег: коммит `feat: ...` даёт 1.0.0 → 1.1.0, любой другой — 1.0.0 → 1.0.1;
4. собирает Docker-образ на свежем базовом образе и публикует его в `ghcr.io/colderrrrrr/calculator-api`.

Dependabot раз в неделю дополнительно проверяет обновления Python-пакетов и базового Docker-образа.
=======
1. запускает тесты;
2. увеличивает версию в файле `VERSION` и ставит тег;
3. собирает Docker-образ и публикует его в `ghcr.io/colderrrrrr/calculator-api`.

Dependabot раз в неделю проверяет обновления Python-пакетов и базового Docker-образа.
>>>>>>> c9f2134209eb07121d8d62f3903e305738fc4b16
