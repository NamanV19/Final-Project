import matplotlib.pyplot as plt
import numpy as np


class JuliaGenerator:
    # kindly see the function main() to see the values which are passed to these variables.
    def __init__(self, screen_width, screen_height, scale, x_cords, y_cords, Z, C, M, N, colormap_type):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scale = scale
        self.x_cords = x_cords
        self.y_cords = y_cords
        self.Z = Z
        self.C = C
        self.M = M
        self.N = N
        self.colormap_type = colormap_type

    def julia_calculator(self):
        # note that Z, C, M, N are 2D arrays.
        for i in range(256):
            # We want to process the whole coordinates at once, hence we used 2D arrays. Z contains all the coordinates
            # on the complex plane. (the coordinates are already converted into complex form).
            # self.Z[self.M] means boolean indexing. Values of Z for which M contains true are selected.
            self.Z[self.M] = self.Z[self.M] * self.Z[self.M] + self.C[self.M]
            # for the magnitude of the values of array Z which exceed 2, M will store false. So that next time, the
            # values which are processed are the "True" values (values of Z which do not exceed 2)
            self.M[abs(self.Z) > 2] = False
            # to color the Julia fractals
            self.N[self.M] = i

    # plot the Julia fractals, remove the axes and save the figure.
    def plot_julia(self):
        fig = plt.figure()
        fig.set_size_inches(self.screen_width / 100, self.screen_height / 100)
        ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.imshow(np.flipud(self.N), cmap=self.colormap_type)
        plt.savefig('julia-plt.png')
        plt.close()


# ref:[https://tomroelandts.com/articles/how-to-compute-colorful-fractals-using-numpy-and-matplotlib]
