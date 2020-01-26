from objectBase import ObjectBase
from priority import Priority

class Stream(ObjectBase):
    def __init__(self, expected_interval, departure_time,
            id_=None, parent_object=None):
        super().__init__(id_=id_, parent_object=parent_object)
        self.expected_interval = expected_interval
        self.departure_time = departure_time
        # List of cars from this stream currently driving through the intersection
        self.on_intersection = []
        self.priority = None

    def add_to_queue(self, car):
        self.parent_object.add_to_queue(car)

    def assign_priority(self, priority):
        self.priority = priority

    def get_cars_on_intersection(self):
        return self.on_intersection

    def get_departure_time(self):
        return self.departure_time

    def get_expected_interval(self):
        return self.expected_interval

    def get_id(self):
        return self.id

    def get_priority(self):
        return self.priority

    def get_queue(self):
        return self.parent_object

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

    def is_used(self):
        """
        Method checks if any car from given stream
        is driving through the intersection at the moment
        """
        return True if self.on_intersection != [] else False

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
