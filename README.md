# skillfactory-module-d1-asemochkin
Практика D1

Реализована модификация проекта TODO:
1. Рядом с названием колонки отображается цифра, отражающая количество задач в ней. 
Для проверки нужно запустить файл с помощью интерпретатора Python в командной строке без аргументов:
```
% python3 trello.py

Нужно сделать (3)
        1. Научиться использовать Trello API
        2. Изучить Python
        3. Изучить Python
В процессе (2)
        1. Написать программу
        2. Изучить Python
```

2. Реализована функция создания списка задач.
Для проверки нужно запустить файл с помощью интерпретатора Python в командной строке c аргументами create_list <имя списка>: 
```
% python3 trello.py create_list "Готово"
% python3 trello.py
Готово (0)
        Нет задач!
Нужно сделать (3)
        1. Научиться использовать Trello API
        2. Изучить Python
        3. Изучить Python
В процессе (2)
        1. Написать программу
        2. Изучить Python
```

3. Модифицирована функция перемещения задачи в другой список с учётом наличия совпадений нескольких задач по имени:
```
% python3 trello.py move "Изучить Python" "Готово"
Таких задач несколько:
1. Изучить Python (время: 2021-02-01T14:14:37.557Z, описание: Работа с requests) - НУЖНО СДЕЛАТЬ
2. Изучить Python (время: 2021-02-01T14:43:43.648Z, описание: Работа с фреймворком Django) - НУЖНО СДЕЛАТЬ
3. Изучить Python (время: 2021-02-01T15:21:45.622Z, описание: Основы языка Python) - В ПРОЦЕССЕ
Введите номер задачи: 3
% python3 trello.py
Готово (1)
        1. Изучить Python
Нужно сделать (3)
        1. Научиться использовать Trello API
        2. Изучить Python
        3. Изучить Python
В процессе (1)
        1. Написать программу
```
