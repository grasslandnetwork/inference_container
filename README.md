# Substrate version of the Grassland Inference Container

## Building the image

cd into the repo's root directory

## Download the Model to the '/app' Directory

```
cd app
wget https://downloads.grassland.network/models/p6.pt

```
## Return to the Root Directory and Build the Docker Image

```
cd ..
docker build -t grasslandnetwork/inference_container:0.3 .
```

## Running the container

For DPT (depth detection), create a "weights" directory in the root folder and add the depth models there.
Place the detection models inside the "app" directory

Ensure that the Substrate version of the Grassland full node is running first. This inference container assumes that the node is listening for incoming WebSocket traffic on 127.0.0.1:9944

```
docker run -t --gpus all --rm --network=host grasslandnetwork/inference_container:0.3
```

If you're using a webcam, add "--device=/dev/video0" to ensure that the container can access the webcam 
```
docker run -t --gpus all --rm --device=/dev/video0 --network=host grasslandnetwork/inference_container:0.3
```

## Default URL's

The default RTSP URL that it reads from is "rtsp://0.0.0.0:8554/live.stream". Change the RTSP URL to whatever feed you're reading from by appending the following to the end of the "docker run...." command above.

```
--source [YOUR RTSP URL]
```

## RTSP server and proxy

If you need an RTSP server, the rtsp-simple-server is very good. It's maintained [here](https://github.com/aler9/rtsp-simple-server).



## Profile The Model

From root 

```
python -m tests.profile_models
```
