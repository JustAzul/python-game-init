import os
import subprocess
import psutil
from threading import Thread
from time import sleep
from utils import is_process_running, kill_process_name


class ProcessHackerHandler(Thread):
    def __init__(self):
        Thread.__init__(self)
        
        self.process = None
        self.process_name = r'ProcessHacker.exe'
        
        self.process_loc = r'C:\Program Files\Process Hacker 2\ProcessHacker.exe'
        self.process_args = r'-hide -elevate'
        
    def is_process_running(self):
        result = is_process_running(self.process_name)
        print(f'ProcessHackerHandler is_process_running: {result}')
        return result
    
    def kill(self):
        print('ProcessHackerHandler trying to kill process..')
        
        if self.is_process_running() == False:
            print('ProcessHackerHandler process is not running!')
            return
        
        if self.process != None:
            print('ProcessHackerHandler found internal pid, proceding..')
            parent_pid = self.process.pid
            parent = psutil.Process(parent_pid)
            
            for child in parent.children(recursive=True):
                child.kill()
                
            parent.kill()
        else:
            print('ProcessHackerHandler internal pid not found, trying to kill by process name')
            kill_process_name(self.process_name)
            
    def handle_kernel(self, new_state = r'stop'):
        print(f'ProcessHackerHandler handle_kernel: {new_state}')
        os.system('cmd /c sc ' + new_state + ' kprocesshacker3')
        
    def stop_process(self):
        if self.is_process_running() == True:
            self.kill()
            
        self.handle_kernel(r'stop')
        
    def start_process(self):        
        self.handle_kernel(r'start')
        
        print('ProcessHackerHandler waiting a second..')
        sleep(1)
        
        if self.is_process_running() == False:
            print('ProcessHackerHandler running process..')
            full_path = self.process_loc + ' ' + self.process_args
            self.process = subprocess.Popen(full_path)
        else:
            print('ProcessHackerHandler process hacker is already running, exiting..')
