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
        self.departed = None

    def get_stream(self):
        """Method returns car's stream"""
        return self.parent_object

    def is_first_in_queue(self):
        """Method checks if car is first in queue"""
        if self is self.parent_object.get_queue_first_car():
            return True
        else:
            return False

    def move_to_queue(self):
        self.parent_object.add_to_queue(self)

    def set_arrival_event(self, event):
        """Method sets arrival event"""
        self.arrival = event

    def set_departure_event(self, event):
        """Method sets departure event"""
        self.departed = event
