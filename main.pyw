from p_hacker_handler import ProcessHackerHandler
from priority import set_process_priority_by_name, PriorityLevel
from time import sleep
from tkinter import messagebox
from utils import elevate, is_process_running
import tkinter as tk

import sys

def show_error_message(message):
    """Displays an error message popup."""
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)
    sys.exit(1)

def main(game_name: str) -> None:
    elevate()
    print('Starting..')

    if is_process_running(game_name):
        print('Game is already running!')
        set_process_priority_by_name(game_name, PriorityLevel.HIGH)
        print('Exiting..')
        return

    process_hacker = ProcessHackerHandler()
    process_hacker.stop_process_if_running()

    while not is_process_running(game_name):
        sleep(1)

    set_process_priority_by_name(game_name, PriorityLevel.HIGH)

    while is_process_running(game_name):
        sleep(1)

    process_hacker.start_process()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        error_message = "Arguments are not valid."
        print(error_message)
        show_error_message(error_message)
        sys.exit(1)

    game_name = str(sys.argv[1])
    main(game_name)
