
minikube start --driver=docker

eval $(minikube docker-env)

kubectl apply -f kubernetes/secret.yaml
kubectl apply -f kubernetes/configmap.yaml
kubectl apply -f kubernetes/deployment.yaml

kubectl get pods