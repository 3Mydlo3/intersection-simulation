from objectBase import ObjectBase

class TrafficLights(ObjectBase):
    def __init__(self, id_=None, parent_object=None, green_duration=None):
        super().__init__(id_=id_, parent_object=parent_object)
        # Controls whether lights are working or not
        self.on = False
        # Current lights state
        self.green = False
        # How long green light should be on
        self.green_duration = green_duration

    def enable_lights(self, state=True):
        """Method enables or disables lights"""
        self.on = state

    def get_green_duration(self):
        """Method returns green light duration"""
        return self.green_duration

    def get_lights_state(self):
        """
        Method returns current lights state.
        Returns None if lights are disabled
        or True/False depending on green state
        """
        if not self.is_on():
            return None
        return True if self.is_green() else False

    def is_on(self):
        """Method returns true if lights are working"""
        return self.on

    def is_green(self):
        """Method returns true if lights are green"""
        return True if self.green else False

    def switch_lights(self, state=None):
        """
        Method switches current light to desired state
        or to opposite if desired is not given.
        If desired state is the same as current state, does nothing.
        Returns final lights state.
        """
        if state is None:
            state = not self.green
        self.green = state
        return state
