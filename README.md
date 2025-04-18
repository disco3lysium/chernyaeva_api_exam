📁 README.md — FastAPI Task Manager

# ✅ Task Manager API (FastAPI)

Это простое FastAPI-приложение для учёта задач в проекте.  
API позволяет создавать, обновлять, удалять и просматривать задачи в формате REST.

## 📌 Возможности API

Доступные эндпоинты:

- GET /tasks — Получить список всех задач
- POST /tasks — Создать новую задачу
- PUT /tasks/{id} — Обновить задачу по её ID
- DELETE /tasks/{id} — Удалить задачу по её ID

## 📘 Примеры запросов и ответов

### GET /tasks

📥 Пример запроса:

GET http://127.0.0.1:8000/tasks

📤 Ответ:

```json
[
  {
    "id": 1,
    "title": "Задача 1",
    "description": "Описание задачи 1",
    "status": "open"
  },
  {
    "id": 2,
    "title": "Задача 2",
    "description": "Описание задачи 2",
    "status": "completed"
  }
]
```

---

### POST /tasks

📥 Тело запроса:

```json
{
  "title": "Новая задача",
  "description": "Описание новой задачи",
  "status": "open"
}
```

📤 Ответ:

```json
{
  "id": 3,
  "title": "Новая задача",
  "description": "Описание новой задачи",
  "status": "open"
}
```

---

### PUT /tasks/{id}

📥 Тело запроса:

```json
{
  "title": "Обновленная задача",
  "description": "Описание обновленной задачи",
  "status": "completed"
}
```

📤 Ответ:

```json
{
  "id": 1,
  "title": "Обновленная задача",
  "description": "Описание обновленной задачи",
  "status": "completed"
}
```

---

### DELETE /tasks/{id}

📤 Ответ:

```json
{
  "message": "Задача с id 1 успешно удалена"
}
```

---

## 🚀 Запуск проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/ВАШ_ПОЛЬЗОВАТЕЛЬ/ВАШ_РЕПОЗИТОРИЙ.git
cd ВАШ_РЕПОЗИТОРИЙ
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Запустите сервер:

```bash
uvicorn main:app --reload
```

Откройте браузер и перейдите по адресу http://127.0.0.1:8000.

## 🧾 Документация OpenAPI

Swagger-интерфейс доступен по адресу:

📄 http://127.0.0.1:8000/docs

Здесь вы можете протестировать API с помощью визуального интерфейса.

## ✅ Валидация входных данных

Валидация параметров запроса (title, description, status) выполняется с помощью библиотеки Pydantic.

- title — строка, обязательна
- description — строка, обязательна
- status — одно из значений: "open", "in_progress", "completed"

## 🧪 Тестирование

Проект был протестирован в Postman. Проведены следующие действия:

- Создание задач (POST)
- Получение всех задач (GET)
- Обновление задачи (PUT)
- Удаление задачи (DELETE)

К каждому запросу написаны тесты (Postman Test Scripts), проверяющие:

- Статус ответа (200, 201, 204)
- Корректность тела ответа
- Поведение при удалении и повторных операциях

Все тесты прошли успешно ✅
