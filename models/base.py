class Base:
    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
