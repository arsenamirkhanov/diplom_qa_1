

# QA Python Diplom Project

Проект демонстрирует работу с классами для моделирования бургера: булочки, ингредиенты, сборка бургера. Также включены автотесты с покрытием кода.


---

## Структура проекта

```bash

qa-python-diplom/
├── bun.py                  # Класс Bun
├── burger.py               # Класс Burger
├── ingredient.py           # Класс Ingredient
├── ingredient\_types.py     # Типы ингредиентов (SAUCE, FILLING)
├── database.py             # Класс Database с набором булок и ингредиентов
├── praktikum\_main.py       # Основной скрипт для сборки бургера
├── tests/                  # Папка с тестами
│   ├── test\_bun.py
│   ├── test\_burger.py
│   └── test\_ingridient.py
└── README.md

````
---

## Установка

1. Создать виртуальное окружение (рекомендуется):
```bash
python3 -m venv .venv
````

2. Активировать виртуальное окружение:

* Для macOS/Linux:

```bash
source .venv/bin/activate
```

* Для Windows:

```cmd
.venv\Scripts\activate
```

3. Установить зависимости (pytest и pytest-cov):

```bash
pip install -U pip
pip install pytest pytest-cov
```

---

## Запуск проекта

Чтобы собрать и вывести рецепт бургера:

```bash
python3 praktikum_main.py
```

---

## Запуск автотестов

Для запуска всех тестов:

```bash
pytest tests/
```

---

## Запуск тестов с покрытием

Для проверки покрытия кода и создания HTML-отчёта:

```bash
pytest --cov=./ --cov-report=term-missing --cov-report=html tests/
```

После этого HTML-отчёт появится в папке `htmlcov/`. Чтобы открыть его в браузере:

```bash
open htmlcov/index.html   # macOS
start htmlcov\index.html  # Windows
```

---

## Описание классов

* **Bun** — булочка с названием и ценой.
* **Ingredient** — ингредиент (начинка или соус) с названием, типом и ценой.
* **Burger** — сборка бургера с булочками и ингредиентами; поддерживает добавление, удаление, перемещение ингредиентов и вывод чека.
* **Database** — хранит набор доступных булок и ингредиентов.

```
