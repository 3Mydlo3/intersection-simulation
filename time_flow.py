from time_class import Time

class TimeFlow:
    def __init__(self, start_time=(8,0,0), end_time=(9,0,0)):
        self.start_time = Time(*start_time)
        self.current_time = Time(*start_time)
        self.end_time = Time(*end_time)
        # Dictionary of all time events.
        # Key is hashed time (in seconds) and value is list of events.
        self.time_events = {}

    def advance_time(self):
        """Function advances simulation time"""
        next_event_time = self.get_next_event_time()
        self.current_time += next_event_time
        return self

    def check_end_condition(self, time_checked=None):
        """Function checks if time end condition is fulfilled"""
        if time_checked is None:
            time_checked = self.current_time
        if time_checked >= self.end_time:
            self.current_time = self.end_time
            return True
        else:
            return False
