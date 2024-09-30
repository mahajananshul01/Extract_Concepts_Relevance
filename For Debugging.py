from azure.storage.blob import BlobServiceClient

# Replace with your connection string
CONNECTION_STRING = "your_connection_string"
CONTAINER_NAME = "container-name"

def list_folders_and_files(container_name):
    # Create a BlobServiceClient object using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    
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
