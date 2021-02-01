import sys 
import requests

auth_params = {    
    'key': "c5a8aacdb5486758ea85df03000db8d0",    
    'token': "e86d14e65e61cf3d079a8b1266a751731ba6929c6e7ae578317ec5c4349663ec", }
base_url = "https://api.trello.com/1/{}"  
board_id = "60170d9c5bc9f95d480bf9cb"

def read():
    """ Функция вывода всех задач в каждом списке по номерам """
    column_data = requests.get(base_url.format('boards') + \
                '/' + board_id + '/lists', params=auth_params).json()
    for column in column_data:
        task_data = requests.get(base_url.format('lists') + \
                '/' + column['id'] + '/cards', params=auth_params).json()
        print('{} ({})'.format(column['name'], len(task_data)))
        if not task_data:
            print('\t' + 'Нет задач!')
            continue
        for num, task in enumerate(task_data):
            print(('\t{}. {} | id: {}').format(num + 1, task['name'], task['id']))

def create_card(name, column_name):
    """ Функция создания задачи с указанным именем в указанном списке """
    column_data = requests.get(base_url.format('boards') + '/' + \
        board_id + '/lists', params = auth_params).json()
    # Поиск существования списка задач с заданным именем и получение его id
    column_id = None
    for column in column_data:
        if column['name'] == column_name:
            column_id = column['id']
            break
    # Если списка задач не найдено, то создаётся новый список и берётся его id
    if column_id is None:
        column_id = create_list(column_name)['id']
    # Создаётся задача в текущем или новом списке
    requests.post(base_url.format('cards'), data={'name': name, 'idList': column_id, **auth_params})

def create_list(name):
    """ Функция создания списка с указанным именем """
    return requests.post(base_url.format('boards') + '/' + \
        board_id + '/lists', data={'name': name, **auth_params}).json()
    

def move(name, column_name):
    """ Функция перемещения задачи в другой список """
    column_data = requests.get(base_url.format('boards') + '/' + \
                        board_id + '/lists', params=auth_params).json()

    # если указанного списка нет на доске, то работа функции прекращается
    if not(list(filter(lambda x: x['name'] == column_name, column_data))):
        print("Такого списка не найдено!")
        return

    tasks = []
    for column in column_data:
        # если задача с введённым именем уже есть в целевом списке, то пропускаем этот список
        if column['name'] != column_name:
            column_tasks = requests.get(base_url.format('lists') + '/' + \
                    column['id'] + '/cards', params=auth_params).json() 
            for task in column_tasks:
                if task['name'] == name:
                    # добавление в список словарей всех найденных задач по имени
                    # с указанием id, даты последней активности, описания и списка, в котором она сейчас находится
                    tasks.append({
                        "id" : task['id'], 
                        "date" : task['dateLastActivity'],
                        "desc": task['desc'],
                        "column_name": column['name']})
    if tasks:
        task_id = tasks[0]['id']
        if len(tasks) > 1:
            # если в списке задач добавлено больше одной задачи, то выводим на экран список найденных задач со всеми данными
            print("Таких задач несколько:\n", "\n".join(
                ["{}. {} (id: {}, описание: {}) - {}".format(i+1, name, x['id'], x['desc'],  x['column_name'].upper()) 
                for i, x in enumerate(tasks)]),sep="")
            # пользователь вводит номер задачи и система фиксирует её id для дальнейшей работы (перемещения)
            task_id = tasks[int(input("Введите номер задачи: "))-1]['id']
        for column in column_data:
            if column['name'] == column_name:
                requests.put(base_url.format('cards') + '/' + task_id + \
                        '/idList', data={'value': column['id'], **auth_params})
                break
    else:
        print("Задача не найдена!")

if __name__ == "__main__":    
    if len(sys.argv) <= 2:    
        read()    
    elif sys.argv[1] == 'create_card':    
        create_card(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'create_list':    
        create_list(sys.argv[2])     
    elif sys.argv[1] == 'move':    
        move(sys.argv[2], sys.argv[3])  