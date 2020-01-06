from objectBase import ObjectBase

class Lane(ObjectBase):
    def __init__(self, id_=None, parent_object=None, outgoing=False):
        super().__init__(id_=id_, parent_object=parent_object)
        self.outgoing = outgoing
        self.queue = []

    def is_incoming(self):
        return (False if self.outgoing else True)

    def add_to_queue(self, object_):
        """Method adds object (car) to queue"""
        self.queue.append(object_)

    def get_first_car(self):
        """Method returns first car from queue or None if not availabe."""
        try:
            car = self.queue[0]
            return car
        except IndexError:
            return None

    def remove_first_car(self):
        """Method removes and returns first car from queue or None if not available."""
        try:
            car = self.queue.pop(0)
            return car
        except IndexError:
            return None
