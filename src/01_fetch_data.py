import os
import zipfile
import urllib.request as request

data_url = "https://github.com/entbappy/Branching-tutorial/raw/master/articles.zip"

def download_file():

    filename, headers = request.urlretrieve(
        url = data_url,
        filename = "articles.zip"
    )
    

download_file()
with zipfile.ZipFile("articles.zip", "r") as zip_ref:
    zip_ref.extractall("articles")

# Delete ZIP file
os.remove("articles.zip")