# "Interface" for wrapperklassene til forskjellige sensorer

class Sensob:

    def __init__(self):
        pass

    def update(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError
