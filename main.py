import os
from time import sleep

# Переходим в библиотеку BIN
input_dir = input("List scripts? [Y/n]")

if input_dir == "Y" or "y":
  os.chdir("scripts")

if input_dir == "n" or "N":
  exit()
