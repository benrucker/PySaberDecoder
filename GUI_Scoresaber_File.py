

import argparse

from decode_file import decompress, deserialize
from write_to_csv import write_to_csv

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import pandas as pd
import numpy as np


gui = Tk()
gui.title("Process the DataFile")
file = None
folder = None

def getFolderPath():
    global file
    global filepath
    file = filedialog.askopenfilename()
    if file:
        filepath = os.path.abspath(file)
        Label(gui, text=str(filepath), font=('Aerial 11')).grid(row=1, column=2)
        if complete:
            complete.config(text="")

def getFolderPath3():
  global folder
  global filepath3
  folder = filedialog.askdirectory()
  if folder:
        filepath3 = os.path.abspath(folder)
        Label(gui, text=str(filepath3), font=('Aerial 11')).grid(row=2, column=2)
        if complete:
            complete.config(text="")

def onFolderConfirmed():
    global file
    global folder
    if file is None:
        strvarError.set("No Note File Selected")
    if folder is None:
        strvarError.set("No Output Folder Selected")
    else:
        doSomethingWithFolder()

def doSomethingWithFolder():
    global file
    global folder
    global parser
    global folder_name 
    global folder2

    folder_name=os.path.splitext(filepath)[0]

    parser = argparse.ArgumentParser(
        description='Decompress & decode a ScoreSaber replay file'
        )

    parser.add_argument(
        '-i',
        '--input',
        help='path to the file to parse',
        default=filepath
        )

    parser.add_argument(
        '-o',
        '--output',
        help='path to the output folder',
        default=os.path.join(filepath3,"/",folder_name)
        )

    args = parser.parse_args()

    write_to_csv(deserialize(decompress(args.input)), args.output)
    folder2=os.path.join(filepath3,"/",folder_name)
    df1=pd.read_csv(f'{folder2}/Position.csv')
    df2=pd.read_csv(f'{folder2}/Notes.csv')
    mergedRes2 = pd.merge(df1, df2,how='right', on ='Time')
    mergedRes2.to_csv(f'{folder2}/Notes.csv')
    mergedRes = pd.merge(df1, df2,how='left', on ='Time')
    mergedRes= mergedRes.drop(columns=["CutPoint.X","CutPoint.Y","CutPoint.Z","CutPoint.Y","CutNormal.X","CutNormal.Y","CutNormal.Z","SaberDirection.X","SaberDirection.Y","SaberDirection.Z","SaberType","CutAngle","CutDistanceToCenter","CutDirectionDeviation","BeforeCutRating","AfterCutRating"])
    mergedRes.to_csv(f'{folder2}/Position.csv')
    complete.config(text="Complete")


##Notes Row
btnFind = ttk.Button(gui, text="Select Replay File", command=getFolderPath)
btnFind.grid(row=1, column=1)
Label(gui, text="Replay File Path", font=('Aerial 11')).grid(row=1, column=2)

##Output Folder
ttk.Button(gui, text="Select Output Folder",command=getFolderPath3).grid(row=2,column=1)
Label(gui, text="Output File Path", font=('Aerial 11')).grid(row=2, column=2)
##Start Button
btnConfirm = ttk.Button(gui, text="Start", command=onFolderConfirmed)
btnConfirm.grid(row=3, column=2)
strvarError = StringVar()
## ERROR VALUE
lblError = Label(gui, textvar=strvarError)
lblError.grid(row=3, column=1)
## COMPLETE VALUE
complete=Label(gui, text="", font=('Aerial 11'))
complete.grid(row=3, column=1)
gui.mainloop()

