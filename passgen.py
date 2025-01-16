## Password generator
## Author: ANgel Mariscurrena
## Inspo: W J Pearce

import random
import string as str

def genpass(lenght: int = 10): #If argument is not set, the utility set a default parameter of ten
    alphabet = str.ascii_letters + str.digits + str.punctuation ##Store all the ascii letters, all the digits and all the punctuation signs into the US and UK system
    pwd = ''.join(random.choice(alphabet) for i in range(lenght)) ##Randomly choose a character of the alphabet array defined before for every caracter of the password (use lenght value) and concatenate this to a blank string, setting in this way a random password
    return pwd #Return password

print("Welcome to this Password Generator!!")
lenght = input("Insert the desired password lenght: ")
password = genpass(int(lenght))
print(f"Generated Password: {password}")