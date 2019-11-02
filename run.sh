#!/bin/bash

echo Do you have env for trtis? y/n
read -p "Your answer: " install_env
if $install_env == 'y'
then
    echo Installing trtserver .........
    docker pull nvcr.io/nvidia/tensorrtserver:19.03-py3
    echo Installing trtclient .........
    git clone https://gitlab.com/TienDucHoang/trtis
    cd trtis
    git checkout client_19.04
    cd tensorrt-inference-server
    git checkout r19.03
    docker build -t tensorrtserver_client -f Dockerfile.client .
fi

# echo Start vehicle detection server .......
# nvidia-docker run --rm --name trtserver -p 8000:8000 -p 8001:8001  -v $1:/models nvcr.io/nvidia/tensorrtserver:19.03-py3 trtserver  --model-store=/models

# echo Start vehicle detection client .....
# nvidia-docker run -it --cpuset-cpus="0-3" -m 1G -v $2:/data --rm --net=host tensorrtserver_client
