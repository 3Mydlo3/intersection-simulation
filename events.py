from car import Car
import numpy as np

class CarArrival:
    def __init__(self, time_flow, stream):
        self.time_flow = time_flow
        self.stream = stream
        # Schedule Event - event_time
        self.schedule_arrival()

    def get_event_time(self):
        """Method returns event time"""
        return self.event_time

    def on_executed(self):
        """
        Method run when event is executed
        Moves assigned car to appropriate queue
        and schedules next car arrival event
        """
        self.car.move_to_queue()
        CarArrival(time_flow=self.time_flow, stream=self.stream)
        return True

    def schedule_arrival(self):
        """Schedules car arrival at the intersection"""
        # Schedule arrival
        self.event_time = self.time_flow.get_current_time() + np.random.randint(0, 10)
        # Create car and assign event
        self.car = Car(parent_object=self.stream)
        self.car.set_arrival_event(self)
        # Add event to timeflow
        self.time_flow.add_time_event(self)
