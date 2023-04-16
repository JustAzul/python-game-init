from enum import Enum
from utils import find_pid_from_name
import win32api
import win32con
import win32process


class PriorityLevel(Enum):
    IDLE = "idle"
    BELOW_NORMAL = "below_normal"
    NORMAL = "normal"
    ABOVE_NORMAL = "above_normal"
    HIGH = "high"
    REALTIME = "realtime"


def set_priority(pid, priority: PriorityLevel):
    priority_map = {
        PriorityLevel.IDLE: win32process.IDLE_PRIORITY_CLASS,
        PriorityLevel.BELOW_NORMAL: win32process.BELOW_NORMAL_PRIORITY_CLASS,
        PriorityLevel.NORMAL: win32process.NORMAL_PRIORITY_CLASS,
        PriorityLevel.ABOVE_NORMAL: win32process.ABOVE_NORMAL_PRIORITY_CLASS,
        PriorityLevel.HIGH: win32process.HIGH_PRIORITY_CLASS,
        PriorityLevel.REALTIME: win32process.REALTIME_PRIORITY_CLASS,
    }

    if priority not in priority_map:
        raise ValueError(f"Invalid priority level: {priority}")

    handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
    win32process.SetPriorityClass(handle, priority_map[priority])


def set_process_priority_by_name(name, priority: PriorityLevel):
    pid = find_pid_from_name(name)
    set_priority(pid, priority)
