from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient

# Azure AD app registration details
TENANT_ID = "your-tenant-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"

# Replace with your storage account URL
STORAGE_ACCOUNT_URL = "https://app4071storagega.blob.core.windows.net"
CONTAINER_NAME = "container-name"  # Specify your container name

# Create a credential object using ClientSecretCredential
def get_blob_service_client():
    credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    # Create a BlobServiceClient using the credential
    return BlobServiceClient(account_url=STORAGE_ACCOUNT_URL, credential=credential)

def list_folders_and_files(container_name):
    # Get the BlobServiceClient
    blob_service_client = get_blob_service_client()
    
    # Get a client to interact with the specific container
    container_client = blob_service_client.get_container_client(container_name)
    
    # Dictionary to store folders and their respective files
    folders_and_files = {}

    # Iterate over blobs in the container
    blobs = container_client.list_blobs()

    # Process each blob
    for blob in blobs:
        blob_name = blob.name
        # Split the blob name to identify folders and files
        parts = blob_name.split('/')

        if len(parts) > 1:
            folder_name = parts[0]
            file_name = '/'.join(parts[1:])

            # If folder_name is not in the dictionary, add it
            if folder_name not in folders_and_files:
                folders_and_files[folder_name] = []

            # If it's a file (not an empty folder), add the file to the folder
            if file_name:
                folders_and_files[folder_name].append(file_name)

    return folders_and_files

if __name__ == "__main__":
    # Call the function and print the folders and files
    result = list_folders_and_files(CONTAINER_NAME)
    
    for folder, files in result.items():
        print(f"Folder: {folder}")
        for file in files:
            print(f"  File: {file}")