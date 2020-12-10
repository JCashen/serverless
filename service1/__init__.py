import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    letterstring = requests.get('https://functionapp1234.azurewebsites.net/api/service2?code=Fg4mg5mnVSTr3Zs/7BJVuzsSIHctxxaH25VzdRgCUqSmEyg/FjODxw==').text
    nostring = requests.get('https://functionapp1234.azurewebsites.net/api/service3?code=pm8FENfrjttUjop6n3xCx0n/AtWX7Lq9DNJbRtACX5i2dU3ekmqGsw==').text
    
    username = ""
    for i in range(5):
        username += letterstring[i]
        username += nostring[i]
    
    endpoint = ""
    key = "k"
    client = CosmosClient(endpoint, key)

    database_name = "name"
    client.create_database_if_not_exists(id=database_name)

    container_name = "UserContainer"
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/username")
    )
    username_to_add = {
        "id": username
    }
    container.create_item(body=username_to_add)

    return username