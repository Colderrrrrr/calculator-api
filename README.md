
## Запуск

```bash
docker build -t calculator-api .
docker run -p 8000:8000 calculator-api
```

Документация: http://localhost:8000/docs

## API

`POST /calculate` с телом `{"a": 2, "b": 3, "operation": "+"}` возвращает
`{"result": 5.0}`. Операции: `+`, `-`, `*`, `/`, `**`.

Код 400 — операция невыполнима (деление на ноль, переполнение, нецелое
число в результате), 422 — некорректный запрос.

`GET /` возвращает название и версию, `GET /health` — состояние сервиса.

## CI/CD

При каждом пуше в `main` GitHub Actions выполняет два job.

`security`:

1. Semgrep — наборы правил `p/python`, `p/security-audit`, `p/secrets`,
   `p/dockerfile`, `p/github-actions`;
2. Trivy config — мисконфигурации Dockerfile;
3. Gitleaks — поиск секретов по всей истории коммитов.

`release` (запускается только если `security` прошёл):

1. обновляет Python-пакеты до последних версий и записывает их в
   `requirements.txt`;
2. запускает тесты;
3. увеличивает версию в файле `VERSION` и ставит тег: коммит `feat: ...`
   даёт 1.0.0 → 1.1.0, любой другой — 1.0.0 → 1.0.1;
4. собирает образ, сканирует его через Trivy и публикует в
   `ghcr.io/colderrrrrr/calculator-api`.

Отчёты сканеров доступны как artifacts запуска. Dependabot раз в неделю
проверяет обновления Python-пакетов, базового Docker-образа и actions.

## Безопасность

Разбор отчётов сканеров, исправления и предложения —
[`docs/security-analysis.md`](docs/security-analysis.md).
