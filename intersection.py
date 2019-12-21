from road import Road
from objectBase import ObjectBase

class Intersection(ObjectBase):
    def __init__(self):
        super().__init__(parent_object=None)
        self.roads = [
            Road(id_=0, parent_object=self),
            Road(id_=1, parent_object=self),
            Road(id_=2, parent_object=self)
        ]
        self.incoming_lanes = self.get_incoming_lanes()
        self.outgoing_lanes = self.get_outgoing_lanes()

    def get_incoming_lanes(self):
        incoming_lanes = []
        for road in self.roads:
            incoming_lanes.append(road.get_incoming_lane())
        return incoming_lanes

    def get_outgoing_lanes(self):
        outgoing_lanes = []
        for road in self.roads:
            outgoing_lanes.append(road.get_outgoing_lane())
        return outgoing_lanes
