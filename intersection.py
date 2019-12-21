from road import Road
from stream import Stream
from priority import Priority
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
        self.streams = self.initialize_streams()

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

    def get_streams(self):
        return self.streams

    def initialize_streams(self):
        """Create streams and initialize their priorities"""
        streams = []
        # Create streams
        _i = 0
        for _x in range (0, 3):
            for _y in range (0, 3):
                if (_x != _y):
                    stream = Stream(id_=_i, parent_object=self.roads[_x].get_incoming_lane(),
                                    connected_with=self.roads[_y].get_outgoing_lane())
                    streams.append(stream)
                    _i += 1
        # Initialize stream priorities
        priorities = [
            Priority(higher_priority=[4, 5], lower_priority=[3], non_colliding=[1, 2]),
            Priority(higher_priority=[], lower_priority=[3], non_colliding=[0, 2, 4, 5]),
            Priority(higher_priority=[], lower_priority=[4], non_colliding=[0, 1, 3, 5]),
            Priority(higher_priority=[0, 1, 4], lower_priority=[], non_colliding=[2, 5]),
            Priority(higher_priority=[2, 3], lower_priority=[0], non_colliding=[1, 5]),
            Priority(higher_priority=[], lower_priority=[0], non_colliding=[1, 2, 3, 4])
        ]
        for _i in range (0, 6):
            streams[_i].assign_priority(priorities[_i])
        return streams
