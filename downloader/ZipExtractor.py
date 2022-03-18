from zipfile import ZipFile
from pathlib import Path

class ZipExtractor:
    def __init__(self):
        self.cwd = Path.cwd()

        self.downloads = self.cwd.joinpath("downloads")
    
    def extract(self):
        for folder in list(self.downloads.iterdir()):
            print(f'processing -> {folder.name}')
            
            zipPath = folder.joinpath(f'{folder.name}.zip')
            
            filesDir = folder.joinpath("files")
            
            if not filesDir.exists():
                filesDir.mkdir()
            
            
            
            if not zipPath.exists():
                print(f'zip file does not exists : {zipPath.name}')
                continue
            with ZipFile(zipPath,"r") as zFile:
                zFile.extractall(filesDir)
            
            print(f'zip file extracted : {zipPath.name}')
            

if __name__ == "__main__":
    e = ZipExtractor()
    e.extract()