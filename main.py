from backend import backend
from gui import gui_main

import multiprocessing

if __name__ == "__main__":
    multiprocessing.freeze_support()
    p = multiprocessing.Process(target=backend)
    p.start()
    gui_main()
