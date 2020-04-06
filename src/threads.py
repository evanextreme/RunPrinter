import threading
import time


class PrinterThread(threading.Thread):
    def __init__(self, starttext, printtime=2, inctime=0.5):
        threading.Thread.__init__(self)
        self.printing = True
        self.starttext = starttext
        self.printtime = printtime
        self.acctime = 0
        self.inctime = inctime

    def run(self):
        print("{}...".format(self.starttext), end="")
        while self.printing:
            self.acctime += self.inctime
            time.sleep(self.inctime)
            if self.acctime % self.printtime == 0:
                print(".", end="")

    def stop(self):
        self.printing = False
