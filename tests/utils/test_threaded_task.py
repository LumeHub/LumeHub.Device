import time
import unittest

from src.utils import ThreadedTask


def sample_task(is_running_flag):
    # Placeholder for a sample task
    try:
        is_running_flag.append(True)
        time.sleep(2)
    finally:
        is_running_flag.pop()


class TestThreadedTask(unittest.TestCase):
    def test_thread_running(self):
        is_running_flag = []
        thread = ThreadedTask(lambda: sample_task(is_running_flag))
        thread.start()
        thread.join(timeout=3)
        self.assertFalse(len(is_running_flag))

    def test_thread_still_running(self):
        is_running_flag = []
        thread = ThreadedTask(lambda: sample_task(is_running_flag))
        thread.start()
        thread.join(timeout=1)
        self.assertTrue(len(is_running_flag))

    def test_thread_killing(self):
        is_running_flag = []
        thread = ThreadedTask(lambda: sample_task(is_running_flag))
        thread.start()
        self.assertTrue(is_running_flag)
        thread.kill()
        thread.join(timeout=1)
        self.assertTrue(len(is_running_flag))


if __name__ == '__main__':
    unittest.main()
