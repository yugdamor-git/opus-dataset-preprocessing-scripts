from pathlib import Path
from wget import download
import requests

class Downloader:
    def __init__(self):
        print(f'downloader init')
        self.langs = dataFound = [{'source': 'english', 'target': 'spanish', 'title': 'english - spanish', 'sourceCode': 'en', 'targetCode': 'es', 'code': 'en-es'}, {'source': 'english', 'target': 'french', 'title': 'english - french', 'sourceCode': 'en', 'targetCode': 'fr', 'code': 'en-fr'}, {'source': 'english', 'target': 'russian', 'title': 'english - russian', 'sourceCode': 'en', 'targetCode': 'ru', 'code': 'en-ru'}, {'source': 'english', 'target': 'indonesian', 'title': 'english - indonesian', 'sourceCode': 'en', 'targetCode': 'id', 'code': 'en-id'}, {'source': 'english', 'target': 'swedish', 'title': 'english - swedish', 'sourceCode': 'en', 'targetCode': 'sv', 'code': 'en-sv'}, {'source': 'english', 'target': 'croatian', 'title': 'english - croatian', 'sourceCode': 'en', 'targetCode': 'hr', 'code': 'en-hr'}, {'source': 'english', 'target': 'finnish', 'title': 'english - finnish', 'sourceCode': 'en', 'targetCode': 'fi', 'code': 'en-fi'}, {'source': 'english', 'target': 'italian', 'title': 'english - italian', 'sourceCode': 'en', 'targetCode': 'it', 'code': 'en-it'}, {'source': 'english', 'target': 'dutch', 'title': 'english - dutch', 'sourceCode': 'en', 'targetCode': 'nl', 'code': 'en-nl'}, {'source': 'english', 'target': 'portuguese', 'title': 'english - portuguese', 'sourceCode': 'en', 'targetCode': 'pt', 'code': 'en-pt'}, {'source': 'english', 'target': 'polish', 'title': 'english - polish', 'sourceCode': 'en', 'targetCode': 'pl', 'code': 'en-pl'}, {'source': 'english', 'target': 'hindi', 'title': 'english - hindi', 'sourceCode': 'en', 'targetCode': 'hi', 'code': 'en-hi'}, {'source': 'english', 'target': 'japanese', 'title': 'english - japanese', 'sourceCode': 'en', 'targetCode': 'ja', 'code': 'en-ja'}, {'source': 'english', 'target': 'korean', 'title': 'english - korean', 'sourceCode': 'en', 'targetCode': 'ko', 'code': 'en-ko'}, {'source': 'english', 'target': 'malay', 'title': 'english - malay', 'sourceCode': 'en', 'targetCode': 'ms', 'code': 'en-ms'}, {'source': 'english', 'target': 'vietnamese', 'title': 'english - vietnamese', 'sourceCode': 'en', 'targetCode': 'vi', 'code': 'en-vi'}, {'source': 'english', 'target': 'malayalam', 'title': 'english - malayalam', 'sourceCode': 'en', 'targetCode': 'ml', 'code': 'en-ml'}, {'source': 'english', 'target': 'tamil', 'title': 'english - tamil', 'sourceCode': 'en', 'targetCode': 'ta', 'code': 'en-ta'}, {'source': 'english', 'target': 'chinese', 'title': 'english - chinese', 'sourceCode': 'en', 'targetCode': 'zh', 'code': 'en-zh'}, {'source': 'english', 'target': 'marathi', 'title': 'english - marathi', 'sourceCode': 'en', 'targetCode': 'mr', 'code': 'en-mr'}, {'source': 'english', 'target': 'romanian', 'title': 'english - romanian', 'sourceCode': 'en', 'targetCode': 'ro', 'code': 'en-ro'}, {'source': 'english', 'target': 'urdu', 'title': 'english - urdu', 'sourceCode': 'en', 'targetCode': 'ur', 'code': 'en-ur'}]
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
        for lang in self.langs[12:13]:
            self.downloadFile(lang["code"])

if __name__ == "__main__":
    d = Downloader()
    d.main()