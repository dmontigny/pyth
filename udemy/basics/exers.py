from builtins import int

def get_length(txt):
    if type(txt) == int:
        print('Sorry intergers don\'t have length')
        return
    elif type(txt) == float:
        print('Sorry floats don\'t have length')
        return
    else:
        return len(txt)

def c_to_f(cel):
    if cel < -273.15:
        print('invalid temp')
    return cel * 9/5 + 32

def test_temps():
    temps=[10,-20,-289,100]
    for item in temps:
        print(c_to_f(item))

def len_lines():
    myfile = open('fruits.txt')
    c = myfile.read()
    myfile.close()
    c = c.splitlines()
    for item in c:
        print(len(item))
    return

def write_file():
    myfile=open('employees.txt., w')