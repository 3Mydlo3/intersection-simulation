from road import Road
from stream import Stream
from priority import Priority
from objectBase import ObjectBase
import numpy as np

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

    def get_awaiting_cars(self):
        """
        Method returns all cars that are
        currently in queues
        """
        awaiting_cars = []
        for _lane in self.get_incoming_lanes():
            awaiting_cars.extend(_lane.get_queue())
        return awaiting_cars

    def get_crossing_cars(self):
        """Method returns cars currently crossing the intersection"""
        crossing_cars = []
        for _stream in self.streams:
            crossing_cars.extend(_stream.get_cars_on_intersection())
        return crossing_cars

    def get_departed_cars(self):
        """Method returns cars which crossed the intersection"""
        departed_cars = [car for car in self.get_all_cars() if car.has_departed()]
        return departed_cars

    def get_all_cars(self):
        """
        Method returns all cars that are
        or were on the intersection
        """
        cars = []
        for _stream in self.get_streams():
            stream_cars = _stream.get_child_objects()
            cars.extend(stream_cars)
        return cars

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
                    expected_interval = np.random.uniform(low=5.0, high=10.0)
                    stream = Stream(id_=_i, parent_object=self.roads[_x].get_incoming_lane(),
                                    connected_with=self.roads[_y].get_outgoing_lane(),
                                    expected_interval=expected_interval)
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
            [[0, 1], [4], [2, 5]],
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
