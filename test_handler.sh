#!/usr/bin/env sh

BODY="$HOME/.mcabber/event_files/mcabber-10628.sVg5yU"
echo 'hello!' >"$BODY"
~/.mcabber/event-handler.py MSG IN checker@gmail.com $BODY
echo 'again )' >"$BODY"
~/.mcabber/event-handler.py MSG IN checker@gmail.com $BODY
