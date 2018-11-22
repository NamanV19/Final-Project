from math import pi, sin, cos
from CoordinatesPlotter import PlotCords


class Tree(PlotCords):
    def __init__(self, name_of_tree, input_command, turn_amount, x, y, angle, x_cords, y_cords, saved_x_cords, saved_y_cords, angle1, saved_angle1):
        self.name_of_tree = name_of_tree
        self.input_command = input_command
        self.turn_amount = turn_amount
        self.x = x
        self.y = y
        self.angle = angle
        self.x_cords = x_cords
        self.y_cords = y_cords
        self.saved_x_cords = saved_x_cords
        self.saved_y_cords = saved_y_cords
        self.angle1 = angle1
        self.saved_angle1 = saved_angle1

    def coordinates_generator(self):
        # nan = float('nan')
        for i in self.input_command:
            # if the code detects capital letter in input_command:
            if i in "ABCDEFGHIJKLMNOPQRST":
                # x and y coordinates' positions depend on current angle
                self.x = self.x - (cos(self.angle * pi / 180))
                # current x coordinate will be appended to x_cords list, similar case with y and angle
                self.x_cords.append(self.x)
                self.y = self.y + (sin(self.angle * pi / 180))
                self.y_cords.append(self.y)
                self.angle1.append(self.angle)

            # if the code detects any lower case letter in input_command:
            if i in "abcdefghijklmnopqrstuvwxyz":
                # The effect will be similar to the first case (if the code detects capital letter in input_command)
                # EXCEPT:
                self.x = self.x - (cos(self.angle * pi / 180))
                # float('nan') will be added to x_cords and y_cords so that no line will be drawn on the output graph
                self.x_cords.append(float('nan'))
                self.x_cords.append(self.x)
                self.y = self.y + (sin(self.angle * pi / 180))
                self.y_cords.append(float('nan'))
                self.y_cords.append(self.y)
                # conclusion: updating the current x and y coordinates without actually plotting the coordinates
                # on graph

            # if "+" is present in the command
            if i == "+":
                # angle will updated (be added with turn_amount)
                self.angle = self.angle + self.turn_amount
                # it will be appended to list containing angles
                self.angle1.append(self.angle)
            if i == "-":
                # angle will be updated (angle - turn_amount)
                self.angle = self.angle - self.turn_amount
                self.angle1.append(self.angle)
            if i == "[":
                # current x, y, angle added to its respective list, in other words, it is saving the current
                # -state of "pointer"
                self.saved_x_cords.append(self.x)
                self.saved_y_cords.append(self.y)
                self.saved_angle1.append(self.angle)
            if i == "]":
                # access the position of the current pointer which was saved. Pop removes and returns last element from
                # list
                self.x = self.saved_x_cords.pop()
                self.y = self.saved_y_cords.pop()
                self.angle = self.saved_angle1.pop()
                self.x_cords.append(float('nan'))
                self.y_cords.append(float('nan'))
                self.x_cords.append(self.x)
                self.y_cords.append(self.y)
                self.angle1.append(self.angle)

    def return_x_cords(self):
        return self.x_cords

    def return_y_cords(self):
        return self.y_cords

    def return_angle(self):
        return self.angle

