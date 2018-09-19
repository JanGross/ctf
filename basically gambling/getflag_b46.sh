#!/bin/bash
echo "Attempting to get flag..."
ATTEMPT=1
while :;
do
    echo "Attempt ${ATTEMPT}..."
    ATTEMPT=$[ATTEMPT + 1]
    RESULT=$(nc ctf.minzkraut.com 6646 -w2 | base64 -d | strings | grep "MNZ{")
    if [[ $RESULT ]]; then
        echo "Found the flag"
        echo $RESULT
        break
    fi
done
