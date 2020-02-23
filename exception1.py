"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    questionsDictionaries = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Хороша ли погода?": "Хороша"}
    answer = ''
    questionText = "Задай вопрос: "
    while True:
        try:
            questionFromUser = input(questionText)
        except KeyboardInterrupt:
            print('Пока!')
            break
        answer = questionsDictionaries.get(questionFromUser)
        if answer is not None:
            print(answer)
            break
        else:
            questionText = "Не расслышал, что? "

if __name__ == "__main__":
    ask_user()
