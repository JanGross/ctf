#!/bin/bash

#Get everything from the data segment
DATA_SEGMENT=$(readelf -p '.data' auth.o)
#Get the adress of the factory user variable and strip leading 0s
USERNAME_ADDRESS=$(readelf -s auth.o | grep "DEFAULT_FACTORY_USER" | awk '{print $2}' | sed 's/^0*//')
#Get the username value from the data segment, remove th adress column
USERNAME=$(echo "$DATA_SEGMENT" | grep $USERNAME_ADDRESS | awk '{print $3}')
echo "Username: $USERNAME"

#Repeat for the password
PASSWORD_ADDRESS=$(readelf -s auth.o | grep "DEFAULT_FACTORY_PW" | awk '{print $2}' | sed 's/^0*//')
PASSWORD=$(echo "$DATA_SEGMENT" | grep $PASSWORD_ADDRESS | awk '{print $3}')
echo "Password: $PASSWORD"

echo "Login and find the flag at loremcorp.ctf.minzkraut.com:8787/login.php"
