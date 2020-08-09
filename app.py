import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []
root.resizable(True, True)

# handles the extra whitespace in save.txt bug
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    # input for an application for start
    fileName = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(fileName)

    # create a label for every stored app
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()  # attach label in the UI


# function to run all of the stores applications
def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()  # create the main UI

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()  # attach the 'open file' button to the UI

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()  # attach the 'run apps' button to the UI

# pack the stored app links onto to the main UI
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# store applications inside a new text file 'save.txt' for future retrieval
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ",")
