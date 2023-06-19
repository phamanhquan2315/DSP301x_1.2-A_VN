try:
    getfile = open("myfile","r")
    getfile.write("Myfile for exception handling")
except IOError :
    print("Unable open and read data")
else: 
    print("the file was written successfully")
finally:
    
    print("file closed")
    