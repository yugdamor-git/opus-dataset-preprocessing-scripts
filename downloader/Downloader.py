from pathlib import Path
from wget import download
import requests

class Downloader:
    def __init__(self):
        print(f'downloader init')
        self.langs = ['en-es', 'en-fr', 'en-ru', 'en-id', 'en-sv', 'en-hr', 'en-fi', 'en-it', 'en-nl', 'en-pt', 'en-pl', 'en-hi', 'en-ja', 'en-ko', 'en-ms', 'en-vi', 'en-ml', 'en-ta', 'en-zh', 'en-mr', 'en-ro', 'en-ur', 'es-fr', 'es-ru', 'es-id', 'es-sv', 'es-fi', 'es-it', 'es-nl', 'es-pt', 'es-pl', 'es-hi', 'es-ja', 'es-ko', 'es-vi', 'es-ta', 'es-zh', 'es-ro', 'fr-ru', 'fr-id', 'fr-sv', 'fr-hr', 'fr-it', 'fr-nl', 'fr-pt', 'fr-pl', 'fr-hi', 'fr-ja', 'fr-ko', 'fr-ms', 'fr-vi', 'fr-ml', 'fr-ta', 'fr-zh', 'fr-ro', 'ru-sv', 'ru-vi', 'ru-ta', 'ru-zh', 'ru-ur', 'cs-id', 'cs-sv', 'cs-hr', 'cs-fi', 'cs-da', 'cs-de', 'cs-it', 'cs-nl', 'cs-pt', 'cs-pl', 'cs-hi', 'cs-ja', 'cs-ko', 'cs-vi', 'cs-ta', 'cs-zh', 'cs-ro', 'id-sv', 'id-it', 'id-nl', 'id-pt', 'id-pl', 'id-ja', 'id-ko', 'id-ms', 'id-vi', 'id-ml', 'id-ta', 'id-zh', 'id-mr', 'id-ro', 'id-ur', 'sv-vi', 'sv-ta', 'sv-zh', 'hr-pl', 'hr-ta', 'hr-zh', 'hr-ro', 'fi-it', 'fi-nl', 'fi-pt', 'fi-pl', 'fi-hi', 'fi-ja', 'fi-ko', 'fi-vi', 'fi-ta', 'fi-zh', 'fi-ro', 'da-de', 'da-it', 'da-nl', 'da-pt', 'da-pl', 'da-ja', 'da-ko', 'da-vi', 'da-ta', 'da-zh', 'da-ro', 'de-it', 'de-nl', 'de-pt', 'de-pl', 'de-hi', 'de-ja', 'de-ko', 'de-ms', 'de-vi', 'de-ml', 'de-ta', 'de-zh', 'de-ro', 'it-nl', 'it-pt', 'it-pl', 'it-ja', 'it-ko', 'it-vi', 'it-ta', 'it-zh', 'it-ro', 'nl-pt', 'nl-pl', 'nl-vi', 'nl-ta', 'nl-zh', 'nl-ro', 'pt-vi', 'pt-ta', 'pt-zh', 'pt-ro', 'pl-vi', 'pl-ta', 'pl-zh', 'pl-ro', 'hi-ja', 'hi-ko', 'hi-ms', 'hi-vi', 'hi-ml', 'hi-ta', 'hi-zh', 'hi-mr', 'hi-ro', 'hi-ur', 'ja-ko', 'ja-ms', 'ja-vi', 'ja-ml', 'ja-ta', 'ja-zh', 'ja-ro', 'ko-vi', 'ko-ta', 'ko-zh', 'ms-vi', 'ms-ta', 'ms-zh', 'vi-zh', 'bn-ml', 'bn-ta', 'bn-zh', 'bn-mr', 'bn-ro', 'bn-ur', 'ml-ta', 'ml-zh', 'ta-zh', 'ta-ur', 'mr-ur', 'ar-ur']
        self.url = "https://object.pouta.csc.fi/OPUS-CCMatrix/v1/moses/{}.txt.zip"
        self.cwd = Path.cwd()
        
        self.downloads = self.cwd.joinpath("downloads")
        
        if not self.downloads.exists():
            self.downloads.mkdir()
    
    def calcFileSize(self,url):
        info = requests.head(url)
        size = round(int(info.headers["Content-Length"]) * 0.000001,2)
        return round(size/1024,2)
           
        
    def downloadFile(self,langCode):
        print(f'processing langcode : {langCode}')
        
        folderPath = self.downloads.joinpath(langCode)
        
        url = self.url.format(langCode)
        
        if not folderPath.exists():
            folderPath.mkdir()
        
        filePath = folderPath.joinpath(f'{langCode}.zip')
        
        if filePath.exists():
            print(f'file already exists : {filePath}')
            return
        
        print(f'file size : {self.calcFileSize(url)}')
        
        download(url,out=str(filePath))
    
    def main(self):
        for code in self.langs[12:13]:
            self.downloadFile(code)

if __name__ == "__main__":
    d = Downloader()
    d.main()