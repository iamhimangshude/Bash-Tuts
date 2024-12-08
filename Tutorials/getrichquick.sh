#!/bin/bash

echo "What's your name?"

read name

echo "What's your age?"

read age

echo "Hello, $name, you are $age years old."

sleep 2

getrich=$((( $RANDOM % 15 ) + $age ))

echo "$name, you will become a millionaire when you are $getrich years old"
