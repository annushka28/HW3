# ДЗ №3 — Docker. Bash

Проект генерирует и анализирует CSV-данные 

## Просмотр отчёта через GitHub Codespaces

Открыть репозиторий в Codespaces (Code → Codespaces → Create codespace on main)
и в терминале выполнить:

```bash
chmod +x run.sh
./run.sh build_generator
./run.sh build_reporter
./run.sh run_generator
./run.sh run_reporter
./run.sh report_server
```

Последняя команда поднимает веб-сервер на порту 8080, и Codespaces пробрасывает его
автоматически. 
Во вкладке PORTS открыть ссылку для порта 8080 и добавить к ней `/report.html`:

```
https://<имя-codespace>-8080.app.github.dev/report.html
```
