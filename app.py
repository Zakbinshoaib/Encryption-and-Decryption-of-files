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

print(newfile)
extension = os.path.splitext(newfile)[1]
name = os.path.splitext(os.path.basename(newfile))[0]
enc_file = "enc_" + name + extension


key = Fernet.generate_key()

with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)


with open(newfile, "r") as key_file:
    read = key_file.read()


encrypted = Fernet(key).encrypt(read.encode())

with open(enc_file, "wb") as file:
    file.write(encrypted)


