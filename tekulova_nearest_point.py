import matplotlib.pyplot as plt

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        steps += 1
    return steps

def highest_value(n):
    highest = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        highest = max(highest, n)
    return highest

# Histogram
hist_data = [collatz_steps(i) for i in range(1, 1000001)]
plt.hist(hist_data, bins=100)
plt.title("Histogram of Collatz Steps for Numbers 1-10^6")
plt.xlabel("Number of Steps")
plt.ylabel("Frequency")
plt.show()

# Highest value
x_data = list(range(1, 1000001))
y_data = [highest_value(i) for i in range(1, 1000001)]
plt.plot(x_data, y_data, 'o', markersize=1)
plt.title("Highest Value Reached for Each Number in 1-10^6")
plt.xlabel("Number")
plt.ylabel("Highest Value Reached")
plt.show()
