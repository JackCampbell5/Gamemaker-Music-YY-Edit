import os


def add_to_array(array_name, what):
    """
    Adds to  the end of an array or the 1st element if it = negative 1

    :param list array_name: The name of the Array to add too
    :param str what: What to add to the array
    :return: The output list
    :rtype: list
    """
    if array_name[0] == -1:
        array_name[0] = what
    else:
        array_name.append(what)
    return array_name


class edit_text:
    """What the class is about

    :param str directory: The directory that contains all the correct folders
    :param list search_for: What parameters of the file we are looking to change
    :param list replace_array: What number is being replaced
    """

    def __init__(self, directory, search_for, replace_array,remove_character):
        """Constructor method
        """
        # Variables gotten thru constructor
        self.search_for = search_for
        self.replace_array = replace_array
        self.directory = directory
        self.remove_character = remove_character

        # Variables
        self.sub_folders = os.walk(directory)
        self.jack = 0  # Temp variable to only run on one folder
        self.start_edit()

    def start_edit(self):
        # Start working on variables
        self.sub_folders = next(os.walk(directory))[1]

        # Get a list of all the sub folder
        for folder_name in self.sub_folders:
            self.jack += 1
            self.check_folder(folder_name=folder_name)
            if self.jack >= 2:
                return

    def check_folder(self, folder_name):

        # Create a path for the specified sub folder
        folder_path = os.path.join(self.directory, folder_name)

        # Look through all the files in the folder
        for file_name in os.listdir(folder_path):

            # Find the correct file type
            if file_name.endswith("yy"):
                self.change_file(file_name=file_name, folder_path=folder_path)

    def change_file(self, file_name, folder_path):

        # Create path for the file itself
        file_path = os.path.join(folder_path, file_name)
        file_lines = self.read_file(file_path=file_path)

        # If the file is empty we do not have to edit it as there is nothing to edit
        if file_lines == -1:
            return -1

        self.write_file(file_lines=file_lines, file_path=file_path)

    def read_file(self, file_path):
        # Open the file
        with open(file_path, "r") as file_read:

            # Get all the file of the code
            file_lines = file_read.readlines()
            # Output Array for correct line
            output_array = [[-1] for x in range(len(search_for))]

            # If the yy file is empty spit ou an error message
            if len(file_lines) == 0:
                print("Empty YY file")
                return -1

            # Go Through the file and update the output_array with where the search for objects are
            for a in range(len(file_lines)):
                for b in range(len(search_for)):
                    if search_for[b] in file_lines[a]:
                        output_array[b] = add_to_array(output_array[b], a)

            # If there is none of the thing you are searching for print an error message
            for no_search in range(len(search_for)):
                if output_array[no_search] == -1:
                    print("There were no occurences of ", search_for[no_search])

            # Change the lines to your liking
            return self.change_lines(file_lines=file_lines, output_array=output_array)

    def change_lines(self, file_lines, output_array):

        # Loop thru all the detentions of the arrays
        for c in range(len(output_array)):
            # Loop thru all the data in that detention
            for d in range(len(output_array[c])):
                line_output = [-1]
                line = file_lines[output_array[c][d]]
                line = list(line)
                for e in range(len(line)):
                    try:
                        print(int(line[e]))
                        line_output = add_to_array(line_output, e)
                    except ValueError:
                        if line[e] == self.remove_character:
                            line_output = add_to_array(line_output, e)
                for f in range(len(line_output)):
                    g = len(line_output)-f-1
                    print(g)
                    print(line)
                    print(line_output)
                    line.pop(line_output[g])
                print(line)

                line.insert(line_output[0], str(replace_array[c]))
                line = ''.join(line)
                file_lines[output_array[c][d]] = line

        return file_lines

    def write_file(self, file_lines, file_path):
        print(file_path)
        print(file_lines)
        with open(file_path, "w") as output_file:
            for output_line in file_lines:
                if output_line == "\n":
                    continue
                output_file.write(output_line)


# The code that runs on program start

# User Input Parameters
directory = r"C:\Users\jackp\Documents\Game Design\SoundProject\yy Editing\sounds"
search_for = ["type", "bitRate"]
replace_array = [1, 200.0]
remove_character = "."

test_var = edit_text(directory=directory, search_for=search_for, replace_array=replace_array, remove_character=remove_character)
