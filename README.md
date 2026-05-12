# Сервис проверки статуса кнопки

Простой веб-сервис на Python для проверки статуса кнопки в реальном времени.

## Описание

Сервис предоставляет возможность управления статусом (ON/OFF) через HTTP-запросы. Все подключенные клиенты автоматически получают обновления статуса через WebSocket.

## Демо-версия

Демо-версия сервиса доступна здесь: https://button.globloc.ru

## Эндпоинты

| URL | Описание |
|-----|----------|
| `/` | Главная страница с визуальным отображением статуса|
| `/status` | Текстовое представление текущего статуса |
| `/knopka_on` | Поменять статус на "ON" (включено)  |
| `/knopka_off` | Поменять статус на "OFF" (выключено) |

## Установка и запуск


### Способ 1: Локальный запуск (без Docker)

```bash
git clone https://github.com/thecookiel0rd/TheKnopka.git
cd TheKnopka

# Создание виртуального окружения (опционально)
# python -m venv venv
# source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Установка зависимостей
pip install -r requirements.txt

# Запуск сервера
python app.py
```

Сервер запустится на `http://localhost:5000`

### Способ 2: Docker Run

```bash
docker run -d -p 5000:5000 pos61/the_knopka:latest
```

### Способ 3: Docker Compose

```bash
git clone https://github.com/thecookiel0rd/TheKnopka.git
cd TheKnopka
docker compose up -d
```

## Использование

### Управление статусом

**Включить (ON):**
```bash
curl http://localhost:5000/knopka_on
# или открыть в браузере: http://localhost:5000/knopka_on
```

**Выключить (OFF):**
```bash
curl http://localhost:5000/knopka_off
# или открыть в браузере: http://localhost:5000/knopka_off
```

**Получить текущий статус:**
```bash
curl http://localhost:5000/status
```

### Веб-интерфейс

Откройте в браузере `http://localhost:5000/` для просмотра страницы. Статус будет автоматически обновляться при изменении.



