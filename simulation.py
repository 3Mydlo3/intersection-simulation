from time_flow import TimeFlow
from time_class import Time
from intersection import Intersection
from events import CarArrival, LightsPhase
import numpy as np

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

    def get_cars_awaiting(self):
        """Method returns all cars which are waiting in queues"""
        return self.intersection.get_awaiting_cars()

    def get_cars_created(self):
        """
        Method returns all cars created during simulation
        Does not include cars yet to arrive
        """
        return [car for car in self.intersection.get_all_cars() if car.has_arrived()]

    def get_cars_departed(self):
        """Method returns all cars which crossed the intersection"""
        return self.intersection.get_departed_cars()

    def get_cars_avg_time_in_system(self):
        departed_cars = self.get_cars_departed()
        if departed_cars == []:
            return Time()
        average_time_in_system = np.average(np.array([car.get_time_in_system().convert_to_seconds() for car in departed_cars]))
        average_time_in_system = Time(seconds=average_time_in_system)
        return average_time_in_system

    def get_expected_interval_times(self):
        """Method returns expected intervals times for all streams"""
        streams = self.intersection.get_streams()
        return [stream.get_expected_interval() for stream in streams]

    def print_stats(self):
        crossing_cars = self.intersection.get_crossing_cars()
        print(f"Expected arrival times  : {str(self.get_expected_interval_times())}")
        print(f"Number of cars created  : {len(self.get_cars_created())}")
        print(f"Number of cars departed : {len(self.get_cars_departed())}")
        print(f"Number of cars awaiting : {len(self.get_cars_awaiting())}")
        print(f"Average time in system  : {self.get_cars_avg_time_in_system().convert_to_text()}")

    def start_simulation(self):
        """
        Functions handles simualtion start
        Schedules first car for each stream.
        Starts first traffic lights cycle.
        """
        self.streams = self.intersection.get_streams()
        for _stream in self.streams:
            CarArrival(time_flow=self.time, stream=_stream)
        # Start traffic lights cycles
        LightsPhase(intersection=self.intersection, time_flow=self.time,
                    lights_remaining=[])
        # Turn on first light
        self.intersection.get_lights()[0].switch_lights(state=True)
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

