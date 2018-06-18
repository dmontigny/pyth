temps=[10, -20, -289, 100]

def c_to_f():
    with open("temps.txt", "w") as tempsfile:
        for c in temps:
            if c >= -273.15:
                tempsfile.write(str(c * 9/5 + 32) + "\n")
            else:
                print('invalid temp')

def file_merge():
    from datetime import datetime
    with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S.txt") , "w") as ofile:
        with open("file1.txt" , "r") as file1:
            ofile.write(file1.read() + "\n")
        with open("file2.txt" , "r") as file2:
            ofile.write(file2.read() + "\n")
        with open("file3.txt" , "r") as file3:
            ofile.write(file3.read() + "\n")
