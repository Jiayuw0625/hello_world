from cacheTypes import SchedulerProtocol
from threading import Timer
from typing import Callable


class Scheduler(SchedulerProtocol):
    """Concrete scheduler implementation using threading.Timer"""

    """Schedules a function to be run one time after a dely.  Returns a cancellation function that prevents fn from being run."""
    def runOnceAfter(self, duration_in_seconds: float, fn: Callable[[], None]) -> Callable[[], None]:
        timer = Timer(duration_in_seconds, fn)
        timer.start()
        return timer.cancel
