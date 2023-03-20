import PySimpleGUI as sg
import zip_creator as zc
import pathlib

# Variable Declaration
label1 = sg.Text('Select Files to Compress:')
input1 = sg.Input()

# FilesBrowse() is a button that allows for the selection of files
button1 = sg.FilesBrowse('Choose', key='-FILEPATH-') 

# FolderBrowse() is a button that allows for the selection of folders
label2 = sg.Text('Select Destination Folder:')
input2 = sg.Input()
button2 = sg.FolderBrowse('Choose', key='-DIRECTORY-')

# Compress button
compress = sg.Button('Compress')

# Exit button
exit = sg.Button('Exit')

# Text label
text = sg.Text(key='-OUTPUT-')

# Theme
sg.theme(new_theme='DarkGrey4')

# Window Creation
window = sg.Window('File Compressor', layout=[[label1, input1, button1], 
                                              [label2, input2, button2],
                                              [compress, exit, text]],
                                      font=('Helvetica', 10))

while True:
# Calling window.read() to create the window  
# Assigning the values of window.read() to variables, event and values                                     
    event, values = window.read()

    print(event)
    print(values)

    # Variable Declarations
    filepath = values['-FILEPATH-'].split(';')
    destination = values['-DIRECTORY-']
    filenames = []

    for file in filepath:
        file = pathlib.Path(file)
        filenames.append(file.name)

    # If block to compress files or exit application
    if event == 'Compress':
        zc.make_archive(filepath, destination)
        output_text = ', '.join(filenames)
        window['-OUTPUT-'].update(value=f"The following files, {output_text} have been compressed!")
    
    elif event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    
window.close()