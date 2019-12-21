from road import Road
from stream import Stream
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
        return streams
