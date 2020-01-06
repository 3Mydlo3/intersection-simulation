from time_flow import TimeFlow
from intersection import Intersection

class Simulation:
    def __init__(self):
        self.time = TimeFlow()
        self.intersection = Intersection()

    def check_end(self):
        """Function checks if simulation end conditions are fulfilled"""
        if self.time.check_end_condition():
            return True
        return False

    def run_simulation(self):
        while not self.check_end():
            success = self.time.advance_time()
            if not success:
                return False

