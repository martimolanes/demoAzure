## Demo

1. Create flask helloWorld app
2. Contaneirized in docker
3. Upload image -> AzureContainerRegistry
4. Create Azure Kubernetes Service
5. Deploy 2 k8s pods of our webapp with a LoadBalancer

### Create flask helloWorld app

```bash
# create pyenv
pip install -r requirements.txt
python app.py
# access by http://localhost:80
```

### Contaneirized in docker
```bash
sudo docker build -t my-aks-app .
```

```bash
sudo docker run -p 4000:80 my-aks-app
# access by http://localhost:4000
```

### Upload image -> AzureContainerRegistry
```bash
az login
```

```bash
az acr show --name testmartinho --query loginServer --output table
```

```bash
sudo docker login testmartinho.azurecr.io
```

```bash
sudo docker tag my-aks-app:latest testmartinho.azurecr.io/test-aks:latest
```

```bash
sudo docker push testmartinho.azurecr.io/test-aks:latest
```

### Create Azure Kubernetes Service
```bash
az acr repository list --name testmartinho --output table
```

- deployment.yaml
- azurePull

```bash
kubectl create secret docker-registry acr-secret \
  --docker-server=testmartinho.azurecr.io \
  --docker-username=testmartinho \
  --docker-password= \
  --docker-email=fmanu002@edu.xamk.fi
```

```bash
kubectl apply -f deployment.yaml
```

```bash
kubectl get pods
```

### Deploy 2 k8s pods of our webapp with a LoadBalancer
- service.yaml

```bash
kubectl apply -f service.yaml
```

```bash
kubectl get svc my-aks-app-service
```

## Troubleshouting
```bash
kubectl get deployment my-aks-app-deployment

```

```bash
kubectl describe pod [pod-name]
```
