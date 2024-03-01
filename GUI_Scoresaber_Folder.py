import argparse
import os
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from decode_file import decompress, deserialize
from write_to_csv import write_to_csv

gui = Tk()
gui.title("Process DataFiles in Folder")
folder = None

def getFolderPath():
    global folder
    folder = filedialog.askdirectory()
    if folder:
        filepath = os.path.abspath(folder)
        Label(gui, text=str(filepath), font=('Aerial 11')).grid(row=1, column=2)
        if complete:
            complete.config(text="")

def processFilesInFolder():
    global folder
    if folder is None:
        strvarError.set("No Folder Selected")
    else:
        dat_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.dat')]
        if not dat_files:
            strvarError.set("No .dat files found in the folder")
            return

        for file in dat_files:
            processFile(file)
            gui.update()  # Force the GUI to update
            complete.config(text=f"Processing Done!!! 😎")
            

def processFile(file):
    global folder

    folder_name = os.path.splitext(file)[0]
    output_folder = os.path.join(folder, os.path.basename(folder_name))

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    write_to_csv(deserialize(decompress(file)), output_folder)

    df1 = pd.read_csv(os.path.join(output_folder, 'Position.csv'))
    df2 = pd.read_csv(os.path.join(output_folder, 'Notes.csv'))

    mergedRes2 = pd.merge(df1, df2, how='right', on='Time')
    mergedRes2.to_csv(os.path.join(output_folder, 'Notes.csv'), index=False)

    # Remove the second row (considering the first row as headers, so technically this is the first data row)
    df1.drop(df1.index[0], inplace=True)
    # Remove none unique rows for time
    df1.drop_duplicates(subset=['Time'], inplace=True)
    df1.to_csv(os.path.join(output_folder, 'Position.csv'), index=False)

    # Update the completion label for each file processed
    complete.config(text=f"Completed: {os.path.basename(file)}")

# Select Folder Button
ttk.Button(gui, text="Select Folder with .dat Files", command=getFolderPath).grid(row=1, column=1)
Label(gui, text="Replay Folder Path", font=('Aerial 11')).grid(row=1, column=2)

# Start Button
ttk.Button(gui, text="Start", command=processFilesInFolder).grid(row=2, column=1)

# Error Message Label
strvarError = StringVar()
lblError = Label(gui, textvar=strvarError)
lblError.grid(row=2, column=2)

# Completion Message Label
complete = Label(gui, text="", font=('Aerial 11'))
complete.grid(row=2, column=2)  # Adjust grid placement for visibility

gui.mainloop()