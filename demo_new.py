#!/usr/bin/env python2.7
from progressbar import ProgressBar
import time

def main():
    progress = ProgressBar(10, 0.5, '#')

    progress.set_bar_color('G')
    progress.set_perc_color('C')
    progress.set_msg_color('K')

    progress.draw("Starting...")
    time.sleep(1)       # Pretend like this is actually doing something.
    progress.add_progress("Executing...")
    time.sleep(1)
    progress.add_progress()
    time.sleep(1)
    progress.add_progress()
    time.sleep(1)
    progress.add_progress()
    time.sleep(1)
    progress.add_progress()
    time.sleep(1)
    progress.add_progress()
    time.sleep(1)
    progress.change_progress(4)
    time.sleep(1)
    progress.add_progress()
    time.sleep(1)
    progress.add_progress()
    time.sleep(1)
    progress.add_progress()
    time.sleep(1)
    progress.lose_progress()
    time.sleep(1)
    progress.lose_progress()
    time.sleep(1)
    progress.add_progress()
    time.sleep(1)

if __name__ == '__main__':
    main()

