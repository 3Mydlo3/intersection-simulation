from objectBase import ObjectBase

class Lane(ObjectBase):
    def __init__(self, id_=None, parent_object=None, outgoing=False):
        super().__init__(id_=id_, parent_object=parent_object)
        self.outgoing = outgoing
        self.queue = []

    def is_incoming(self):
        return (False if self.outgoing else True)

    def add_to_queue(self, object_):
        self.queue.append(object_)
