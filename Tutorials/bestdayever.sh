#!/bin/bash

# echo "What is your name?"

# read name # for getting inputs

name=$1
compliment=$2

user=$(whoami)
whereami=$(pwd)
date=$(date)

echo "Good Morning $name!!"
sleep 1
echo "You're looking good today $name!!"
sleep 1
echo "You have the best $compliment I've ever seen $name!!"
sleep 2

echo "You're currently logged in as $user and you are in the directory $whereami . Also today is: $date"

