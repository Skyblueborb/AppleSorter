import shutil
import os.path
import glob
import ntpath
import platform
import pwd

#Specify the download folder depending on the system
downloadFolder = ''
userLogin = pwd.getpwuid(os.geteuid())[0]
userOS = platform.system()

if userOS == 'Windows':
    downloadFolder = fr'C://Users//{userLogin}//Downloads//'
elif userOS == 'Linux':
    downloadFolder = fr'/home/{userLogin}/Downloads/' 
elif userOS == 'Darwin':
    downloadFolder = fr'/Users/{userLogin}/Downloads/'

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

    def sort(self, x, y):
        self.makeDirs()
        for file in dir_path: # Finds all files in the specified directory
            extension = os.path.splitext(file)[1]
            if os.path.isfile(file) and extension in y: # Filters files and filenames
                try:
                    shutil.move(file, x) # Tries to move them
                except OSError:
                    # Gets nessecary info about the file
                    filenameWithExtension = os.path.basename(file)
                    onlyFilename = os.path.splitext(filenameWithExtension)[0]
                    filenamePlusOne = f'{downloadFolder}{onlyFilename} (1){extension}'
                    try:
                        # Finds the index of the number to be changed
                        indexOfCharacter = onlyFilename.index(f'(') + 1
                        # Variables of the numbers
                        number = onlyFilename[indexOfCharacter]
                        numberIntPlusOne = str(int(number) + 1)
                        # Figures out how how to rename it
                        filenameRenamed = onlyFilename[:indexOfCharacter] + numberIntPlusOne + onlyFilename[indexOfCharacter+1:]
                        wholePathFileRenamed = f"{downloadFolder}{filenameRenamed}{extension}"
                        os.rename(file, wholePathFileRenamed) # Renames it
                        shutil.move(wholePathFileRenamed, x) # Finally it move it
                    except ValueError:
                        os.rename(file, filenamePlusOne)
                        shutil.move(filenamePlusOne, x)
                        pass
                    pass

    def makeDirs(self): # Tries to make dirs only applicable if first time using the program
        allDirs = [documentsLocation, mediaLocation, setupFilesLocation, compressedFilesLocation, elseLocation]
        timeRun = 0
        while timeRun <= 4:
            try:
                os.makedirs(allDirs[timeRun])
                timeRun += 1
            except FileExistsError:
                timeRun += 1
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


if __name__ == "__main__":
    s = Sorting()
    s.sort(setupFilesLocation, setupFiles)
    s.sort(documentsLocation, documents)
    s.sort(mediaLocation, media)
    s.sort(compressedFilesLocation, compressedFiles)
    s.elsesort()
