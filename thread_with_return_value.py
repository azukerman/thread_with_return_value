from threading import Thread


class ThreadWithReturnValue(Thread):
    class CallBack:
        def __init__(self, target, *args, **kwargs):
            self.result = target(*args, **kwargs)

    def run(self):
        self.__return_value = None
        self.__return_value = self.CallBack(self._target, *self._args, **self._kwargs)

    @property
    def return_value(self):
        return self.__return_value.result
