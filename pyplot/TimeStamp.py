import matplotlib.dates as md
import matplotlib.pyplot as plt
import datetime as dt

x = [1524195763,1524195773,1524195783,1524195793]
y = [5,7,4,0]

dates = [dt.datetime.fromtimestamp(ts) for ts in x]
datenums = md.date2num(dates)

ax = plt.gca()
# xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
xfmt = md.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)

plt.plot(datenums, y, color='green', linestyle='dashed')
plt.show()