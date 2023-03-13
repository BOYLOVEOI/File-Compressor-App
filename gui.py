import PySimpleGUI as sg

# Variable Declaration
label1 = sg.Text('Select Files to Compress:')
input1 = sg.Input()

# FilesBrowse() is a button that allows for the selection of files
button1 = sg.FilesBrowse('Choose') 

# FolderBrowse() is a button that allows for the selection of folders
label2 = sg.Text('Select Destination Folder:')
input2 = sg.Input()
button2 = sg.FolderBrowse('Choose')

compress = sg.Button('Compress')

# Window Creation
window = sg.Window('File Compressor', layout=[[
                                            [label1, input1, button1], 
                                            [label2, input2, button2],
                                            [compress]]])

# Calling window.read() to create the window                                       
window.read()
window.close()