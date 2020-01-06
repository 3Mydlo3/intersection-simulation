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
        if next_event_time is False:
            return False
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

    def get_next_event_time(self):
        """Function returns time of the next planned event"""
        next_events = []
        checked_time = Time(time_reference=self.current_time)
        while next_events == []:
            try:
                next_events = self.time_events[checked_time]
            except KeyError:
                checked_time += Time(seconds=1)
                if self.check_end_condition(checked_time):
                    return False
        return checked_time

    def get_current_events(self):
        """Function returns events planned for current time"""
        return self.time_events[self.current_time]
