#!/bin/bash

image=$1

docker rmi $image

sleep 2

echo "Done"