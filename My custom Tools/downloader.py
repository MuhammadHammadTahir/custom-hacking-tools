import requests

destination = input(f"Enter the URL to download: ")

print(f"Downloading {destination}...")

download_object = requests.get(destination, allow_redirects=True)

if download_object.status_code == 200:
    open("downloaded_file", "wb").write(download_object.content)
    print(f"File downloaded successfully as 'downloaded_file'.")
else:
    print(f"Failed to download file. Status code: {download_object.status_code}")
    print(f"Error message: {download_object.text}")