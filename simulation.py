from time_flow import TimeFlow
from intersection import Intersection
from car import Car

class Simulation:
    def __init__(self):
        self.time = TimeFlow()
        self.intersection = Intersection()
        self.start_simulation()

    def check_end(self):
        """Function checks if simulation end conditions are fulfilled"""
        if self.time.check_end_condition():
            return True
        return False

    def start_simulation(self):
        """
        Functions handles simualtion start
        Schedules first car for each stream.
        """
        self.run_simulation()

    def run_simulation(self):
        """Function handles simulation flow"""
        # Check end conditions
        while not self.check_end():
            # Try to advance time. If failed simulation ended
            success = self.time.advance_time()
            if not success:
                return False

