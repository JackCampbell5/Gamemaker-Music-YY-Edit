import os

directory = r"C:\Users\jackp\Documents\Game Design\SoundProject\Gamemaker\Voice Authority\sounds"
sub_folders = os.walk(directory)
sub_folders = next(os.walk(directory))[1]
search_for = ["type", "bitRate"]

# Get a list of all the sub folder
for path_name in sub_folders:

    # Create a path for the specified sub folder
    folder_path = os.path.join(directory, path_name)

    # Look thru all the files in the folder
    for file_name_all in os.listdir(folder_path):

        # Find the correct file type
        if file_name_all.endswith("yy"):

            # Create path for the file itself
            file_name = os.path.join(folder_path, file_name_all)

            # Open the file
            with open(file_name) as file_name:

                # Get all the file of the code
                file_lines = file_name.readlines()
                # Output Array for correct line
                output_array = [[-1]]*len(search_for)
                print(output_array)

                # If the yy file is empty spit ou an error message
                if len(file_lines) == 0:
                    print("Empty YY file")
                    break
                # Loop thru all the text serching for the words and lines
                for a in range(len(file_lines)):
                    for b in range(len(search_for)):
                        if search_for[b] in file_lines[a]:
                            if output_array[b][0] == -1:
                                output_array[b][0] = a
                            else:
                                output_array[b].append(a)