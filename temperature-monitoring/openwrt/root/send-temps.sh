#!/bin/sh

cd /root

sleep 30

while true; do
	wget -q -O - 'http://'`cat auth.txt`'@stark-savannah-9456.herokuapp.com/add?temp='`digitemp_DS9097 -a | tail -n1 | cut -d' ' -f7`
	sleep 600
done

