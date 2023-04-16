import os
import sys
import psutil
import win32com.shell.shell as shell

ASADMIN = 'asadmin'

def kill_process_name(process_name):
    for process in psutil.process_iter():
        try:
            if process.name().lower() not in process_name.lower():
                continue
            else:
                print('Killing script: ' + process_name)
                process.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def is_process_running(exe_name):
    for process in psutil.process_iter():
        try:
            if exe_name.lower() not in process.name().lower():
                continue
            else:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def is_game_running():
    target_name =  r'Fortnite'

    for process in psutil.process_iter():
        try:
            if target_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

def elevate():
    if sys.argv[-1] != ASADMIN:
            script = os.path.abspath(sys.argv[0])
            params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
            shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
            sys.exit(0)