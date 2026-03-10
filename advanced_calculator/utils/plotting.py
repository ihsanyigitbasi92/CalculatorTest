import matplotlib.pyplot as plt

def plot_function(func, x_range):
    x_values = np.linspace(x_range[0], x_range[1], 100)
    y_values = func(x_values)
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Function Plot')
    plt.grid(True)
    plt.show()
