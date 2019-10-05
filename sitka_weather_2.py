import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #выведем название показания и его позицию в строке
    for (index, number) in enumerate(header_row):
        print(index, " ", number)
    #выведем все ежедневные высшие температуры с датами
    dates = []
    highs = []
    for row in reader:
        highs.append(int(row[1]))
        dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
    print(highs)
plt.figure(figsize=(10, 6))

plt.plot(dates, highs, linewidth = 2, color = "red")
plt.xlabel("Month")
plt.ylabel("Highest temperature")
plt.title("Highest temperatures of the year", color = "Green")
plt.tick_params(axis = "both", labelsize = 8, which = "major")
plt.show()