# Import the class that does all the methods
from edit_text import edit_text

# Edit this code below and run
# User Input Parameters
directory_input = r"C:\Users\jackp\Documents\Game Design\SoundProject\Gamemaker\Voice Authority\sounds"
search_for_input = ["type"]
replace_array_input = [1]
remove_character_input = "."
extension_input = "yy"

# Function call
test_var = edit_text(directory=directory_input, search_for=search_for_input, replace_array=replace_array_input,
                     remove_character=remove_character_input, extension=extension_input)
