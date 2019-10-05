'''
Pygal нужен для приложений, имеющих разное представление на разных экранах
Он легко масштабируется

'''
import pygal
import random


#Класс Кубика
class Die():
    def __init__(self):
        self.num_sides = 6
    def roll(self):
        return random.randint(1, self.num_sides) #возвращает случайное значение от 1 до кол-ва сторон кубика



die1 = Die()
die2 = Die()
results = []
for i in range(1000):
    results.append(die1.roll() + die2.roll()) #все результаты 1000 бросков 2 кубиков

#посчитает частоты каждого результата
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))

"""СОЗДАЮ ГИСТОГРАММУ"""
hist = pygal.Bar()
hist.title = "Results of rolling two D6 for a 1000 times" #здесь уже нет скобок, а через равно!
hist.x_labels = list(i for i in range(13))
hist.x_title = "Results" #название оси х
hist.y_title = "Frequencies" # название оси y

hist.add("D6 + D6", frequencies) #D6 - метка, frequances.values() - значения, которые будут отображаться
hist.render_to_file("two_dice_visual.svg")


#упражнение 15-8 при броске трех кубиков D6 наименьший результат будет 3 а наибольший - 18 НАДО ДОКАЗАТЬ
die3 = Die()
results = []
frequencies = []
for i in range(1000):
    results.append(die1.roll() + die2.roll() + die3.roll())
max_result = die1.num_sides * 3
for value in range(1, max_result + 1):
    frequencies.append(results.count(value))
hist = pygal.Bar()
hist.title = "Results of throwing three D6 for a 1000 times"
hist.x_labels = list(i for i in range(19))
hist.x_title = "Results"
hist.y_title = "Frequencies"
hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file("three_dice_visual.svg")
