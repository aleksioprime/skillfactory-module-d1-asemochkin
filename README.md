# skillfactory-module-d1-asemochkin
Практика D1

Реализована модификация проекта TODO:
1. Рядом с названием колонки отображается цифра, отражающая количество задач в ней. 
```
% python3 trello.py
Нужно сделать (3)
        1. Научиться использовать Trello API | id: 60170e86080e406fd585c704
        2. Изучить Python | id: 60180cbe66a9d587dca17f94
        3. Изучить Python | id: 6018075f07462513ad30a03e
В процессе (2)
        1. Написать программу | id: 6018141b7f317b32bd2d2470
        2. Изучить Python | id: 601713ad5812546ad1759e89
```

2. Реализована функция создания списка задач и модифицирована функция создания задачи.
```
% python3 trello.py create_card "Изучить логирование" "Дополнительные задачи"
% python3 trello.py
Дополнительные задачи (1)
        1. Изучить логирование | id: 60182788b9406848e0a0fabc
Нужно сделать (3)
        1. Научиться использовать Trello API | id: 60170e86080e406fd585c704
        2. Изучить Python | id: 60180cbe66a9d587dca17f94
        3. Изучить Python | id: 6018075f07462513ad30a03e
В процессе (2)
        1. Написать программу | id: 6018141b7f317b32bd2d2470
        2. Изучить Python | id: 601713ad5812546ad1759e89
        
% python3 trello.py create_list "Готово"
% python3 trello.py
Готово (0)
        Нет задач!
Дополнительные задачи (1)
        1. Изучить логирование | id: 60182788b9406848e0a0fabc
Нужно сделать (3)
        1. Научиться использовать Trello API | id: 60170e86080e406fd585c704
        2. Изучить Python | id: 60180cbe66a9d587dca17f94
        3. Изучить Python | id: 6018075f07462513ad30a03e
В процессе (2)
        1. Написать программу | id: 6018141b7f317b32bd2d2470
        2. Изучить Python | id: 601713ad5812546ad1759e89
```

3. Модифицирована функция перемещения задачи в другой список с учётом наличия совпадений нескольких задач по имени:
```
% python3 trello.py move "Изучить Python" "Готово"
Таких задач несколько:
1. Изучить Python (id: 60180cbe66a9d587dca17f94, описание: Работа с requests) - НУЖНО СДЕЛАТЬ
2. Изучить Python (id: 6018075f07462513ad30a03e, описание: Работа с фреймворком Django) - НУЖНО СДЕЛАТЬ
3. Изучить Python (id: 601713ad5812546ad1759e89, описание: Основы языка Python) - В ПРОЦЕССЕ
Введите номер задачи: 3
% python3 trello.py
Готово (1)
        1. Изучить Python | id: 601713ad5812546ad1759e89
Дополнительные задачи (1)
        1. Изучить логирование | id: 60182788b9406848e0a0fabc
Нужно сделать (3)
        1. Научиться использовать Trello API | id: 60170e86080e406fd585c704
        2. Изучить Python | id: 60180cbe66a9d587dca17f94
        3. Изучить Python | id: 6018075f07462513ad30a03e
В процессе (1)
        1. Написать программу | id: 6018141b7f317b32bd2d2470
```
