import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import logging

# from dotenv import load_dotenv
# load_dotenv()

key_vault_uri=os.getenv("KEYVAULT_URI")

credential=DefaultAzureCredential()

client=SecretClient(vault_url=key_vault_uri, credential=credential)

def get_secret(name_secret:str)->str:
    try:
        return client.get_secret(name=name_secret).value
    except Exception as ex:
        logging.error("ERROR AZURE GET SECRET {%s}", ex)