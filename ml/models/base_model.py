class BaseModel(object):
    def __init__(self, *kwargs):
        raise NotImplementedError

    def __call__(self, **kwargs):
        raise NotImplementedError
