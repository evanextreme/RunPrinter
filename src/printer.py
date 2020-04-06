import time

from .threads import PrinterThread


class Printer:
    def __init__(self, sleeptime=2):
        self.sleeptime = sleeptime
        self.sleepthread = None
        self.starttext = None
        self.endtext = None

    def start(self, starttext="Running", endtext="done"):
        self.starttext = starttext
        self.endtext = endtext
        self.sleepthread = PrinterThread(
            printtime=self.sleeptime, starttext=starttext)
        self.sleepthread.start()

    def stop(self):
        self.sleepthread.stop()
        self.sleepthread.join()
        while self.sleepthread.isAlive():
            time.sleep(0.5)
        print(self.endtext)

    def restart(self, starttext="Running", endtext="done"):
        self.stop()
        self.start(starttext=starttext)
