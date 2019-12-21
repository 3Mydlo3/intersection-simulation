from lane import Lane
from objectBase import ObjectBase

class Road(ObjectBase):
    def __init__(self, id_=None, parent_object=None, incoming_lanes_number=1,
                    outgoing_lanes_number=1):
        super().__init__(id_=id_, parent_object=parent_object)
        # Initialize lanes
        self.incoming_lane = Lane(id_=0, parent_object=self, outgoing=False)
        self.outgoing_lane = Lane(id_=1, parent_object=self, outgoing=True)

    def get_incoming_lane(self):
        return self.incoming_lane

    def get_outgoing_lane(self):
        return self.outgoing_lane
