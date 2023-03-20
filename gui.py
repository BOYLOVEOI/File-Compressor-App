import PySimpleGUI as sg
import zip_creator as zc

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

# Theme
sg.theme(new_theme='DarkGrey4')

# Window Creation
window = sg.Window('File Compressor', layout=[[label1, input1, button1], 
                                              [label2, input2, button2],
                                              [compress, exit]],
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

    # If block to compress files or exit application
    if event == 'Compress':
        zc.make_archive(filepath, destination)
    
    elif event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    
window.close()