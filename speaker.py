#!/usr/bin/env python

"""

MCabber Festival
----------------

Voice incoming messages

"""

import sys, os
import subprocess

CMD_MSG_SAY = 'echo "%s" | festival_client --async --ttw --aucommand \'aplay $FILE\''
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

# russian 'voice_msu_ru_nsh_clunits' doesn't like some symbols, remove it
def replace_for_russian(text):
    import re
    return re.sub(r'[\(\)\?\.\,\\\"\'\[\]\:\;\@\#\$\%\^\&\*\+\>\<\_\/\`\~]', ' ', text)

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

    content = replace_for_russian(content)

    last_filename = os.path.join(ROOT_PATH, 'last_nick')
    with open(last_filename, 'r') as f:
        last = f.read()

    nick, server = arg2.split('@')
    message = ('%s ' % nick) if nick != last else ''
    message += content

    with open(last_filename, 'w') as f:
        f.write(nick)

    subprocess.call(CMD_MSG_SAY % message, shell=True)

if __name__ == '__main__':
    main(sys.argv)
