"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():
    questionsDictionaries = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Хороша ли погода?": "Хороша"}
    answer = ''
    questionText = "Задай вопрос: "
    while True:
        questionFromUser = input(questionText)
        # можно сделать проще:
        print(questionsDictionaries.get(questionFromUser, "Не расслышал, что?"))
        # answer = questionsDictionaries.get(questionFromUser)
        # if answer is not None:
        #     print(answer)
        #     break
        # else:
        #     questionText = "Не расслышал, что? "
if __name__ == "__main__":
    ask_user()
