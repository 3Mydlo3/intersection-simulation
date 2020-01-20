from time_class import Time

class TimeFlow:
    def __init__(self, start_time=(8,0,0), end_time=(9,0,0)):
        self.start_time = Time(*start_time)
        self.current_time = Time(*start_time)
        self.end_time = Time(*end_time)
        # Dictionary of all time events.
        # Key is hashed time (in seconds) and value is list of events.
        self.time_events = {}
        self.conditional_events = []

    def add_time_event(self, event):
        """Method adds time event to events list"""
        event_time = event.get_event_time()
        try:
            self.time_events[event_time].append(event)
        except KeyError:
            self.time_events[event_time] = [event]

    def add_conditional_event(self, event):
        """Method adds conditional event to events list"""
        self.conditional_events.append(event)

    def advance_time(self):
        """Function advances simulation time"""
        next_event_time = self.get_next_event_time()
        if next_event_time is False:
            return False
        self.current_time = next_event_time
        return self

    def check_end_condition(self, time_checked=None):
        """Function checks if time end condition is fulfilled"""
        if time_checked is None:
            time_checked = self.current_time
        if time_checked >= self.end_time:
            # Checked time is out of time horizon, set current time as end time
            self.current_time = self.end_time
            return True
        else:
            return False

    def execute_events(self):
        """Function executes current time events"""
        current_events = self.get_current_events()
        for event in current_events:
            event.execute()
        conditional_events = self.get_conditional_events()
        # Check if all cars should give way to another
        if [0, 3, 4] == sorted([event.get_stream_id() for event in conditional_events]):
            conditional_events[0].execute(forced=True)
        else:
            for event in conditional_events:
                event.execute()

    def get_current_time(self):
        """Function returns current time"""
        return self.current_time

    def get_next_event_time(self):
        """Function returns time of the next planned event"""
        next_events = []
        checked_time = Time(time_reference=self.current_time) + 1
        while next_events == []:
            try:
                # Get planned events for given time
                next_events = self.time_events[checked_time]
            except KeyError:
                # There were no events so we need to increase time
                # and check end conditions
                checked_time += 1
                if self.check_end_condition(checked_time):
                    return False
        return checked_time

    def get_conditional_events(self):
        """Method returns conditional events list"""
        return self.conditional_events

    def get_current_events(self):
        """Function returns events planned for current time"""
        return self.time_events[self.current_time]

    def remove_conditional_event(self, event):
        """Method removes conditional event from events list"""
        self.conditional_events.remove(event)
