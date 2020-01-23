from car import Car
import numpy as np

class CarArrival:
    def __init__(self, time_flow, stream):
        self.time_flow = time_flow
        self.stream = stream
        # Schedule Event - event_time
        self.schedule_arrival()
        self.executed = False

    def get_event_time(self):
        """Method returns event time"""
        return self.event_time

    def execute(self, forced=False):
        """Method executes event"""
        self.executed = True
        return self.on_executed()

    def is_executed(self):
        return self.executed

    def on_executed(self):
        """
        Method run when event is executed
        Moves assigned car to appropriate queue
        and schedules next car arrival event
        """
        # Move car to queue and assign conditional departure event
        self.car.move_to_queue()
        if self.car.is_first_in_queue():
            CarDeparture(time_flow=self.time_flow, car=self.car)
        # Schedule next car arrival for given stream
        CarArrival(time_flow=self.time_flow, stream=self.stream)
        return True

    def schedule_arrival(self):
        """Schedules car arrival at the intersection"""
        # Schedule arrival
        self.event_time = self.time_flow.get_current_time() + int(np.random.exponential(self.stream.get_expected_interval()))
        # Create car and assign event
        self.car = Car(parent_object=self.stream)
        self.car.set_arrival_event(self)
        # Add event to timeflow
        self.time_flow.add_time_event(self)


class CarDeparture:
    def __init__(self, time_flow, car):
        if car is None:
            return None
        self.time_flow = time_flow
        self.car = car
        self.stream = car.get_stream()
        self.queue = self.stream.get_queue()
        self.lights = self.queue.get_lights()
        self.priority = self.stream.get_priority()
        self.time_flow.add_conditional_event(self)
        # Assign departing event
        self.car.set_departing_event(self)
        # Event start time
        self.event_time = self.time_flow.get_current_time()
        self.executed = False

    def execute(self, forced=False):
        """Method executes event"""
        if not self.pre_executed() and not forced:
            return False
        self.executed = True
        return self.on_executed()

    def get_stream_id(self):
        """Method returns assigned stream id"""
        return self.stream.get_id()

    def is_executed(self):
        return self.executed

    def pre_executed(self):
        """
        Method run before on_executed.
        Checks if event conditions are fulfilled.
        Returns true when no higher priority stream awaits departure
        or when lights are green (when enabled)
        """
        # Check if lights are enabled and green
        if self.lights.is_on():
                return True if self.lights.is_green() else False
        else:
            # Check if any higher priority stream is used or awaits departure
            higher_priority_streams = self.priority.get_higher_priority()
            for _stream in higher_priority_streams:
                if _stream.is_used() or _stream.is_queue_first_car():
                    return False
            return True if self.car == self.queue.get_first_car() else False

    def on_executed(self):
        """
        Method run when event is executed
        Moves assigned car to intersection,
        schedules CarDeparted time event
        and adds conditional event for next car
        """
        self.queue.remove_first_car().move_to_intersection()
        CarDeparted(self.time_flow, self.car)
        self.time_flow.remove_conditional_event(self)
        # Add conditional event for next car in queue
        CarDeparture(time_flow=self.time_flow, car=self.queue.get_first_car())
        return True


class CarDeparted:
    def __init__(self, time_flow, car):
        self.time_flow = time_flow
        self.car = car
        self.stream = car.get_stream()
        self.schedule_departed()
        self.executed = False

    def execute(self, forced=False):
        """Method executes event"""
        self.executed = True
        return self.on_executed()

    def get_event_time(self):
        """Method returns event time"""
        return self.event_time

    def is_executed(self):
        return self.executed

    def on_executed(self):
        """
        Method run when event is eecuted
        Removes car from intersection
        """
        self.car.remove_from_intersection()
        self.car.calculate_time_in_system()

    def schedule_departed(self):
        """Method schedules car's departure time"""
        # Schedule departure
        self.event_time = self.time_flow.get_current_time() + np.random.randint(3, 5)
        # Assign departure event
        self.car.set_departure_event(self)
        # Add event to timeflow
        self.time_flow.add_time_event(self)

class LightsPhase:
    def __init__(self, intersection, time_flow, lights_remaining):
        self.intersection = intersection
        # Check if we are through all lights
        self.lights_remaining = lights_remaining
        # Get first light from the list
        try:
            self.light = self.lights_remaining.pop(0)
        except IndexError:
            self.lights_remaining = self.intersection.get_lights().copy()
            self.light = self.lights_remaining.pop(0)
        # Usual events stuff
        self.time_flow = time_flow
        self.schedule_event()
        self.time_flow.add_time_event(self)
        self.executed = False

    def execute(self, forced=False):
        """Method executes event"""
        self.executed = True
        return self.on_executed()

    def get_event_time(self):
        """Method returns event time"""
        return self.time

    def is_executed(self):
        return self.executed

    def on_executed(self):
        """
        Method run when event is executed
        Changes light to red and schedules
        light change to green for next traffic lights.
        """
        # Change light to red
        self.light.switch_lights(state=False)
        # Schedule new green light
        LightsSwitch(intersection=self.intersection, time_flow=self.time_flow,
                    lights_remaining=self.lights_remaining)

    def schedule_event(self):
        """Method schedules light change events"""
        self.time = self.intersection.get_current_time() + self.light.get_green_duration()

class LightsSwitch:
    def __init__(self, intersection, time_flow, lights_remaining):
        self.intersection = intersection
        self.time_flow = time_flow
        self.lights_remaining = lights_remaining
        try:
            self.light = self.lights_remaining[0]
        except IndexError:
            self.lights_remaining = self.intersection.get_lights().copy()
            self.light = self.lights_remaining[0]
        self.schedule_event()
        self.time_flow.add_time_event(self)
        self.executed = False

    def execute(self, forced=False):
        """Method executes event"""
        self.executed = True
        return self.on_executed()

    def get_event_time(self):
        """Method returns event time"""
        return self.time

    def is_executed(self):
        return self.executed

    def on_executed(self):
        """
        Method run when event is executed
        Changes light to red and schedules
        light change to green for next traffic lights
        after 5 seconds.
        """
        # Change light to green
        self.light.switch_lights(state=True)
        # Schedule next lights phase
        LightsPhase(intersection=self.intersection, time_flow=self.time_flow,
                    lights_remaining=self.lights_remaining)

    def schedule_event(self):
        """Method schedules light change events"""
        self.time = self.intersection.get_current_time() + 5
