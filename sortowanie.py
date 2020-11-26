import shutil
import os.path
import glob
import ntpath
from configparser import ConfigParser

configfile = 'config.ini'
config = ConfigParser()
config.read(configfile, encoding='utf-8')
username = config['account']['user']
dir_path = glob.glob(fr'C:/Users/{username}/Downloads/*')
documents = ['.pdf', '.docx', '.doc', '.txt', '.odt', '.xlsx', '.xls']
media = ['.jpeg', '.jpg', '.svg', '.png', '.JPG', '.PNG', '.mp4', '.mp3', '.psd', '.ico', '.jfif', '.pptx', '.wav']
setupFiles = ['.exe', '.msi']
compressedFiles = ['.zip', '.rar', '.7z']
excluded = ['.py', '.ini']
documentsLocation = fr'C:/Users/{username}/Downloads/Document/'
mediaLocation = fr'C:/Users/{username}/Downloads/Media/'
setupFilesLocation = fr'C:/Users/{username}/Downloads/SetupFiles/'
compressedFilesLocation = fr'C:/Users/{username}/Downloads/Zips/'
elseLocation = fr'C:/Users/{username}/Downloads/Else/'

class Sorting:
    def __innit__(self):
        pass

    def sort(self, x, y):
        try:
            os.makedirs(documentsLocation)
            os.makedirs(mediaLocation)
            os.makedirs(setupFilesLocation)
            os.makedirs(compressedFilesLocation)
            os.makedirs(elseLocation)
        except OSError:
            pass
            for file in dir_path:
                if os.path.isfile(file):
                    extension = os.path.splitext(file)[1]
                    filename = ntpath.basename(file)
                    if extension in y:
                        try:
                            os.remove(os.path.join(x, filename))
                        except OSError:
                            pass
                        shutil.move(file, x)

    def elsesort(self):
        for file in dir_path:
            if os.path.isfile(file):
                extension = os.path.splitext(file)[1]
                filename = ntpath.basename(file)
                if extension not in excluded:
                    try:
                        os.remove(os.path.join(elseLocation, filename))
                    except OSError:
                        pass
                    shutil.move(file, elseLocation)



s = Sorting()
s.sort(setupFilesLocation, setupFiles)
s.sort(documentsLocation, documents)
s.sort(mediaLocation, media)
s.sort(compressedFilesLocation, compressedFiles)
s.elsesort()
exit()
