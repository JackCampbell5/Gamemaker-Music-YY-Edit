import os

directory = r"C:\Users\jackp\Documents\Game Design\SoundProject\Gamemaker\Voice Authority\sounds"
subFolders = os.walk(directory)
subFolders = next(os.walk(directory))[1]
searchFor = ["type", "bitRate"]

# Get a list of all the sub folder
for pathName in subFolders:
    # Create a path for the specified sub folder
    folderPath = os.path.join(directory, pathName)
    # Look thru all the files in the folder
    for fileNameAll in os.listdir(folderPath):
        # Find the correct file
        if fileNameAll.endswith("yy"):
            fileName = os.path.join(folderPath, fileNameAll)
            fileRead = open(fileName, "r")
            fileWrite = open(fileName, "w")
            fileLines = fileRead.readline(20)
            print(fileLines)
            for line in fileLines:
                print(line)
                for word in searchFor:
                    if word in line:
                        print(line)

            exit()
