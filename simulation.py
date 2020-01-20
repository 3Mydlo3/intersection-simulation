from time_flow import TimeFlow
from intersection import Intersection
from events import CarArrival

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

    def get_all_cars(self):
        """Method returns all cars from simulation"""
        return self.intersection.get_all_cars()

    def start_simulation(self):
        """
        Functions handles simualtion start
        Schedules first car for each stream.
        """
        self.streams = self.intersection.get_streams()
        for _stream in self.streams:
            CarArrival(time_flow=self.time, stream=_stream)
        self.run_simulation()

    def run_simulation(self):
        """Function handles simulation flow"""
        # Check end conditions
        while not self.check_end():
            # Try to advance time. If failed simulation ended
            success = self.time.advance_time()
            if not success:
                return False
            # Execute planned events
            self.time.execute_events()

