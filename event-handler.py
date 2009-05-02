#!/usr/bin/env python

import sys, os
import subprocess

CMD_MSG_SAY = 'echo "%s %s!" | festival --tts'

def main(argv):
    if len(argv) < 2:
        print """ MCabber event-handler, using:
event-handler.py MSG IN test@gmail.com ~/.mcabber/event_files/mcabber-10628.sVg5yU
"""
        return

    event, arg1, arg2 = argv[1:4]
    if event != 'MSG':
        return

    if arg1 != 'IN':
        return

    filename = argv[4]
    with file(filename) as f:
        content = f.read()
    os.remove(filename)

    subprocess.call(CMD_MSG_SAY % (arg2, content), shell=True)

if __name__ == '__main__':
    main(sys.argv)
