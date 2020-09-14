# Complex Version

# Purpose of this tool:
# Transform APT History Logs, Widnows DNS-Logs or other multiline logs into handy one-liners

import sys
import os
from queue import Queue
import threading


class LogReader(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        # Not implemented, yet
        pass

    def stop(self):
        self.stop()


class LogFilter(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        # Not implemented, yet
        pass

    def stop(self):
        self.stop()


class LogWriter(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        # Not implemented, yet
        pass

    def stop(self):
        self.stop()


class LogTail():

    reader: LogReader = LogReader()
    filter_queue: Queue = Queue()
    filter: LogFilter = LogFilter()
    writer_queue: Queue = Queue()
    writer: LogWriter = LogWriter()

    def __init__(self):
        self.writer.start()
        self.filter.start()
        self.reader.start()
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.writer.stop()
        self.filter.stop()
        self.reader.stop()


lt = LogTail()

exit()
