#! /usr/bin/env bash

# saves microphone to files and plays.
# created as an improve 

if [ -n "$1" ]; then
    echo "saving to $1"
else
    >&2 echo "specify an output file"
    exit 2
fi

arecord --buffer-time=1 -f s16_LE | tee $1 | aplay --buffer-time=1 -

