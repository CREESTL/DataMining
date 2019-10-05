import matplotlib.pyplot as plt


big_nums = list(i for i in range(1,1001))
big_squares = list(map(lambda x: x**2, big_nums))
plt.scatter(big_nums, big_squares, s = 20, edgecolor = "none", color = "blue")# s = размер точек, edgecolor = цвет контуров точек



plt.title("SQUARES", fontsize = 24)
plt.xlabel("numbers", fontsize = 18)
plt.ylabel("squares", fontsize = 18)
plt.tick_params(axis = "both", labelsize = 14)

plt.show()