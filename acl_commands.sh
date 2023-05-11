#  https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-acr

az login
az group create --name openai_quickstart --location eastus

az acr create --resource-group openai_quickstart --name openairegadm --sku Basic

az acr login --name openairegadm

docker login openairegadm.azurecr.io -u openairegadm -p eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpYN1c6VkY1UzpNTzZFOlhaNlM6TVgyNzpHMjdXOllNMkM6RFlXSzpKQ1RNOjdFNk46T0Y3WjpGWkIyIn0.eyJqdGkiOiJkNGRkMTEwMi01ZjRlLTRjODktYjdlNy01ZjcyODk0ODU4NGEiLCJzdWIiOiJsaXZlLmNvbSNhbGV4YW5kZXIubWFjY2FsbWFuQG91dGxvb2suY29tIiwibmJmIjoxNjgzNzY0NjE1LCJleHAiOjE2ODM3NzYzMTUsImlhdCI6MTY4Mzc2NDYxNSwiaXNzIjoiQXp1cmUgQ29udGFpbmVyIFJlZ2lzdHJ5IiwiYXVkIjoib3BlbmFpcmVnYWRtLmF6dXJlY3IuaW8iLCJ2ZXJzaW9uIjoiMS4wIiwicmlkIjoiNmM2Zm\MzMjZiZWI0NDVmZDkwZWU1NWM1OWMwYzMyNDgiLCJncmFudF90eXBlIjoicmVmcmVzaF90b2tlbiIsImFwcGlkIjoiMDRiMDc3OTUtOGRkYi00NjFhLWJiZWUtMDJmOWUxYmY3YjQ2IiwidGVuYW50IjoiNDVhZGRiZTctOGRiZi00YzVkLTlmOTMtMjRlZjUxYzg2ZDNjIiwicGVybWlzc2lvbnMiOnsiQWN0aW9ucyI6WyJyZWFkIiwid3JpdGUiLCJkZWxldGUiLCJkZWxldGVkL3JlYWQiLCJkZWxldGVkL3Jlc3RvcmUvYWN0aW9uIl0sIk5vdEFjdGlvbnMiOm51bGx9LCJyb2xlcyI6W119.paUVjr63VzAdd5CzP0RDItQrbPc2cqLUXn36HSnbYkRD1s76W6gQfFiFzfshCpaASL7EjCUPn80osA4xa4ioXHRodeaaa-SbSeuTTMKO1TSbCpZYi7EZIpZ6b9IsRXlwA4VCflEZpOVvZ-7ohHC00IfD5mqVviVmEGtjC-lT2s76dW-Xs40KIGmXPBSZZiBH0y2ebN8fTlKyvtq0VOropKvrfZdSvN0qUZBxltglqBG6eDgJQmu1UptC2gVNkP8eZz_1_eRrs64iLusXFKlNjm1rOz4VtYixswX3V-pkLCI-iM4biF7AVyvOe7Zmna6a4zxOaizlwA3mjrUziv7cbQ