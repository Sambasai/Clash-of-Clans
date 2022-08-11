# """Defining input class."""
# import sys
# import termios
# import tty
# import signal

# class Get:
#     """Class to get input."""

#     def __call__(self):
#         """Defining __call__."""
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             ch = sys.stdin.read(1)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return ch


# class AlarmException(Exception):
#     """Handling alarm exception."""
#     pass


# def alarmHandler(signum, frame):
#     """Handling timeouts."""
#     raise AlarmException


# def input_to(getch, timeout=0.1):
#     """Taking input from user."""
#     signal.signal(signal.SIGALRM, alarmHandler)
#     signal.setitimer(signal.ITIMER_REAL, timeout)
#     try:
#         text = getch()
#         signal.alarm(0)
#         return text
#     except AlarmException:
#         signal.signal(signal.SIGALRM, signal.SIG_IGN)
#         return None

import signal
import sys
import termios
import tty
from time import sleep


class Input:
    def _get_key_raw(self):
        fd = sys.stdin.fileno()
        self.old_config = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.buffer.raw.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, self.old_config)
        return ch

    def _timeout_handler(self, signum, frame):
        raise TimeoutError

    def get_parsed_input(self, timeout=0.1):
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            ip = self._get_key_raw()
            signal.alarm(0)
            if ip in [b'q', b'Q']:
                text = 'quit'
            elif ip in [b'w', b'W']:
                text = 'up'
            elif ip in [b'a', b'A']:
                text = 'left'
            elif ip in [b's', b'S']:
                text = 'down'
            elif ip in [b'd', b'D']:
                text = 'right'
            elif ip == b' ':
                text = 'space'
            elif ip in [b'2']:
                text = 'queen'
            elif ip in [b'1']:
                text = 'king'
            elif ip in [b'j', b'J']:
                text = 'spawn1'
            elif ip in [b'k', b'K']:
                text = 'spawn2'
            elif ip in [b'l', b'L']:
                text = 'spawn3'
            elif ip in [b'b', b'B']:
                text = 'spawn4'
            elif ip in [b'n', b'N']:
                text = 'spawn5'
            elif ip in [b'm', b'M']:
                text = 'spawn6'
            elif ip in [b'i', b'I']:
                text = 'spawn7'
            elif ip in [b'o', b'O']:
                text = 'spawn8'
            elif ip in [b'p', b'P']:
                text = 'spawn9'
            elif ip in [b'h', b'H']:
                text = 'heal'
            elif ip in [b'r', b'R']:
                text = 'rage'
            elif ip in [b'x', b'X']:
                text = 'axe'
            else:
                text = 'none'
            sleep(timeout)
            return text
        except TimeoutError:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None
