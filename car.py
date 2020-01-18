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

    def move_to_queue(self):
        self.parent_object.add_to_queue(self)

    def set_arrival_event(self, event):
        """Method sets arrival event"""
        self.arrival = event

    def set_departure_event(self, event):
        """Method sets departure event"""
        self.departed = event
