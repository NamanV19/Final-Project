from SequenceTransformer import AxiomTransformer
from Coordinates_Generator import Tree
from MandelbrotGenerator import MandelbrotGenerator
from Julia_Generator import JuliaGenerator
import numpy as np


def main():
    while True:
        print("===============**WELCOME TO FRACTALS GENERATOR**===============")
        print("What type of fractals you want to generate?")
        print("--L-system(No.1)\n--Julia(No.2)\n--Mandelbrot(No.3)\n--Exit(No.4)")
        input_fractal_type = int(input("Please input the number"))
        x = 0
        y = 0
        angle = 90
        cords_x = [0]
        cords_y = [0]
        saved_x_cords = []
        saved_y_cords = []
        angle1 = []
        saved_angle1 = []
        if input_fractal_type == 1:
            input_axiom = str(input("Please input axiom"))
            rules = {}
            input_no_of_rules = int(input("The number of transformation rules you want to apply"))
            # How many rules to be applied to axiom and processed axiom
            for i in range(input_no_of_rules):
                input_rules_key = str(input("Please input letter you want to transform"))
                input_rules_value = str(input("Please input rule corresponding to that letter"))
                rules[input_rules_key] = input_rules_value
            no_of_times_rule_be_applied = int(input("How many times you want the rule to be applied"))
            angle_of_tree = float(input("Please input tree angle"))

            input_choice = int(input("Do you wish to visualize growth of leaves?\nYes(No.1)\nNo(No. 2)"))
            if input_choice == 1:
                # shows the growth of leaves as it plots not only one graph but many under different condition (diff i
                # values)
                for i in range(2, no_of_times_rule_be_applied+1):
                    x = 0
                    y = 0
                    angle = 90
                    saved_x_cords = []
                    saved_y_cords = []
                    angle1 = []
                    saved_angle1 = []
                    cords_x = [0]
                    cords_y = [0]

                    sym_tree = AxiomTransformer(input_axiom, rules, i, angle_of_tree)
                    # stores the processed axiom
                    command = str(sym_tree.iteration())
                    ang = sym_tree.get_angle()
                    first_tree = Tree('Banyan Tree', command, ang, x, y, angle, cords_x, cords_y,  saved_x_cords,
                                      saved_y_cords, angle1, saved_angle1)
                    first_tree.coordinates_generator()
                    first_tree.return_x_cords()
                    first_tree.return_y_cords()
                    # uses inheritance so that the Tree class can access the function of PlotCords which is to plot
                    # graph
                    first_tree.plot_graph()

            # plots the final graph (does not show the process of growth)
            if input_choice == 2:
                sym_tree = AxiomTransformer(input_axiom, rules, no_of_times_rule_be_applied, angle_of_tree)
                command = str(sym_tree.iteration())
                ang = sym_tree.get_angle()

                first_tree = Tree('Banyan Tree', command, ang, x, y, angle, cords_x, cords_y, saved_x_cords,
                                  saved_y_cords, angle1, saved_angle1)
                first_tree.coordinates_generator()
                first_tree.return_x_cords()
                first_tree.return_y_cords()
                first_tree.plot_graph()

        elif input_fractal_type == 2:
            print("No.1 Input the real and imaginary parts of c")
            print("No.2 View Sample 1")
            print("No.3 View Sample 2")
            input_choice = int(input("Please input the number"))
            screen_width = 480
            screen_height = 320
            scale = 300
            # creates a list of x coordinates. The form of the list is changed (it has 1 row and 480 column consisting
            # of elements / x-coordinates) due to function reshape()
            x_cords = np.linspace(-screen_width / scale, screen_width / scale, num=screen_width).reshape((1,
                                                                                                          screen_width))

            # creates a list of y coordinates. The shape of the list is changed (it has 320 row and 1 column consisting
            # of elements)
            y_cords = np.linspace(-screen_height / scale, screen_height / scale, num=screen_height).reshape(
                (screen_height, 1))
            # generates a 2D array in which each element is in complex number form. It represents the complex plane. It
            # contains all the possible coordinates within the range specified earlier (see x_cords and y_cords)
            # np.tile multiplies the elements inside the array. np.tile(x_cords, (screen_height, 1)) generates 320
            # duplicates of x_cords list while 1j * np.tile(y_cords, (1, screen_width)) creates screen_width number of
            # duplicates inside each row in y_cords. (multiplied by 1j so we can distinguish between imaginary and real
            # values). Adding these 2 matrices together results in 2D array which represents complex plane.
            z = np.tile(x_cords, (screen_height, 1)) + 1j * np.tile(y_cords, (1, screen_width))
            # creates 2D array consisting of True values
            m = np.full((screen_height, screen_width), True, dtype=bool)
            # generates 2D array consisting of zero values
            n = np.zeros((screen_height, screen_width))

            if input_choice == 1:
                # allows user to decide real and imaginary value of c unlike in sample, where the values are already
                # fixed
                c_real = float(input("Please input real part of c"))
                c_imaginary = float(input("Please input imaginary part of c"))
                colormap_type = str(input("Please input colour type"))
                # creates a 2D array storing the same complex numbers
                c = np.full((screen_height, screen_width), complex(c_real, c_imaginary))
                general_julia = JuliaGenerator(screen_width, screen_height, scale, x_cords, y_cords, z, c, m, n,
                                               colormap_type)
                general_julia.julia_calculator()
                general_julia.plot_julia()

            # view sample 1
            elif input_choice == 2:
                c = np.full((screen_height, screen_width), complex(-0.4, 0.6))
                general_julia = JuliaGenerator(screen_width, screen_height, scale, x_cords, y_cords, z, c, m, n,
                                               "gist_earth")
                general_julia.julia_calculator()
                general_julia.plot_julia()

            # view sample 2
            elif input_choice == 3:
                c = np.full((screen_height, screen_width), complex(-0.624, 0.435))
                general_julia = JuliaGenerator(screen_width, screen_height, scale, x_cords, y_cords, z, c, m, n,
                                               "summer")
                general_julia.julia_calculator()
                general_julia.plot_julia()

        elif input_fractal_type == 3:
            # in mandelbrot set z always starts with 0
            z = complex(0, 0)
            # initial value to be passed into class, will store the coordinates of the complex plane later
            cx = 0
            cy = 0
            c = complex(cx, cy)
            input_choice = int(input("No.1 Input zoom values manually\nNo.2 View sample 1\nNo.3 View sample 2"))
            if input_choice == 1:
                # allows user to input zoom values and color map
                x1 = float(input("Please input x1 value"))
                x2 = float(input("Please input x2 value"))
                y1 = float(input("Please input y1 value"))
                y2 = float(input("Please input y2 value"))
                color_map = str(input("Please input the color type"))
                x_axis = np.linspace(x1, x2, 1000)
                y_axis = np.linspace(y1, y2, 1000)
                x_axis_len = len(x_axis)
                y_axis_len = len(y_axis)
                atlas = np.empty((x_axis_len, y_axis_len))
                general_mandelbrot = MandelbrotGenerator(120, 1000, x_axis, y_axis, x_axis_len, y_axis_len, atlas, z, cx
                                                            , cy, c, color_map)
                # values to be passed to and organized by mandelbrot function which in turn calls mandelbrot_calculator
                # - function so that the z values are tested
                general_mandelbrot.mandelbrot()
                # plots and save the mandelbrot image
                general_mandelbrot.return_atlas()

            # View sample 1
            elif input_choice == 2:
                x_axis = np.linspace(-2.55, 0.75, 1000)
                y_axis = np.linspace(-1.5, 1.5, 1000)
                x_axis_len = len(x_axis)
                y_axis_len = len(y_axis)
                atlas = np.empty((x_axis_len, y_axis_len))

                general_mandelbrot = MandelbrotGenerator(120, 1000, x_axis, y_axis, x_axis_len, y_axis_len, atlas, z, cx
                                                         , cy, c, "hot")
                general_mandelbrot.mandelbrot()
                general_mandelbrot.return_atlas()

            # View Sample 2
            elif input_choice == 3:
                x_axis = np.linspace(-0.22, -0.21, 1000)
                y_axis = np.linspace(-0.70, -0.69, 1000)
                x_axis_len = len(x_axis)
                y_axis_len = len(y_axis)
                atlas = np.empty((x_axis_len, y_axis_len))
                general_mandelbrot = MandelbrotGenerator(120, 1000, x_axis, y_axis, x_axis_len, y_axis_len, atlas, z, cx
                                                         , cy, c, "hot")
                general_mandelbrot.mandelbrot()
                general_mandelbrot.return_atlas()

        elif input_fractal_type == 4:
                break


main()
