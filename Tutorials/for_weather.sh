#!/bin/bash

for city in $(cat cities.txt);
do
  weather=$(curl -s http://wttr.in/$city?format=3)
  echo "The weather for $weather"
done

