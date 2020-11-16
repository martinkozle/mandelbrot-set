class FractalGenerator:
    def calculate_point(self, x0, y0):
        raise NotImplementedError

    def color_from_iteration(self, iteration):
        raise NotImplementedError


class MandelbrotSetGenerator(FractalGenerator):
    def __init__(self, max_iterations=256):
        self.max_iterations = max_iterations
        self.palette = [
            (66, 30, 15),
            (25, 7, 26),
            (9, 1, 47),
            (4, 4, 73),
            (0, 7, 100),
            (12, 44, 138),
            (24, 82, 177),
            (57, 125, 209),
            (134, 181, 229),
            (211, 236, 248),
            (241, 233, 191),
            (248, 201, 95),
            (255, 170, 0),
            (204, 128, 0),
            (153, 87, 0),
            (106, 52, 3)
        ]

    def color_from_iteration(self, iteration):
        if iteration < self.max_iterations:
            return self.palette[iteration % 16]
        return 0, 0, 0

    def calculate_point(self, x0, y0):
        iteration = 0
        x2 = 0
        y2 = 0
        w = 0
        while x2 + y2 <= 4 and iteration < self.max_iterations:
            x = x2 - y2 + x0
            y = w - x2 - y2 + y0
            x2 = x * x
            y2 = y * y
            w = (x + y) * (x + y)
            iteration += 1
        return iteration
