import os


def add_to_array(array_name, what):
    if array_name[0] == -1:
        array_name[0] = what
    else:
        array_name.append(what)
    return array_name


directory = r"C:\Users\jackp\Documents\Game Design\SoundProject\yy Editing\sounds"
sub_folders = os.walk(directory)
sub_folders = next(os.walk(directory))[1]
search_for = ["type", "bitRate"]
replace_array = [0, 4660]
jack = False

# Get a list of all the sub folder
for path_name in sub_folders:

    # Create a path for the specified sub folder
    folder_path = os.path.join(directory, path_name)

    # Look thru all the files in the folder
    for file_name_all in os.listdir(folder_path):

        # Find the correct file type
        if file_name_all.endswith("yy"):

            # Create path for the file itself
            empty = False
            file_name = os.path.join(folder_path, file_name_all)

            # Open the file
            with open(file_name, "r") as file_name:

                # Get all the file of the code
                file_lines = file_name.readlines()
                # Output Array for correct line
                output_array = [[-1] for x in range(len(search_for))]

                # If the yy file is empty spit ou an error message
                if len(file_lines) == 0:
                    print("Empty YY file")
                    empty = True
                    break
                for a in range(len(file_lines)):
                    for b in range(len(search_for)):
                        if search_for[b] in file_lines[a]:
                            output_array[b] = add_to_array(output_array[b], a)
                # Loop thru all the detentions of the arrays
                for c in range(len(output_array)):
                    # Loop thru all the data in that demention
                    for d in range(len(output_array[c])):
                        line_output = [-1]
                        line = file_lines[output_array[c][d]]
                        line = list(line)
                        for e in range(len(line)):
                            try:
                                print(int(line[e]))
                                line_output = add_to_array(line_output, e)
                            except ValueError:
                                pass
                        for f in range(len(line_output)):
                            line.pop(line_output[f])
                        line.insert(line_output[0] - 1, str(replace_array[c]))
                        line = ''.join(line)
                        file_lines[output_array[c][d]] = line
            if empty:
                break
            with open(file_name, "w") as output_file:
                for output_line in file_lines:
                    output_file.write(output_line+"\n")
                print(output_file.readlines())


            jack = True
    if jack:
        break
