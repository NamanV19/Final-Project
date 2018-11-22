import matplotlib.pyplot as plt


# Plot the x and y coordinates
class PlotCords:
    def __init__(self, x_cords, y_cords):
        self.x_cords = x_cords
        self.y_cords = y_cords

    def plot_graph(self):
        plt.xlabel("x coordinates")
        plt.ylabel("y_coordinates")
        plt.margins(x=0.1, y=0.1)
        plt.plot(self.x_cords, self.y_cords)
        plt.show()