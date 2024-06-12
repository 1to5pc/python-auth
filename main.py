# initialise required libs
import art
import usrcheck
import random
quiet,alg,saltSize,artConf=usrcheck.configRead()
if artConf==True:
  # initialise ASCII art
  # Define the ASCII art for the text
  text_art = r"""
    ____        _   _                 
   |  _ \ _   _| |_| |__   ___  _ __  
   | |_) | | | | __| '_ \ / _ \| '_ \ 
   |  __/| |_| | |_| | | | (_) | | | |
   |_|    \__, |\__|_| |_|\___/|_| |_|
          |___/                       
  """

  # Define the ASCII art for the cat
  cat_art = r"""
   /\_/\  
  ( o.o ) 
   > ^ <
  """
  # initialise other required python files

  combined_art = art.insert_cat_randomly(text_art, cat_art)
  print(combined_art)

if __name__ == "__main__":
    while True:
      usrcheck.main_menu()