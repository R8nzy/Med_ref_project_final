# MedRef 🩺

A simple medical reference web app built with **Flask**. Search for a disease and instantly get its description, symptoms, and treatment — pulled live from Wikipedia.

> 🎓 Final course project (Python/Flask). Currently a work in progress — see [Status](#status--known-limitations) below.

---

## Features

- 🔎 **Search by disease name** — type a disease (e.g. `influenza`, `migraine`) and get a description, symptoms, and treatment.
- 🧩 **Search by symptoms** *(UI in place, backend logic in progress)* — planned mode to find possible conditions from a list of symptoms.
- 🌐 **Live data from Wikipedia** — no static database; results are fetched in real time via the Wikipedia API.
- 🎨 **Clean, no-JS interface** — plain HTML/CSS with Flask + Jinja2 templates, GitHub-Light–inspired theme with green accents.

### Planned next
- Reliable extraction of symptoms/treatment sections (Wikipedia's structure isn't always consistent)
- Working "search by symptoms" mode
- Popular diseases/symptoms shown on the homepage
- A "saved results" / wishlist-style feature for recommended treatments

---

## Tech Stack

| Layer | Tech |
|---|---|
| Backend | Python, Flask |
| Templates | Jinja2, HTML |
| Styling | CSS (no frameworks, no JS) |
| Data source | [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) |
| HTTP requests | `requests` |

No JavaScript is used anywhere in this project — all interactivity is handled through standard HTML forms and Flask's GET/POST request cycle.

---

## How It Works

1. User submits a disease name through a search form.
2. The Flask backend queries the **Wikipedia API** (`en.wikipedia.org/w/api.php`):
   - finds the matching article title,
   - pulls the intro paragraph as the description,
   - scans the article's sections for ones mentioning *symptoms* or *treatment* and extracts bullet points from them.
3. The result is rendered back into the page via a Jinja2 template — no page reload frameworks, just a server-rendered HTML response.

---

## Project Structure

```
├── main.py        # Flask app: routes + Wikipedia search/parsing logic
├── base.html       # Shared page layout (header/footer)
├── index.html      # Search form + results template
├── style.css       # Site styling (GitHub Light theme, green accents)
└── LICENSE         # MIT License
```

---

## Getting Started

**Requirements:** Python 3.9+

```bash
# 1. Clone the repo
git clone https://github.com/R8nzy/Med_ref_project_final.git
cd Med_ref_project_final

# 2. Install dependencies
pip install flask requests

# 3. Run the app
python main.py
```

Then open **http://127.0.0.1:5000** in your browser.

---

## Status & Known Limitations

This project is **incomplete / actively being developed** as a course assignment:

- Symptom and treatment extraction can return empty results for some diseases, since Wikipedia's article structure isn't perfectly consistent across pages.
- The "search by symptoms" mode is not yet implemented on the backend.
- No database — every search hits Wikipedia live, so results depend on its API being available.

---

## License

This project is licensed under the [MIT License](LICENSE).

---
---

# MedRef 🩺 (Русская версия)

Простой медицинский справочник на **Flask**. Вводишь название болезни — получаешь описание, симптомы и лечение, взятые в реальном времени из Wikipedia.

> 🎓 Финальный проект курса (Python/Flask). Проект ещё в разработке — см. [Статус и ограничения](#статус-и-известные-ограничения).

---

## Возможности

- 🔎 **Поиск по названию болезни** — например, `influenza`, `migraine` — выводит описание, симптомы и лечение.
- 🧩 **Поиск по симптомам** *(интерфейс готов, логика на backend в разработке)* — режим для поиска возможных болезней по списку симптомов.
- 🌐 **Живые данные из Wikipedia** — без статичной базы данных, всё подгружается в реальном времени через API Wikipedia.
- 🎨 **Простой интерфейс без JS** — чистый HTML/CSS с Flask + Jinja2, стиль в духе GitHub Light с зелёными акцентами.

### Дальше в планах
- Надёжное извлечение симптомов и лечения (структура статей Wikipedia не всегда одинаковая)
- Рабочий режим "поиск по симптомам"
- Популярные болезни/симптомы на главной странице
- Сохранение/вишлист рекомендованных лекарств

---

## Технологии

| Слой | Технология |
|---|---|
| Backend | Python, Flask |
| Шаблоны | Jinja2, HTML |
| Стили | CSS (без фреймворков и JS) |
| Источник данных | [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) |
| HTTP-запросы | `requests` |

JavaScript в проекте не используется — вся интерактивность реализована через обычные HTML-формы и цикл запросов GET/POST во Flask.

---

## Как это работает

1. Пользователь вводит название болезни в форму поиска.
2. Backend на Flask делает запрос к **Wikipedia API** (`en.wikipedia.org/w/api.php`):
   - находит подходящую статью,
   - берёт вступительный абзац как описание,
   - ищет в разделах статьи те, что упоминают *симптомы* или *лечение*, и достаёт из них пункты списка.
3. Результат отображается на странице через шаблон Jinja2 — без фреймворков для динамической отрисовки, просто HTML-ответ от сервера.

---

## Структура проекта

```
├── main.py        # Flask-приложение: роуты + логика поиска/парсинга Wikipedia
├── base.html       # Общий каркас страницы (хедер/футер)
├── index.html      # Форма поиска + шаблон результатов
├── style.css       # Стили сайта (GitHub Light, зелёные акценты)
└── LICENSE         # Лицензия MIT
```

---

## Установка и запуск

**Требования:** Python 3.9+

```bash
# 1. Клонируем репозиторий
git clone https://github.com/R8nzy/Med_ref_project_final.git
cd Med_ref_project_final

# 2. Устанавливаем зависимости
pip install flask requests

# 3. Запускаем приложение
python main.py
```

Затем открой **http://127.0.0.1:5000** в браузере.

---

## Статус и известные ограничения

Проект **не завершён** и активно разрабатывается в рамках курсового задания:

- Извлечение симптомов и лечения иногда возвращает пустой результат — структура статей в Wikipedia не идеально одинакова для всех болезней.
- Режим "поиск по симптомам" пока не реализован на backend.
- Базы данных нет — каждый поиск идёт напрямую в Wikipedia, поэтому результат зависит от доступности их API.

---

## Лицензия

Проект распространяется под лицензией [MIT](LICENSE).
