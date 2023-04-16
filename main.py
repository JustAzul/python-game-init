from p_hacker_handler import ProcessHackerHandler
from priority import set_process_priority_by_name
from time import sleep
from utils import elevate, is_process_running

import sys

def main(game_name: str) -> None:
    elevate()
    print('Starting..')

    if is_process_running(game_name):
        print('Game is already running!')
        set_process_priority_by_name(game_name)
        print('Exiting..')
        return

    process_hacker = ProcessHackerHandler()
    process_hacker.stop_process_if_running()

    while not is_process_running(game_name):
        sleep(1)

    set_process_priority_by_name(game_name)

    while is_process_running(game_name):
        sleep(1)

    process_hacker.start_process()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        error_message = "Usage: python main.py <game_name>"
        sys.exit(1)

    game_name = str(sys.argv[1])
    main(game_name)
