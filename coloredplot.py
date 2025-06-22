import matplotlib.pyplot as plt

x = [5, 8, 10]
y = [12, 16, 6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]

plt.plot(x, y, "g", label="line one", linewidth=20)
plt.plot(x2, y2, "r", label="line two", linewidth=50)

plt.title("Information")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()
plt.grid(True, color="k")
plt.show()
