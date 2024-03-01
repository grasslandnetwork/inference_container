# Pipeless Example Commands

### Terminal 1: 

```
mkdir /tmp/venv
sudo chown 1001 /tmp/venv # Give the proper permissions for the non-root image
```

Then from inside the my-project directory

```
docker run --rm --gpus all --network=host -v "/tmp/venv:/.venv" -v $(pwd):/app -e "PIPELESS_USER_PYTHON_PACKAGES=opencv-python,numpy" --name pipeless grasslandnetwork/inference_container:pipeless-0.5 start --stages-dir .
```

The mounted volume must have rwx permissions for the root group. In Linux, the root group is just like any other group and by default new users belong to it. Since the Pipeless container is non-root it uses the user 1001, thus, the required permissions allow it to created content in the mounted volume.

### Terminal 2: 

```
docker exec -it pipeless /bin/bash
```

```
pipeless add stream --input-uri "https://pipeless-public.s3.eu-west-3.amazonaws.com/cats.mp4" --output-uri "rtsp://127.0.0.1:8554/mystream" --frame-path "my-stage"

```
### Then view the video output
Either at http://localhost:8889/mystream/ or rtsp://localhost:8554/mystream
