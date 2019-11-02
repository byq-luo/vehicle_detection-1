# vehicle_detection
yolo_v3 YunYang1994 time: 0.15s

# Vehicle detection
## 1. Container detection:
- Download [model.graphdef](https://drive.google.com/drive/folders/154z92tlbAjojCOjgfiGRYLVm9AHo8xvr) and place into 'nvserving/vehicle-detector/1'
- Push your test video in /vehicle_detection and change it name to 1.mp4
- Update nvidia version to nvidia-410
- Install docker and nvidia-docker (follow this [link](https://www.pugetsystems.com/labs/hpc/How-To-Install-Docker-and-NVIDIA-Docker-on-Ubuntu-19-04-1460/) or find it yourself)
- Install client and server docker images follow below step:
```
docker pull nvcr.io/nvidia/tensorrtserver:19.03-py3
git clone https://github.com/NVIDIA/tensorrt-inference-server.git
docker build -t tensorrtserver_client -f Dockerfile.client .
```
- To start server:
```
cd vehicle_detection/nv_serving
bash run_models.sh
```
- To start client:
```
cd vehicle_detection
bash run_clients.sh
```
- Run demo:
In client terminal
```
cd /data
python3 video_clients.py
```
