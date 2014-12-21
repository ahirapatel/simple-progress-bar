#!/usr/bin/env python2.7

# Useful links:
# http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html

import time
import sys

bcolors = {
    'K' : '\033[90m',
    'R' : '\033[91m',
    'G' : '\033[92m',
    'B' : '\033[94m',
    'C' : '\033[96m',
    'M' : '\033[95m',
    'Y' : '\033[93m',
    'N' : '\033[0m'}

class ProgressBar(object):
    """ This is a super simple progress bar for the command line.  """

    # TODO: Testing.
    # TODO: A version of this that you can just say increment to X percent done.
    # TODO: Add colors.
    def __init__(self, steps, fillchar = '|'):
        """
        The number of steps until the bar gets to 100%
        steps: Number of times the object's update_progress() can be called
        fillchar: The character to fill the bar with.
        """
        self._curr = 0
        self._steps = steps
        self._msg = None
        self._width = 4

        self._bcol = bcolors['N']
        self._pcol = bcolors['N']
        self._mcol = bcolors['N']

        if len(fillchar) != 1 or not fillchar:
            raise Exception("Invalid value for fillchar")
        else:
            self._fillchar = fillchar

    # TODO: Get the size of the terminal (Get it everytime here or just once in __init__ ?)
    def update_progress(self, msg = None):
        """
        Update the progress bar status and print it.
        If msg=None, then use previous message, if no previous message, do not use second row.
        If msg=<some string> print it and store it as the previously used string.
        If msg=<some string>, then upon next call msg=None, the old string will be printed.
        """
        if self._curr > self._steps:
            raise Exception("Progress bar already completed")

        # Store previous message if provided.
        self._msg = self._mcol + msg + bcolors['N'] if msg != None else self._msg

        # Move to appropriate location to change progress bar and message.
        self.move_up_as_needed()
        self.move_to_start_of_line()

        print self.get_progress_bar()
        if self._msg:
            # TODO: Or just pad msg with space characters?
            self.clear_curr_line()          # Clear the line with the old message on it. If the old message is larger parts of it will remain if you just do a print.
            print self._msg
        sys.stdout.flush()

        self._curr += 1

    def dec_progress(self, msg = None):
        if self._curr < 0:
            raise Exception("Progress bar already empty")

        # Store previous message if provided.
        self._msg = self._mcol + msg + bcolors['N'] if msg != None else self._msg

        # Move to appropriate location to change progress bar and message.
        self.move_up_as_needed()
        self.move_to_start_of_line()

        print self.get_progress_bar()
        if self._msg:
            # TODO: Or just pad msg with space characters?
            self.clear_curr_line()          # Clear the line with the old message on it. If the old message is larger parts of it will remain if you just do a print.
            print self._msg
        sys.stdout.flush()

        self._curr -= 1

    def move_progress_to(self, point, msg = None):
        # We don't care if we've already reached full for this
        # We do care about trying to jump to a point greater than 100%
        if self._steps < point:
            raise Exception("Point is outside the bounds of the progress bar")
        self._msg = self._mcol + msg + bcolors['N'] if msg != None else self._msg

        self.move_up_as_needed()
        self.move_to_start_of_line()

        print self.get_progress_bar()
        if self._msg:
            self.clear_curr_line()
            print self._msg
        sys.stdout.flush()

        # Set our current value to the point we want to jump to
        self._curr = point

    def move_up_as_needed(self):
        """
        Move up in the term once or twice, depending on if you have a message.
        """
        if self._curr != 0:
            self.move_up_one_line()
            if self._msg != None:
                self.move_up_one_line()

    def get_terminal_width(self):
        """
        Get the width of the terminal.
        """
        import os
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(columns)

    def move_to_start_of_line(self):
        """
        Moves to the start of the current line.
        """
        print "\r",

    def move_up_one_line(self):
        """
        Moves up one line in the terminal.
        """
        print "\033[1A",

    def clear_curr_line(self):
        """
        Clears the current line by filling with spaces then moves to the start.
        """
        print ' '.ljust(self.get_terminal_width()-1), '\r',

    def set_width(self, width):
        """
        Sets what we divide the terminal width by when drawing the progress bar
        """
        self._width = width

    def set_bar_color(self, col):
        """
        Sets the progress bar color
        col: key for the bcolors dict; if not found, no color is set
        """
        if col in bcolors:
            self._bcol = bcolors[col]

    def set_perc_color(self, col):
        """
        Sets the progress percentage color
        col: key for the bcolors dict; if not found, no color is set
        """
        if col in bcolors:
            self._pcol = bcolors[col]

    def set_msg_color(self, col):
        """
        Sets the message color
        col: key for the bcolors dict; if not found, no color is set
        """
        if col in bcolors:
            self._mcol = bcolors[col]

    def get_progress_bar(self):
        """
        Outputs the progress bar string.
        """
        reserved_char_count = 2     # For start and ending character of the progress bar.
        progress_chars_max = self.get_terminal_width() - reserved_char_count
        progress_chars_max /= self._width    # Arbitrarily make it 1/4th the number of chars that can fit onscreen.
        percent_done = float(self._curr) / self._steps
        progress = int(percent_done * progress_chars_max)
        bar = "[" + self._bcol.ljust(progress_chars_max, ' ') + bcolors['N'] + "]"
        return bar.replace(' ', self._fillchar, progress) + self._pcol + ' {}%'.format(percent_done*100) + bcolors['N']

