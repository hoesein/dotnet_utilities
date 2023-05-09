#!/bin/bash

name=$1

docker build -it --name $name .