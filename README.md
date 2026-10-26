# Агентство А.

Семейные детективные квесты для кухонного стола. Основа игры бумажная: поле, карточки, улики. Телефон дополняет её через QR-коды: приветствие агента, детектор правды, сейф и награждение.

Сайт: https://alexander-hairdresser.github.io/agent-a-quests/

## Дело № 001. Фисташковый след

Ссылки для QR-кодов:

| Экран | Ссылка |
|---|---|
| Агент А. | https://alexander-hairdresser.github.io/agent-a-quests/case-001/#start |
| Детектор правды | https://alexander-hairdresser.github.io/agent-a-quests/case-001/#detector |
| Сейф | https://alexander-hairdresser.github.io/agent-a-quests/case-001/#final |
| Награда | https://alexander-hairdresser.github.io/agent-a-quests/case-001/#award |

Код сейфа: Б → В → А.

Видео агента: положи `agent-hello.mp4` и `agent-final.mp4` в `case-001/video/`. Пока файлов нет, на экранах показывается текст.

## Как устроено

```
index.html              главная агентства со списком дел
case-001/index.html     готовая игра, один файл, работает и без интернета
case-001/video/         видео агента А.
engine/template.html    движок: экраны, стили, логика, тексты дела (объект CASE)
engine/build.py         сборщик: подставляет стикеры в шаблон
cases/case-001/stickers PNG-стикеры персонажей
```

Пересобрать дело после правок:

```
pip install pillow
python3 engine/build.py case-001
```

## Как сделать новое дело

1. Скопировать `cases/case-001` в `cases/case-002` и заменить стикеры, сохранив имена файлов (или поправив их в шаблоне).
2. Поправить тексты, код сейфа и вердикты детектора в объекте `CASE` в `engine/template.html`. Если дело сильно отличается, шаблон можно скопировать под него.
3. Запустить `python3 engine/build.py case-002`.
4. Добавить карточку дела на главную `index.html`.
