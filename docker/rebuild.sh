#!/bin/bash
sudo docker-compose -f docker/local.yml down --volumes --remove-orphans --rmi=local
sudo docker-compose -f docker/local.yml build --force-rm --no-cache