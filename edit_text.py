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

    TODO add all the self's and there tpes
    """

    def __init__(self, directory="/", search_for=None, replace_array=None, remove_character=".", extension="yy"):
        """Constructor method

        :param  str directory: The directory that contains all the correct folders
        :param list[str] search_for: What parameters of the file we are looking to change
        :param list[str] replace_array: What number is being replaced
        :param str remove_character: What character you will remove along with any integers
        :param extension: What file type extension we are looking for
        """
        # Variables gotten thru constructor
        if search_for is None:
            search_for = [" "]
        self.search_for = search_for
        self.replace_array = replace_array
        self.directory = directory
        self.remove_character = remove_character
        self.extension = extension

        # Variables
        self.sub_folders = os.walk(directory)
        self.jack = 0  # Temp variable to only run on one folder
        self.start_edit()

    def start_edit(self):
        """Gets a list of all the sub folders and runs them through the check folder function

        Used self.Jack to break after 2 occurrences for testing purposes
        :return: Nothing as the function has no output
        :rtype: None
        """
        # Get a list of all the sub folder
        self.sub_folders = next(os.walk(self.directory))[1]

        # Start looping thru folders
        for folder_name in self.sub_folders:
            self.jack += 1
            # Increases self.jack so not too many
            self.check_folder(folder_name=folder_name)
            # if self.jack >= 1:
            #     return

    def check_folder(self, folder_name):
        """ This goes through the folder finds the one that end

        :param folder_name: The name of the folder we are looping through to help create the file path
        :return: This function returns nothing
        :rtype: None
        """

        # Create a path for the specified sub folder
        folder_path = os.path.join(self.directory, folder_name)

        # Look through all the files in the folder
        for file_name in os.listdir(folder_path):

            # Find the correct file type
            if file_name.endswith(self.extension):
                change_file_output = self.change_file(file_name=file_name, folder_path=folder_path)
                if change_file_output == 1:
                    print(file_name, " has been correctly outputed")
                elif change_file_output == 0:
                    print(file_name," is blank and could not be edited")
                else:
                    print("There was an error encoding ", file_name)

    def change_file(self, file_name, folder_path):
        """ This is the main function that goes through the file in question
         This function gets the correct lines and then writes them to the output file

        :param file_name: The name of the file your going for
        :param folder_path: The path you are going through
        :return: If it returns -1 the file was blank. If it returns a 1 the program succeeded
        :rtype: int
        """

        # Create path for the file itself
        file_path = os.path.join(folder_path, file_name)
        file_lines = self.read_file(file_path=file_path)

        # If the file is empty we do not have to edit it as there is nothing to edit
        if file_lines[0] == "-1":
            return 0
        # Writes the correct output
        return self.write_file(file_lines=file_lines, file_path=file_path)

    def read_file(self, file_path):
        """ This goes through the file gets the lines

        :param str file_path: the path to the file in question
        :return: -1 if the file is blank. Else it returns a array of all the lines to be replaced
        :rtype: list[str]
        """
        # Open the file
        with open(file_path, "r") as file_read:

            # Get all the file of the code
            file_lines = file_read.readlines()
            # Output Array for correct line
            output_array = [[-1] for x in range(len(self.search_for))]

            # If the yy file is empty spit ou an error message
            if len(file_lines) == 0:
                return ["-1"]

            # Go Through the file and update the output_array with where the search for objects are
            for a in range(len(file_lines)):
                for b in range(len(self.search_for)):
                    if self.search_for[b] in file_lines[a]:
                        output_array[b] = add_to_array(output_array[b], a)

            # If there is none of the thing you are searching for print an error message
            for no_search in range(len(self.search_for)):
                if output_array[no_search] == -1:
                    print("There were no occurences of ", self.search_for[no_search])

            # Change the lines to your liking
            return self.change_lines(file_lines=file_lines, output_array=output_array)

    def change_lines(self, file_lines, output_array):
        """This file goes to the positions that have integers and removes them

        :param list[str] file_lines: All the lines in a file
        :param list[str] output_array: The array of where the numbers to be replaced are
        :return: The corrected file_lines array with the updated data
        :rtype: list[str]
        """

        # Loop thru all the detentions of the arrays
        for c in range(len(output_array)):
            # Loop thru all the data in that detention
            for d in range(len(output_array[c])):
                line_output = [-1]
                line = file_lines[output_array[c][d]]
                line = list(line)
                for e in range(len(line)):
                    try:
                        print(int(line[e])) # NEED this print statement
                        line_output = add_to_array(line_output, e)
                    except ValueError:
                        if line[e] == self.remove_character:
                            line_output = add_to_array(line_output, e)
                for f in range(len(line_output)):
                    g = len(line_output) - f - 1
                    # Removes the characters
                    line.pop(line_output[g])

                line.insert(line_output[0], str(self.replace_array[c]))
                line = ''.join(line)
                file_lines[output_array[c][d]] = line

        return file_lines

    def write_file(self, file_lines, file_path):
        """ This takes the lines edited by the change lines fucnction and outputed it

        :param list[str] file_lines: The corrected file lines from the changes_lines function
        :param str file_path: The path to the file we are writing too
        :return: 1 when the function is finished
        :rtype: int
        """

        with open(file_path, "w") as output_file:
            for output_line in file_lines:
                # Removed all the just new lines in the document
                if output_line == "\n":
                    continue
                output_file.write(output_line)
            return 1

