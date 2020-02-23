"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    answer = ''
    while answer != 'Хорошо':
        answer = input('Как дела? ')
    print('Ну и молодец!')

if __name__ == "__main__":
    ask_user()
