import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    highs, lows, dates = [], [], []
    for row in reader:
        highs.append(int(row[1]))
        lows.append(int(row[3]))
        dates.append(datetime.strptime(row[0], "%Y-%m-%d"))

plt.figure(figsize = (10, 6))
plt.xlabel("Month")
plt.ylabel("Highest/Lowest temperature")
plt.title("Temperatures of 2014 in Sitka", fontsize = 18, color = "purple")
plt.tick_params(axis = "both", labelsize = 14)
plt.plot(dates, highs, color = "red")
plt.plot(dates, lows, color = "blue")
plt.fill_between(dates, highs, lows, facecolor = "yellow", alpha = 0.5)
plt.show()
