class TaskException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class BadInputException(TaskException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class LogicException(TaskException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AssertException(TaskException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
