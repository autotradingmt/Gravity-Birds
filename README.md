# Gravity Birds

Новая игра с нуля на Python по мотивам физической аркады:

- окно `1920x1080`
- меню с описанием птиц
- экран выбора из 5 уровней
- 4 вида птиц: `red`, `black`, `blue`, `yellow`
- рогатка, натяг, траектория
- разные планеты и разная гравитация
- большие разрушаемые конструкции
- физика на `pymunk`

## Запуск

```bash
cd /Users/foxsovich/gravity_birds_dialogue
source .venv/bin/activate
python main.py
```

## Web Version

Теперь есть браузерная версия игры:

```bash
cd /Users/foxsovich/Documents/gravity_birds_no_trail_153502
python3 server.py
```

После запуска на своем ноутбуке открой:

```text
http://127.0.0.1:8015/
```

Для игры с других устройств в том же Wi-Fi используй адрес, который сервер напечатает в строке `Wi‑Fi`, например:

```text
http://192.168.1.23:8015/
```

Домен для этого не нужен. Ноутбук должен оставаться включенным, а `server.py` должен быть запущен.

## GitHub Pages

Если нужна ссылка, которая открывается с любого Wi-Fi, проект можно выложить на `GitHub Pages` бесплатно.

Что уже подготовлено:

- workflow для публикации: `.github/workflows/deploy-pages.yml`
- статический сайт берется прямо из папки `web/`

Что нужно сделать дальше:

1. Создать пустой репозиторий на GitHub, например `gravity-birds`.
2. В этой папке выполнить:

```bash
cd /Users/foxsovich/Documents/gravity_birds_no_trail_153502
git init
git add .
git commit -m "Initial Gravity Birds web release"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/gravity-birds.git
git push -u origin main
```

3. На GitHub открыть `Settings -> Pages` и убедиться, что source = `GitHub Actions`.
4. Подождать завершения workflow `Deploy Gravity Birds to GitHub Pages`.

После этого ссылка обычно будет такой:

```text
https://YOUR_USERNAME.github.io/gravity-birds/
```

Важно: сейчас `web/index.html` загружает `matter.js` с CDN, поэтому для опубликованной версии у игроков должен быть доступ в интернет.

## Управление

- ЛКМ по меню: открыть уровни
- ЛКМ по карточке уровня: старт
- Зажать ЛКМ на рогатке и отпустить: выстрел
- `Space` или ЛКМ во время полета желтой птицы: ускорение
- `R`: перезапуск уровня
- `Esc`: назад / выход

## Что дальше для версии по ссылке

Локальная версия уже готова для игры на компьютере. Для браузерной публикации следующий практичный шаг: собрать проект через `pygbag` в статический web-билд и выложить его на GitHub Pages или Netlify.

## Тестирование

Проверка разбита на два слоя:

- сценарные тесты механик
- stress/fuzz прогон физики по всем уровням
- autoplay-бот с эвристическим прицеливанием по свиньям
- детектор застрявших объектов и невалидных физсостояний
- JSON-отчет по каждому сценарию

Запуск:

```bash
cd /Users/foxsovich/gravity_birds_dialogue
source .venv/bin/activate
python -m unittest discover -s tests -v
python qa_runner.py
```

После `python qa_runner.py` создается файл `qa_report.json` со сводкой:

- `errors`: исключения и сломанные сценарии
- `warnings`: подозрения на застревание объектов
- `wins/losses/unfinished`: исходы сценариев
- `avg_fps`: скорость headless-симуляции
- подробный результат по каждому прогону уровня
