#!/bin/bash

container=$1

status=$(docker inspect -f '{{.State.Running}}' $container)

if "$status" == "true" ; then
        echo "Container $container is running."
        echo "Stop and Remove  Container $container"
        docker stop $container && docker rm $container
        sleep 2
        echo "Done"
elif "$status" == "false"; then
        echo "Container is Stopped."
        echo "Try to remove Container $container"
        docker rm $container
        sleep 2
        echo "Container $container removed."
else
        echo "Can not determind container $container"
fi