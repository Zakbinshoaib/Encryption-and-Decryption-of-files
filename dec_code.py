from tkinter import filedialog
from cryptography.fernet import Fernet
import os

def openfile():
    file = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
    )
    return file

newfile = openfile()

with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

print(newfile)
extension = os.path.splitext(newfile)[1]
name = os.path.splitext(os.path.basename(newfile))[0]
denc_file = "denc_" + name + extension


with open(newfile, "r") as key_file:
    read = key_file.read()

decrypted = Fernet(key).decrypt(read).decode()


with open(denc_file, "w") as file:
    file.write(decrypted)