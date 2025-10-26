with open("file1.txt","a")as f:
    f.write("welcome to the python life")
    f.close

with open("file1.txt","a")as f:
    print(f.read())