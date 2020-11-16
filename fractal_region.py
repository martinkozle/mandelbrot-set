import numpy as np
import time
import threading
from fractal_generator import FractalGenerator


class FractalRegion:
    def __init__(self, center_x, center_y, fractal_generator: FractalGenerator,
                 width, height, resolution=(800, 800)):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.fractal_generator = fractal_generator
        self.resolution = resolution
        self.res_x, self.res_y = self.resolution
        self.matrix = np.zeros((self.res_y, self.res_x), dtype=np.int16)
        self.calculation_queued = False
        self.calculation_queued_lock = threading.Lock()
        threading.Thread(target=self._continuous_calculate).start()

    def zoom(self, screen_x, screen_y, multiplier):
        self.center_x = (self.center_x + (
                screen_x - self.res_x / 2) * self.width / self.res_x / 2)
        self.center_y = (self.center_y + (
                screen_y - self.res_y / 2) * self.height / self.res_y / 2)
        self.width *= multiplier
        self.height *= multiplier

    def _continuous_calculate(self):
        while True:
            wait = True
            while wait:
                time.sleep(0.01)
                with self.calculation_queued_lock:
                    wait = not self.calculation_queued
                    self.calculation_queued = False
            self.calculate()

    def queue_calculate(self):
        with self.calculation_queued_lock:
            self.calculation_queued = True

    def calculate(self):
        start_time = time.time()
        for y in range(self.res_y):
            for x in range(self.res_x):
                plot_y = (self.center_y - self.height / 2 +
                          y * self.height / self.res_y)
                plot_x = (self.center_x - self.width / 2 +
                          x * self.width / self.res_x)
                self.matrix[y, x] = self.fractal_generator.calculate_point(
                    plot_x, plot_y)
        end_time = time.time()
        print(f'Calculation took: {end_time - start_time}s')

    def draw(self, screen):
        for y in range(self.res_y):
            for x in range(self.res_x):
                screen.set_at(
                    (x, y),
                    self.fractal_generator.color_from_iteration(
                        self.matrix[y, x])
                )
