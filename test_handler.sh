#!/usr/bin/env sh

BODY="$HOME/.mcabber/event_files/mcabber-10628.sVg5yU"
echo '<== hello, master!' >"$BODY"
~/.mcabber/event-handler.py MSG IN test@gmail.com $BODY
