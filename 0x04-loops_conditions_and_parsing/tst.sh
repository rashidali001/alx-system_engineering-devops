#!/usr/bin/env bash

echo "Do  you like Shell scrpting?"
read -p "Yes or No: " answer
case $answer in
	Yes|yes|YES|Y|y)
		echo "That's Amazing"
		;;
	NO|No|no|N|n)
		echo "It's easy. You just have to start"
		;;
esac
