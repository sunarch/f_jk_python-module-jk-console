# Initially taken from:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell
import msvcrt


def readchar(blocking=False):
    "Get a single character on Windows."

    while msvcrt.kbhit():
        msvcrt.getch()
    ch = msvcrt.getch()
    while ch.decode() in '\x00\xe0':
        msvcrt.getch()
        ch = msvcrt.getch()
    return ch.decode()
#

def readchar_loop():
	raise NotImplementedError()
#

def readkeydata_loop():
	raise NotImplementedError()
#








