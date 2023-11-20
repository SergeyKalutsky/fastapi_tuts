import requests


base_url = 'http://127.0.0.1:8000'

name = input('Введите имя пользователя: ')
res = requests.post(base_url + '/create_user', json={'name': name})
data = res.json()
while data['status'] != 'ok':
    print('Ошибка. Пользователь с таким именем уже существует')
    name = input('Введите имя пользователя')
    res = requests.post(base_url + '/create_user', json={'name': name})


user_id = data['user_id']
while True:
    command = input('Введите команду:\n1 - написать сообщение,\n2 - посмотреть сообщения,\n3 - выйти\n')
    if command == '1':
        msg = input('Введите сообщение: ')
        res = requests.post(base_url + '/save_message/', json={'user_id': user_id, 'text': msg})
        data = res.json()
        if data['status'] == 'ok':
            print('Сообщение успешно отправлено')
        else:
            print('Не удалось отправить сообщение')
    if command == '2':
        res = requests.get(base_url + '/messages/')
        data = res.json()
        print(data)
    if command == '3':
        break
        
    