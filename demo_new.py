#!/usr/bin/env python2.7
from progressbar import ProgressBar
import time

def main():
    progress = ProgressBar(10, '#')

    progress.set_bar_color('G')
    progress.set_perc_color('C')
    progress.set_msg_color('K')
    progress.set_width(2)

    progress.update_progress("Starting...")
    time.sleep(1)       # Pretend like this is actually doing something.
    progress.update_progress("Executing...")
    time.sleep(1)
    progress.update_progress()
    time.sleep(1)
    progress.update_progress()
    time.sleep(1)
    progress.update_progress()
    time.sleep(1)
    progress.update_progress()
    time.sleep(1)
    progress.update_progress()
    time.sleep(1)
    progress.move_progress_to(4)
    time.sleep(1)
    progress.update_progress()
    time.sleep(1)
    progress.update_progress()
    time.sleep(1)
    progress.update_progress()
    time.sleep(1)
    progress.dec_progress()
    time.sleep(1)
    progress.dec_progress()
    time.sleep(1)
    progress.update_progress()
    time.sleep(1)

if __name__ == '__main__':
    main()

