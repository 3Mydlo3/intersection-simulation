from math import floor

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0, time_reference=None):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        # If time reference was given, adjust
        if time_reference is not None:
            self.hours += time_reference.hours
            self.minutes += time_reference.minutes
            self.seconds += time_reference.seconds
            self.update_time()

    def __eq__(self, other):
        """For == comparison support"""
        if isinstance(other, Time):
            return True if self.convert_to_seconds() == other.convert_to_seconds() else False
        else:
            return NotImplemented

    def __gt__(self, other):
        """For > comparison support"""
        if isinstance(other, Time):
            return True if self.convert_to_seconds() > other.convert_to_seconds() else False
        else:
            return NotImplemented

    def __lt__(self, other):
        """For < comparison support"""
        if isinstance(other, Time):
            return True if self.convert_to_seconds() < other.convert_to_seconds() else False
        else:
            return NotImplemented

    def __ge__(self, other):
        """For >= comparison support"""
        if isinstance(other, Time):
            return True if self.convert_to_seconds() >= other.convert_to_seconds() else False
        else:
            return NotImplemented

    def __le__(self, other):
        """For <= comparison support"""
        if isinstance(other, Time):
            return True if self.convert_to_seconds() <= other.convert_to_seconds() else False
        else:
            return NotImplemented

    def __add__(self, other):
        """For + operation support"""
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            self.seconds += other.seconds
            self.update_time()
            return Time(time_reference=self)
        else:
            return NotImplemented

    def __iadd__(self, other):
        """For += operation support"""
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            self.seconds += other.seconds
            self.update_time()
        else:
            return NotImplemented

    def update_time(self):
        """Function updates time to keep minutes and seconds under 60"""
        new_minutes = floor(self.seconds/60)
        self.seconds -= new_minutes * 60
        self.minutes += new_minutes
        new_hours = floor(self.minutes/60)
        self.minutes -= new_hours * 60
        self.hours += new_hours
        return self

    def convert_to_seconds(self, time=None):
        """Converts given time to seconds"""
        if time is None:
            time = self
        return time.hours * 3600 + time.minutes * 60 + time.seconds

    def convert_to_time(self, seconds):
        """Converts given seconds to time"""
        hours = floor(seconds/3600)
        minutes = floor((seconds - hours * 3600)/60)
        seconds -= (hours * 3600 + minutes * 60)
        return Time(hours, minutes, seconds)
