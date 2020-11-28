# https://github.com/boehs/discord-auth-bot/blob/master/keygenerator.py

import re
import random
import string

def genkey(length, ovr):
  if not ovr:
    keytxt = open("keys.txt","a")
  if ovr:
    keytxt = open("keys.txt","w")
  letters_and_digits = string.ascii_uppercase + string.digits
  result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
  keytxt.write(result_str + "\n")
  return result_str

if __name__ == "__main__":
  while True:
    keynum = input("How many keys do you want to generate?: ")
    try:
        int(keynum)
    except:
        #is not int
        print("Hmm, thats not right!")
    else:
        # is a int
        keynum = int(keynum)
        break
    
  while True:
    ovrwrite = input("""Do you wish to overwrite the file? (Please Write "Yes" Or "No"): """)
    if (re.search(r'(Yes|1)', ovrwrite, re.IGNORECASE)):
      ovrwrite = False # We set overwrite to false here so that in the main loop the file is not overwritten everytime the def runs (a lot - runs for as much as keynum is set to)
      open("keys.txt", 'w').close() # we just clear the file once 
      break
    elif (re.search(r'(No|2)', ovrwrite, re.IGNORECASE)):
      ovrwrite = False
      break
    else:
      print("Hmm, did'ent quite get that. lets try again!")
  print("""great! we got all that. we will make changes inside a file in the same folder as this program. the file will be named "keys.txt"! for next steps, refer to "INSTRUCTIONS.md".""")

  while keynum > 0:
    keystore = genkey(int(6), ovrwrite)
    keynum = keynum - 1
    print(keystore)