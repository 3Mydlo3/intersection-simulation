class ObjectBase:
    def __init__(self, id_=None, parent_object=None):
        self.id = id_
        # Parent object initialization
        self.parent_object = parent_object
        if self.parent_object is not None:
            self.parent_object.assign_child_object(self)
        # Child objects initialization
        self.child_objects = []

    def assign_child_object(self, child_object):
        self.child_objects.append(child_object)

    def assing_parent_object(self, parent_object):
        self.parent_object = parent_object

    def get_child_objects(self):
        return self.child_objects

    def get_parent_object(self):
        return self.parent_object
