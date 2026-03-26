import matplotlib.pyplot as plt
dates = ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"]
march2017 = [100, 102, 105, 103, 106]


plt.subplot(211)
plt.plot(dates, march2017, '--')
plt.title('March Temperatures')
plt.ylabel('Temperature')

plt.subplot(212)
plt.plot(dates, march2017, 'ro')
plt.ylabel('Temperature')
plt.xlabel('Date')

plt.show()
