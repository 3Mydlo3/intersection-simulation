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
