import os

KEYWORD = 'import'
def modulesList(filename,modules = []):
    path = os.getcwd()
    file = os.path.join(path,filename)
    print file
    fobj = open(file,'r')
    for line in fobj.readlines():
        if KEYWORD in line:
            linewithoutSpace = line.strip().replace(' ','')
            print line, linewithoutSpace
            print "this is a modules"
            index = linewithoutSpace.find(KEYWORD)
            if 'from' in line:
            # from ..import..
                indexFrom = linewithoutSpace.find('from')
                tempMod1 = linewithoutSpace[indexFrom+4:index]
                modules.append(tempMod1)
            else:
            # import ..
                tempMods1 = linewithoutSpace[index+6:].split(',')
                modules = modules+tempMods1
    return list(set(modules))


if __name__ == '__main__':
    print modulesList('test.py',['os'])
