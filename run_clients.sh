#!/bin/bash
nvidia-docker run -it --cpuset-cpus="0-2" -m 1G -v `pwd`:/data --rm --net=host clients_19.03