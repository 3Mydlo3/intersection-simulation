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
        self.initialize_streams()

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

    def get_stream_by_id(self, _id):
        """Method returns stream by it's ID"""
        for _stream in self.streams:
            if _stream.get_id() == _id:
                return _stream

    def get_streams(self):
        return self.streams

    def initialize_streams(self):
        """Create streams and initialize their priorities"""
        self.streams = []
        # Create streams
        _i = 0
        for _x in range (0, 3):
            for _y in range (0, 3):
                if (_x != _y):
                    stream = Stream(id_=_i, parent_object=self.roads[_x].get_incoming_lane(),
                                    connected_with=self.roads[_y].get_outgoing_lane())
                    self.streams.append(stream)
                    _i += 1
        # Initialize stream priorities
        # First column are higher priority streams
        # Second column are lower priority streams
        # And third are non colliding streams
        priorities_matrix = [
            [[4, 5], [3], [1, 2]],
            [[], [3], [0, 2, 4, 5]],
            [[], [4], [0, 1, 3, 5]],
            [[0, 1, 4], [], [2, 5]],
            [[2, 3], [0], [1, 5]],
            [[], [0], [1, 2, 3, 4]]
        ]
        for _i in range (0, 6):
            # Get prioritized streams by id for given stream
            _priorities = [[], [], []]
            for _j in range (0, 3):
                for _streamID in priorities_matrix[_i][_j]:
                    _priorities[_j].append(self.get_stream_by_id(_streamID))
            # Create priority class and assign to given stream
            priority = Priority(higher_priority=_priorities[0], lower_priority=_priorities[1], non_colliding=_priorities[2])
            self.streams[_i].assign_priority(priority)
