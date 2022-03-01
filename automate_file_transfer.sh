#!/usr/bin/bash

for index in "$@"
do
	image="test$index.jpg"
	text="test$index.txt"
	while [ ! -f "/home/jinhwee-desktop/Desktop/MDP-images/raw_images/$image" ]
		do
			true
		done
	python detect.py --weights ../best.pt --img 544 --conf 0.25 --source "../raw_images/$image" --save-txt --project ~/Desktop/MDP-images/results/
	if [ ! -f "/home/jinhwee-desktop/Desktop/MDP-images/results/labels/$text" ]
		then
			mkdir -p "/home/jinhwee-desktop/Desktop/MDP-images/results/labels"
			echo "No labels found" > "/home/jinhwee-desktop/Desktop/MDP-images/results/labels/$text"
		fi
	sshpass -p "raspberry" scp "../results/labels/$text" pi@192.168.20.20:/home/pi/Desktop/MDPGroup20/results/
	echo "$text sent over to RPI"
done
