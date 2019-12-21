class Priority:
    def __init__(self, higher_priority=[], lower_priority=[], non_colliding=[]):
        self.higher_priority = higher_priority
        self.lower_priority = lower_priority
        self.non_colliding = non_colliding

    def get_higher_priority(self):
        return self.higher_priority

    def get_lower_priority(self):
        return self.lower_priority

    def get_non_colliding(self):
        return self.non_colliding
