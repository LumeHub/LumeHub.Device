import logging
import threading
from ctypes import pythonapi, py_object


class ThreadedTask(threading.Thread):
    def __init__(self, target):
        super(ThreadedTask, self).__init__()
        self.target = target

    def run(self):
        self.target()

    def get_id(self):
        """:return: id of the respective thread"""
        if hasattr(self, '_thread_id'):
            return self._thread_id
        # noinspection PyProtectedMember
        for thread_id, thread in threading._active.items():
            if thread is self:
                return thread_id

    def kill(self):
        thread_id = self.get_id()
        res = pythonapi.PyThreadState_SetAsyncExc(thread_id, py_object(SystemExit))
        if res > 1:
            pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            logging.exception('Exception raise failure')
