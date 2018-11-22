class AxiomTransformer():
    def __init__(self, sequence, transformations, iterations, angle2):
        self.sequence = sequence
        self.transformations = transformations
        self.iterations = iterations
        self.angle2 = angle2

    def iteration(self):
        for j in range(self.iterations):
            # method get(c, c) gets the value of the key of a dictionary(transformations)
            # the function of ''.join is to join strings without any separator
            self.sequence = ''.join(self.transformations.get(c, c) for c in self.sequence)
        return self.sequence

    def get_angle(self):
        return self.angle2

# ref:[https://bitaesthetics.com/posts/fractal-generation-with-l-systems.html]
