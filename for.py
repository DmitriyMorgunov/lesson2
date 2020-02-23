"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

schollScores = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4б', 'scores': [1,3,4,2,1]}, {'school_class': '4в', 'scores': [1,1,1,5,5]}]

def main():
    SumMidPointClass = 0
    numOfClasses = len(schollScores)
    for schollScore in schollScores:
        MidPointClass = sum(schollScore['scores'])/len(schollScore['scores'])
        SumMidPointClass = SumMidPointClass + MidPointClass
        print('Средний бал по классу {}: {}'.format(schollScore['school_class'], MidPointClass))
    print('Средний бал по всей школе: {}'.format(SumMidPointClass/numOfClasses))

def num10():
    listOfK = []
    for k in range(11):
        listOfK.append(k)
    for k in listOfK:
        print(k+1)

if __name__ == "__main__":
    main()
    num10()
