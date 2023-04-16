import os
import sys
import psutil
import win32com.shell.shell as shell

ASADMIN = 'asadmin'

def kill_process_name(process_name: str) -> None:
    """Kills a process by name."""
    for process in psutil.process_iter():
        try:
            if process.name().lower() not in process_name.lower():
                continue
            print(f'Killing script: {process_name}')
            process.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def is_process_running(exe_name: str) -> bool:
    """Checks if a process is running by name."""
    return any(exe_name.lower() in process.name().lower() for process in psutil.process_iter())

def is_game_running() -> bool:
    """Checks if the 'Fortnite' game is running."""
    return is_process_running('Fortnite')

def elevate():
    """Restarts the script with elevated privileges if not already running as administrator."""
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx('runas', sys.executable, params)
        sys.exit(0)
