#  https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-acr

az login
az group create --name openai_quickstart --location eastus

az acr create --resource-group openai_quickstart --name openairegadm --sku Basic

az acr login --name openairegadm

az acr show --name openairegadm --query loginServer --output table

docker tag quickstart openairegadm.azurecr.io/quickstart:v1

docker push openairegadm.azurecr.io/quickstart:v1

az acr repository list --name openairegadm --output table

az acr repository show-tags --name openairegadm --repository quickstart --output table

# https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-deploy-app

# first create a service principle
# https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auth-aci

az acr show --name openairegadm --query loginServer

az container create --resource-group openai_quickstart --name quickstart --image openairegadm.azurecr.io/quickstart:v1 --cpu 1 --memory 1 --registry-login-server openairegadm.azurecr.io --registry-username 82aaded4-ae99-459d-ad28-acdf65173516 --registry-password UXh8Q~vlNQ6jI0W_DaL15Gimk7Hy4FFnNssRJcoC --ip-address Public --dns-name-label alexmaccalmanopenaiquickstart --ports 5000

az container show --resource-group openai_quickstart --name quickstart --query instanceView.state

az container logs --resource-group openai_quickstart --name quickstart