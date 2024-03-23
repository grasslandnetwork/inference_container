# Pipeless Example Commands

## Run Docker Container

### Terminal 1: 
From inside the pipeless directory

```
docker compose up
```

### Terminal 2: 

```
docker exec -it pipeless /bin/bash
```

```
pipeless add stream --input-uri "https://pipeless-public.s3.eu-west-3.amazonaws.com/cats.mp4" --output-uri "rtsp://127.0.0.1:8554/mystream" --frame-path "my-stage"

```
### Then view the video output
Either at http://localhost:8889/mystream/ or rtsp://localhost:8554/mystream


### To stop the containers
```
Ctrl-c
```

To remove stopped containers
```
docker compose down
```


## Build Docker Image

From inside the pipeless directory

```
docker build -f Dockerfile-cpu -t grasslandnetwork/inference_container-cpu:latest .
```
