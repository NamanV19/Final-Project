import matplotlib.pyplot as plt


class MandelbrotGenerator:
    def __init__(self, max_iter, density,  x_axis, y_axis, x_axis_len, y_axis_len, atlas, z, cx, cy, c, color_map):
        self.max_iter = max_iter
        self.density = density
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_axis_len = x_axis_len
        self.y_axis_len = y_axis_len
        self.atlas = atlas
        self.z = z
        self.cx = cx
        self.cy = cy
        self.c = c
        self.color_map = color_map

    def mandelbrot(self):
        # iterates through each and every coordinates
        for ix in range(self.x_axis_len):
            for iy in range(self.y_axis_len):
                self.cx = self.x_axis[ix]
                self.cy = self.y_axis[iy]
                self.c = complex(self.cx, self.cy)
                # test the c values and iteration stored in atlas
                self.atlas[ix, iy] = self.mandelbrot_calculator(self.c, self.max_iter)
                pass
            pass

    # In mandelbrot set the z value starts with 0
    def mandelbrot_calculator(self, c, max_iter):
        # z = complex(0, 0) is the same as 0 + 0j
        self.z = complex(0, 0)
        for iteration in range(max_iter):
            self.z = (self.z * self.z) + self.c
            # checks if the magnitude of z i greater than 4
            if abs(self.z) > 4:
                break
                pass
            pass
        # if magnitude of z greater than 4, return i value
        return iteration

    # generates mandelbrot image
    def return_atlas(self):
        plt.imshow(self.atlas.T, cmap=self.color_map, interpolation="nearest")
        plt.savefig('mandelbrot-plt.png')
        plt.close()


# reference:[Make Your Own Mandelbrot by Tariq Rashid and
# https://github.com/danyaal/mandelbrot/blob/master/mandelbrot.py]
