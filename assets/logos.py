from classes.colours import bcolors
import time

def main_logo():
   print(f'''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bcolors.OKGREEN}{bcolors.BOLD} 
      ______          __     _____ __                     
     / ____/__  _____/ /_   / ___// /___ ___  _____  _____
    / /   / _ \/ ___/ __/   \__ \/ / __ \`/ / / / _ \/ ___/
   / /___/  __/ /  / /_    ___/ / / /_/ / /_/ /  __/ /    
   \____/\___/_/   \__/   /____/_/\__,_/\__, /\___/_/     
                                       /____/             
   {bcolors.ENDC}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n''')
   time.sleep(5)

def game_over():
   print(f'''\n\n\n{bcolors.OKGREEN}{bcolors.BOLD} 

      ______                        ____                 
     / ____/___ _____ ___  ___     / __ \_   _____  _____
    / / __/ __ `/ __ `__ \/ _ \   / / / / | / / _ \/ ___/
   / /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /    
   \____/\__,_/_/ /_/ /_/\___/   \____/ |___/\___/_/     
                                                      

   {bcolors.ENDC}\n\n\n''')




