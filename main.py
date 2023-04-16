import sys
import threading
from utils import elevate, is_process_running, display_error_popup
from time import sleep
from priority import set_high_priority
from p_hacker_handler import PHackerHandler

def main(game_exe_name, game_name):
    elevate()
    print('Starting..')

    if is_process_running(game_name):
        print('Game is already running!')
        set_high_priority(game_exe_name)
        print('Exiting..')
        return

    process_hacker = PHackerHandler()
    process_hacker.stop_process_if_running()
    sleep(10)

    while not is_process_running(game_exe_name):
        sleep(1)

    set_high_priority(game_exe_name)

    def exit_callback():
        process_hacker.start_process()
        sys.exit(0)

    tray_thread = threading.Thread(target=create_tray_icon, args=(exit_callback,))
    tray_thread.start()

    while is_process_running(game_exe_name):
        sleep(1)

    process_hacker.start_process()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        error_message = "Usage: python main.py <game_exe_name> <game_name>"
        display_error_popup(error_message)
        sys.exit(1)

    game_exe_name = sys.argv[1]
    game_name = sys.argv[2]

    main(game_exe_name, game_name)
