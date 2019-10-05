#писал сам, без книги

import matplotlib.pyplot as plt
import random
class RandomWalk():
    def __init__(self, num_of_points):
        self.num_of_points = num_of_points
        self.x_values = [0] #хождение начинается с (0, 0) а затем в массивы добавляются точки и по массивам выводится на экран
        self.y_values = [0]
        self.x_directions = [ "left", "right" ]
        self.y_directions = [ "up", "down" ]
        self.max_distance = 4
        self.edgecolor = "none"
        self.color = "red"
        self.dot_size = 1
    def x_step(self):
        for i in range(self.num_of_points):
            direction = random.choice(self.x_directions)
            length = random.randint(1, self.max_distance)
            if direction == "left":
                step = -1 * length
            elif direction == "right":
                step = 1 * length
            if step == 0:
                pass
            next_x = self.x_values[-1] + step
            self.x_values.append(next_x)
    def y_step(self):
        for i in range(self.num_of_points):
            direction = random.choice(self.y_directions)
            length = random.randint(1,self. max_distance)
            if direction == "up":
                step = 1 * length
            elif direction == "down":
                step = -1 * length
            if step == 0:
                pass
            next_y = self.y_values[-1] + step
            self.y_values.append(next_y)
    def draw(self):
        self.x_step()
        self.y_step()
        plt.figure(figsize = (10, 6)) #изменение соотношения сторон окна диаграммы
        plt.title("RANDOM WALK", fontsize = 28)
        plt.scatter(self.x_values, self.y_values, edgecolor = self.edgecolor, s = self.dot_size, color = self.color)
        plt.scatter(self.x_values[-1], self.y_values[-1], edgecolor = "blue", color = "purple", s = self.dot_size + 100)
        plt.scatter(self.x_values[0], self.y_values[0], edgecolor = "blue", color = "purple", s = self.dot_size + 100)
        plt.axes().get_xaxis().set_visible(False)# удаление осей
        plt.axes().get_yaxis().set_visible(False)

        plt.show()



walk = RandomWalk(50000)
walk.draw()




