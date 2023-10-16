# minikube start --force --cpus=1
eval $(minikube -p minikube docker-env)
docker build -t albert-finetuning-job-minikube:latest ../source
kubectl apply -f minikube.yaml