import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    letterstring = requests.get('https://randostring.azurewebsites.net/api/service2?code=0PIZjZ5krmmlkIeoW1vwD40ezvlnUUWgIQYe3kLneP/BAoAkTa0TDA==').text
    nostring = requests.get('https://randostring.azurewebsites.net/api/service2?code=0PIZjZ5krmmlkIeoW1vwD40ezvlnUUWgIQYe3kLneP/BAoAkTa0TDA==').text
    
    username = ""
    for i in range(5):
        username += letterstring[i]
        username += nostring[i]
    
    endpoint = "https://george-rhodes.documents.azure.com:443/"
    key = "kILpCMZAwpelpDZMAxawxHM7pgETsCi4kiWY1qB9XZMP3CaHfCw74LUEZeWMwsLtEEmd6Vfmi6iMcJuvEyghIg=="
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