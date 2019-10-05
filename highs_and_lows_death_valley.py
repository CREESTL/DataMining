import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "death_valley.csv"
with open(filename) as f:
    reader = csv.reader(f)

    highs, lows, dates = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print("missing data !")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

plt.figure(figsize = (10, 6))
plt.title("Temperatures of Death Valley")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.tick_params(axis = "both", which = "major", labelsize = 18)
plt.plot(dates, highs, color = "red", linewidth = 3)
plt.plot(dates, lows, color = "blue", linewidth = 3)
plt.fill_between(dates, highs, lows, color = "yellow", alpha = 0.5)
plt.show()