import matplotlib as plt



figure, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

ax.plot(x, y)

ax.set_title('Prime Numbers')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.show()