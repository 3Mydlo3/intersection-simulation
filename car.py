from objectBase import ObjectBase

class Car(ObjectBase):
    """
        Car class.
        Parent object is stream to which car belongs,
        as it defines origin and destination
    """
    def __init__(self, id_=None, parent_object=None):
        super().__init__(id_=id_, parent_object=parent_object)
        # Arrival and departure events for later calculations
        self.arrival = None
        self.departing = None
        self.departed = None

    def get_stream(self):
        """Method returns car's stream"""
        return self.parent_object

    def has_arrived(self):
        return self.arrival.is_executed()

    def has_departed(self):
        if self.departed is None:
            return False
        return self.departed.is_executed()

    def is_awaiting(self):
        return self.has_arrived() and not self.has_departed() and not self.is_departing()

    def is_departing(self):
        if self.departing is None:
            return False
        return self.is_departing()

    def is_first_in_queue(self):
        """Method checks if car is first in queue"""
        if self is self.parent_object.get_queue_first_car():
            return True
        else:
            return False

    def move_to_intersection(self):
        """
        Method moves car onto the intersection
        so the car can drive through it
        """
        self.parent_object.move_car_to_intersection(self)

    def remove_from_intersection(self):
        """
        Method removes car from the intersection
        simulating driving through it
        """
        self.parent_object.remove_car_from_intersection(self)

    def move_to_queue(self):
        self.parent_object.add_to_queue(self)

    def set_arrival_event(self, event):
        """Method sets arrival event"""
        self.arrival = event

    def set_departing_event(self, event):
        """Method sets departing event"""
        self.departing = event

    def set_departure_event(self, event):
        """Method sets departure event"""
        self.departed = event
