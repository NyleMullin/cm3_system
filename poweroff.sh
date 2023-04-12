#!/bin/bash

/usr/bin/raspi-gpio set 34 op dl
while :; do
  sleep 1
  /usr/bin/raspi-gpio set 34 op dl
  sleep 1
  /usr/bin/raspi-gpio set 34 op dl
done
