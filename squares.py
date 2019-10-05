import matplotlib.pyplot as plt

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))

plt.plot(nums, squares, linewidth = 2, color = "red")
plt.title("SQAURES", fontsize = 24)
plt.xlabel("numbers", fontsize = 18)
plt.ylabel("squares", fontsize = 18)
plt.tick_params(axis = "both", labelsize = 14)# расстановка делений на осях, labelsize - фактически масштаб
plt.show()

