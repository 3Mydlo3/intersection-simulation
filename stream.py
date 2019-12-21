from objectBase import ObjectBase
from priority import Priority

class Stream(ObjectBase):
    def __init__(self, id_=None, parent_object=None, connected_with=None):
        super().__init__(id_=id_, parent_object=parent_object)
        self.connected_with = connected_with
        self.priority = None

    def assign_priority(self, priority):
        self.priority = priority

