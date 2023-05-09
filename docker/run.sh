#!/bin/bash

echo "Enter Host Port: "
read host

echo "Enter Container Post: "
read container

echo "Enter Container Network: "
read network

echo "Give Container Name: "
read name

echo "Give Image Id: "
read id

docker run -dp $host:$container --network=$network --name $name $id

sleep 2

echo "Done ..."