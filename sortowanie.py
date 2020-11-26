import shutil
import os.path
import glob
import ntpath


dir_path = glob.glob(fr'C:/Users/tomas/Downloads/*')
documents = ['.pdf', '.docx', '.doc', '.txt', '.odt', '.xlsx', '.xls']
media = ['.jpeg', '.jpg', '.svg', '.png', '.JPG', '.PNG', '.mp4', '.mp3', '.psd', '.ico', '.jfif', '.pptx', '.wav']
setupFiles = ['.exe', '.msi']
compressedFiles = ['.zip', '.rar', '.7z']
excluded = ['.py']
documentsLocation = 'C:/Users/tomas/Downloads/Documents/'
mediaLocation = 'C:/Users/tomas/Downloads/Media/'
setupFilesLocation = 'C:/Users/tomas/Downloads/SetupFiles/'
compressedFilesLocation = 'C:/Users/tomas/Downloads/Zips/'
elseLocation = 'C:/Users/tomas/Downloads/Else/'


class Sorting:
    def __innit__(self):
        pass

    def sort(self, x, y):
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
