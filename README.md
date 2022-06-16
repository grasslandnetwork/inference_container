# inference_container

## Building the image

cd into the repo's root directory


```
docker build -t 932200675199.dkr.ecr.ca-central-1.amazonaws.com/inference_container:1.0 . 
```

## Running the container

```
sudo docker run -t --gpus all --rm --network=host 932200675199.dkr.ecr.ca-central-1.amazonaws.com/inference_container:1.0
```

## Default URL's

The default RTSP URL that it reads from is below. Change the value to the output RTSP URL of the kinesis_to_rtsp container

```
--source rtsp://0.0.0.0:8554/live.stream 
```
## Default Output
Right now, a summary of the results is just printed to the terminal

## Deployment

The application is deployed using [ArgoCD](https://argo-cd.readthedocs.io/en/stable/)

If the application has ***not*** been setup in ArgoCD, run this command (assuming that you have logged into the cluster.

```
argocd app create inference-app --repo https://github.com/grasslandnetwork/inference_container --revision "staging" --path inference-app  --dest-server https://6BA0D4357FE2259828A5367EFAB0218C.yl4.ca-central-1.eks.amazonaws.com --dest-namespace inference-app
```

Once the application is setup in ArgoCD, updates can be made to the [helm chart](https://helm.sh/docs/topics/charts/) which has config in the file `./inference-app/values.yaml`

Once config updates have been made, a PR/merge is made to the monitored branch which is `staging` currently & the ArgoCD process picks this up & auto-deploys into the `staging` EKS cluster.

