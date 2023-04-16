from utils import elevate, is_game_running
from time import sleep
from subprocess import check_output
from priority import set_high_priority
from p_hacker_handler import p_hacker_handler

def get_pid(name):
    return check_output(["pidof",name])

def get_game_pid():
    return get_pid(r'FortniteClient-Win64-Shipping.exe')

# not sure if this is working..
def set_game_process_priority():
    print('Trying to change game process priority')
    
    game_pid = 0
    
    try:
        game_pid = get_game_pid()
    except Exception:
        print('Failed to get game pid.')
        return
    
    try:
        set_high_priority(game_pid)
    except Exception:
        print('Cannot change game priority, failed to find game pid.')
    
    return

def main():
    print('Starting..')
    
    if is_game_running() == True:
        print('Game is already running!')
        set_game_process_priority()
        print('exiting..')
        return
    
    process_hacker = p_hacker_handler()
    
    if process_hacker.is_process_running() == True:
        print('Stoping process hacker..')
        process_hacker.stop_process()
    else:
        print('Process hacker is not running, proceding..')
    
    print('Waiting 10 seconds..')
    sleep(10)
    
    if is_game_running() == True:
        print('Game is running, waiting for it to close..')
        set_game_process_priority()
    
    sleep(1)
    
    while is_game_running() == True:
        sleep(1)
    
    print('Game is not running, exiting..')
    process_hacker.start_process()
    return
    
if __name__ == '__main__':
    elevate()
    main()
