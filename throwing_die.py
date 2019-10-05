'''
Pygal нужен для приложений, имеющих разное представление на разных экранах
Он легко мсштабируется

'''
import pygal
import random


#Класс Кубика
class Die():
    def __init__(self):
        self.num_sides = 6
    def roll(self):
        return random.randint(1, self.num_sides) #возвращает случайное значение от 1 до кол-ва сторон кубика



die = Die()
results = []
for i in range(1000):
    results.append(die.roll()) #все результаты 1000 бросков кубика

#посчитает частоты каждого результата
frequencies = {}
for value in results:
    frequencies[value] = results.count(value)# словарь: значение-частота

"""CREATING A HISTOGRAM"""
hist = pygal.Bar()
hist.title = "Results of rolling D6 for a 1000 times" #здесь уже нет скобок, а через равно!
hist.x_labels = ['1', '2', '3', '4', '5', '6'] # деления на оси x
hist.x_title = "Results" #название оси х
hist.y_title = "Frequencies" # название оси y

hist.add("D6", frequencies.values()) #D6 - метка, frequances.values() - значения, которые будут отображаться
hist.render_to_file("die_visual.svg")

