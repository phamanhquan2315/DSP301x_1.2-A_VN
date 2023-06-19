import numpy as np
import pandas as pd
filename = input("input the file name: ")

try :
    if filename =="class1":
        with open("class1.txt","r") as f:
            file = f.readlines()
        print("Successfully opened", filename + ".txt")
        print('Total lines of data:', len(file))

    elif filename == "class2":
        with open("class2.txt","r") as f:
            file = f.readlines()
        print("Successfully opened", filename + ".txt")
        print('Total lines of data:', len(file))

except IOError:
    print("Sorry, I can't find this filename")
