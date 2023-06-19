with open("promayhem.txt", "r") as f:
    l = f.readlines()
for i in l: 
    if i[0] == '0' : l.remove(i)
    if i[0] == '1' : l.remove(i)
    if i[0] == '2' : l.remove(i)
    if i[0] == '3' : l.remove(i)
    if i[0] == ' ' : l.remove(i)
    if i[0] == '\n' : l.remove(i)
    if i[0] == '4' : l.remove(i)
    if i[0] == '5' : l.remove(i)
    if i[0] == '6' : l.remove(i)
    if i[0] == '7' : l.remove(i)
    if i[0] == '8' : l.remove(i)
    if i[0] == '9' : l.remove(i)


for i in l:
    if i[0] == '1': l.remove(i)
    if i[0] == '2' : l.remove(i)
    if i[0] == '3' : l.remove(i)
    if i[0] == '4' : l.remove(i)
    if i[0] == '5' : l.remove(i)
    if i[0] == '6' : l.remove(i)
    if i[0] == '7' : l.remove(i)
    if i[0] == '8' : l.remove(i)
    if i[0] == '9' : l.remove(i)
g = open("demofile2.txt", "a")
fls
    or i in l: g.write(i)