

class BaseChannel():

    def execute_all(self, event):
        action_func = getattr(self, event.action)
        if not action_func:
            raise AttributeError(f'Channel {self.__class__.__name__} got an invalid action: "{event.action}"')

        # TODO - apply multi threading here
        for p in event.prospects:
            action_func(p)


class LinkedInChannel(BaseChannel):
    @staticmethod
    def connect(prospect):
        # TODO implement connect to linkedIn logic
        pass


class EmailChanel(BaseChannel):
    @staticmethod
    def cold_email(prospect):
        # TODO - implement mail sending
        pass


