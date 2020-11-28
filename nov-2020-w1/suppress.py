from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *args) -> None:
        self.e = tuple(args)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_traceback):
        self.exception = exc_val
        self.traceback = exc_traceback
        if exc_type is None:
            return True
        elif exc_type in self.e or issubclass(exc_type, self.e):
            return True
