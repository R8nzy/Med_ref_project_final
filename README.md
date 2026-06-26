# MedRef 🩺

A simple medical reference web app built with **Flask**. Search for a disease and instantly get its description, symptoms, and treatment — pulled live from Wikipedia.

MedRef 🩺
A medical reference web app built with Flask that fetches disease descriptions, symptoms, and treatments live from Wikipedia.

⚠️ IMPORTANT: This project is a work in progress and will be continuously updated.

There is currently no live deployed website to test it online. It must be run locally.

Some buttons do not have backend logic in the main version (main.py) yet. However, these features are actively being developed in the notmain.py file, which will replace the main one once everything works correctly.

Features & Tech Stack
Live Wikipedia Data — Fetches real-time info via Wikipedia API (using requests).

No-JS Interface — Server-rendered HTML/CSS using Flask + Jinja2 templates.

Clean UI — Minimalist design with green accents.

Planned next
Fix bugs and optimize content extraction so everything works without errors.

Update and improve the UI buttons.

Implement new features (including the "search by symptoms" backend logic and a wishlist).

Getting Started (Local Run)
Requirements: Python 3.9+

Bash
# 1. Clone the repo
git clone https://github.com/R8nzy/Med_ref_project_final.git
cd Med_ref_project_final

# 2. Install dependencies
pip install flask requests

# 3. Run the app
python main.py
Open http://127.0.0.1:5000 in your browser.

Known Limitations
Wikipedia's article structure varies, so symptom/treatment extraction may occasionally be empty.

"Search by symptoms" UI is ready, but backend logic is still in progress.

-----------------------------------------------------------------------------------------------------------------------------------------


# MedRef 🩺 (Русская версия)
Медицинский справочник на Flask, который подгружает описание болезней, симптомы и методы лечения в реальном времени из Wikipedia.

⚠️ ВАЖНО: Проект находится в разработке и будет дорабатываться.

Онлайн-демо (сайта) пока нет, протестировать работу можно только при локальном запуске.

Под некоторые кнопки пока нет функционала в основной версии (main.py), но в файле notmain.py сейчас ведется решение этой задачи. В будущем он заменит основной файл и всё будет работать корректно.

Возможности и Технологии
Живые данные — Запросы к API Wikipedia в реальном времени (библиотека requests).

Интерфейс без JS — Чистый HTML/CSS, логика на Flask + шаблоны Jinja2.

Стильный UI — Минималистичный дизайн с зелеными акцентами.

Дальше в планах
Доработать парсинг и исправить ошибки, чтобы всё отображалось корректно.

Изменить и улучшить кнопки в интерфейсе.

Добавить новые функции (включая логику поиска по симптомам и вишлист).

Запуск проекта
Требования: Python 3.9+

Bash
# 1. Клонируем репозиторий
git clone https://github.com/R8nzy/Med_ref_project_final.git
cd Med_ref_project_final

# 2. Устанавливаем зависимости
pip install flask requests

# 3. Запускаем приложение
python main.py
Открой http://127.0.0.1:5000 в бразере.

Ограничения
Структура статей в Wikipedia различается, поэтому блок симптомов или лечения иногда может быть пустым.

Кнопки поиска по симптомам есть в UI, но логика на бэкенде ещё пишется.

## Лицензия

Проект распространяется под лицензией [MIT](LICENSE).
