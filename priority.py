import win32api
import win32process
import win32con

def set_priority(pid, priority):
    priority_map = {
        "idle": win32process.IDLE_PRIORITY_CLASS,
        "below_normal": win32process.BELOW_NORMAL_PRIORITY_CLASS,
        "normal": win32process.NORMAL_PRIORITY_CLASS,
        "above_normal": win32process.ABOVE_NORMAL_PRIORITY_CLASS,
        "high": win32process.HIGH_PRIORITY_CLASS,
        "realtime": win32process.REALTIME_PRIORITY_CLASS,
    }
    
    if priority not in priority_map:
        raise ValueError(f"Invalid priority level: {priority}")
    
    handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
    win32process.SetPriorityClass(handle, priority_map[priority])
