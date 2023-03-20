# Import statements 
import zipfile 
import pathlib

# Function Declaration
def make_archive(filepath, directory):
    
    # pathlib.Path to create the path to the newly created zip file in the destination folder
    # "compressed.zip" can be changed/modified to user preference for their zip file name
    dest_path = pathlib.Path(directory, "compressed.zip")
    
    with zipfile.ZipFile(dest_path, 'w', 
                         compression=zipfile.ZIP_DEFLATED, 
                         # Compresslevel set to 9, but can be changed depending upon user
                         compresslevel=9) as zf:
        for file in filepath:   
            zf.write(file)
