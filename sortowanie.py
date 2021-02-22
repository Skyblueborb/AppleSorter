import shutil
import os.path
import glob
import ntpath

#Specify the download folder
downloadFolder = fr'/home/skyblueborb/Downloads/' 

#Specify all the extension categories
documents = ['.pdf', '.docx', '.doc', '.txt', '.odt', '.xlsx', '.xls'] 
media = ['.jpeg', '.jpg', '.svg', '.png', '.JPG', '.PNG', '.mp4', '.mp3', '.psd', '.ico', '.pptx', '.wav', '.ppt'] 
setupFiles = ['.exe', '.msi'] 
compressedFiles = ['.zip', '.rar', '.7z'] 
excluded = ['.py', '.crdownload'] 

#Download folder
dir_path = glob.glob(fr'{downloadFolder}*')

#Specify the folder names
documentsLocation = fr'{downloadFolder}Documents/' 
mediaLocation = fr'{downloadFolder}Media/'
setupFilesLocation = fr'{downloadFolder}SetupFiles/'
compressedFilesLocation = fr'{downloadFolder}Zips/'
elseLocation = fr'{downloadFolder}Else/'


class Sorting:
    def __innit__(self):
        pass

    def sort(self, x, y): #! Only renames if there is another file in the target directory
        try: # Tries to make dirs only applicable if first time using the program
            os.makedirs(documentsLocation)
            os.makedirs(mediaLocation)
            os.makedirs(setupFilesLocation)
            os.makedirs(compressedFilesLocation)
            os.makedirs(elseLocation)
        except OSError:
            pass
            for file in dir_path: # Finds all files in the specified directory
                extension = os.path.splitext(file)[1]
                if os.path.isfile(file) and extension in y: # Filters files and filenames
                    try:
                        shutil.move(file, x) # Tries to move them
                    except OSError:
                        timesMoved=1
                        for i in range(10):
                            filename = os.path.splitext(file)[0]
                            extension = os.path.splitext(file)[1]
                            normalName = f"{filename}{extension}"
                            normalNamePlusOne = f"{filename} ({timesMoved}){extension}" 
                            try: #TODO: find the number of times moved after move
                                os.rename(normalName, normalNamePlusOne)
                                shutil.move(normalNamePlusOne, x)
                                timesMoved+=1 
                            except OSError:
                                pass 
    def elsesort(self): # Sorts files depending on excluded variable
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
