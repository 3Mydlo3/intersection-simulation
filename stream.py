from objectBase import ObjectBase
from priority import Priority

class Stream(ObjectBase):
    def __init__(self, id_=None, parent_object=None, connected_with=None):
        super().__init__(id_=id_, parent_object=parent_object)
        self.connected_with = connected_with
        # List of cars from this stream currently driving through the intersection
        self.on_intersection = []
        self.priority = None

    def add_to_queue(self, car):
        self.parent_object.add_to_queue(car)

    def assign_priority(self, priority):
        self.priority = priority

    def get_id(self):
        return self.id

    def get_priority(self):
        return self.priority

    def get_queue_first_car(self):
        """Returns first car in queue for given stream's queue"""
        return self.parent_object.get_first_car()

    def is_queue_first_car(self):
        """
        Each queue handles two streams.
        Method checks if first car in queue belongs to this stream.
        """
        first_car = self.parent_object.get_first_car()
        if first_car is None:
            return False
        if first_car.get_stream() == self:
            return True
        else:
            return False

    def move_car_to_intersection(self, car):
        """
        Method moves given car onto the intersection
        so the car can drive through it
        """
        self.on_intersection.append(car)

    def remove_car_from_intersection(self, car):
        """
        Method removes given car from the intersection
        simulating driving through it
        """
        self.on_intersection.remove(car)
