# Create the service principal

az ad sp create-for-rbac --name openairegadmsp --scopes /subscriptions/7e3199f3-4a4e-4c82-88a9-89e0e6e14868/resourceGroups/openai_quickstart/providers/Microsoft.ContainerRegistry/registries/openairegadm --role owner


# Retrieve the service principal ID
USER_NAME=$(az ad sp list --display-name openairegadmsp --query "[].appId" --output tsv)

# Retrieve the service principal password
PASSWORD=$(az ad sp credential reset --name openairegadmsp --credential-description "ACR-Password" --query "password" --output tsv)

# Output the service principal's credentials
echo "Service principal ID: $USER_NAME"
echo "Service principal password: $PASSWORD"

az acr show --name openairegadm --query "id" --output tsv



ACR_REGISTRY_ID=$(az acr show --name openairegadm --query "id" --output tsv)
az ad sp create-for-rbac --name openairegadmsp2 --scopes $ACR_REGISTRY_ID --role owner 

