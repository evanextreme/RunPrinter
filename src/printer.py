import time
from .threads import PrinterThread


class Printer:
    def __init__(self, delay=2):
        self.sleepthread = None
        self.delay = delay
        self.finished_message = None
        self.last_continuous = False
        self.kwargs = {}

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.last_continuous:
            self.stop()

    def print(self, *args, continuous=False,
              finished_message="done", **kwargs):
        self.kwargs = kwargs
        self.last_continuous = continuous
        if self.sleepthread:
            self.stop()

        if continuous:
            self.finished_message = finished_message
            self.kwargs['end'] = ''

        print(*args, **self.kwargs)

        if continuous:
            self.sleepthread = PrinterThread(
                printtime=self.delay)
            self.sleepthread.start()

    def stop(self):
        self.sleepthread.stop()
        self.sleepthread.join()
        self.sleepthread = None
        self.kwargs = {}
        while self.sleepthread.isAlive():
            time.sleep(0.5)
        print(self.finished, **self.kwargs)
