# ** Function that archives/encodes the given text file **
import os


# ** Function that will archive a file given
def archive_file(file_name):
    # Open the file and read it in 'byte' mode
    with open(file_name, "rb") as file:
        # Creating a empty byte array
        byteArray = bytearray()

        # Appending the contents of the text file into the byte array
        byteArray += file.read()

        return byteArray


# ** Function that un-archives the given text file **
def unarchive_file(file_name, encoded_data):
    # This is the path of where we are going to be storing all the files
    # received by the server
    os.chdir("database")
    with open(file_name, "w") as f:
        # Writing the encoded data into an output file
        f.write(encoded_data)
    # Go back to the
    os.chdir("..")